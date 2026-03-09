from __future__ import annotations

import concurrent.futures
import functools
import math
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
import scipy.stats
import tea_tasting as tt
import tea_tasting.utils
import tqdm

import proportion_tests.config
import proportion_tests.data
import proportion_tests.utils


if TYPE_CHECKING:
    from typing import Any

    import tea_tasting.metrics  # noqa: TC004


MAX_EFFECT_SIZE_ERROR = 0.05
MAX_EFFECT_SIZE_ITER = 100
MAX_PROP = 0.9


def main() -> None:
    config = proportion_tests.config.load_config()
    generate_simulation_report(
        rng=config["rng"],
        samples=config["samples"],
        tests=config["tests"],
        **config["simulation"],
    )


def generate_simulation_report(
    rng: int | np.random.Generator,
    samples: dict[str, int],
    tests: list[dict[str, Any]],
    n_simulations: int,
    alpha: float,
    power: float,
    options: list[dict[str, Any]],
    output: str,
) -> None:
    rng = np.random.default_rng(rng)

    report = ["# Simulation"]
    report.append(proportion_tests.utils.render_dict({
        "number of simulations": n_simulations,
        "alpha": alpha,
        "power": power,
    }))

    for sample_name, sample_size in samples.items():
        tqdm.tqdm.write(f"{sample_name} sample: {sample_size}")
        report.append(f"## {sample_name.capitalize()} sample")
        metrics = proportion_tests.utils.filter_metrics(
            tests,
            key="max_simulation_size",
            sample_size=sample_size,
        )

        for option in options:
            tqdm.tqdm.write(f"  option: {option["name"]}")
            report.append(f"### {option["name"].capitalize()}")
            aa_result, power_result = (
                run_simulation(
                    rng.spawn(1)[0],
                    metrics,
                    sample_size=sample_size,
                    n_simulations=n_simulations,
                    alpha=alpha,
                    power=power,
                    ratio=option["ratio"],
                    prop=option["prop"],
                    is_aa=is_aa,
                )
                for is_aa in (True, False)
            )

            report.append(proportion_tests.utils.render_dict({
                "sample size": sample_size,
                "treatment to control allocation ratio": option["ratio"],
                "proportion in control": option["prop"],
            }))

            report.append(proportion_tests.utils.render_dicts(
                power_result.lazy()
                .join(aa_result.lazy(), on="test")
                .sort("power", "type I error", "test", descending=(True, False, False))
                .select(
                    "test",
                    pl.col("power").map_elements(tea_tasting.utils.format_num),
                    pl.col("power ci")
                        .map_elements(proportion_tests.utils.format_ci, pl.String),
                    pl.col("type I error").map_elements(tea_tasting.utils.format_num),
                    pl.col("type I error ci")
                        .map_elements(proportion_tests.utils.format_ci, pl.String),
                )
                .collect()
                .to_dicts(),  # ty:ignore[unresolved-attribute]
            ))

    with open(output, "w") as f:
        f.write("\n\n".join(report) + "\n")


def run_simulation(
    rng: int | np.random.Generator,
    metrics: dict[str, tea_tasting.metrics.MetricBase],
    *,
    sample_size: int,
    n_simulations: int,
    alpha: float,
    power: float,
    ratio: float,
    prop: float,
    is_aa: bool,
) -> pl.DataFrame:
    rng = np.random.default_rng(rng)
    if is_aa:
        effect_size = 0
        rate_col = "type I error"
    else:
        z_stat = scipy.stats.norm.isf(alpha / 2) + scipy.stats.norm.ppf(power)
        effect_size = min(
            calc_effect_size(
                sample_size=sample_size,
                ratio=ratio,
                prop=prop,
                z_stat=z_stat,
            ),
            MAX_PROP - prop,
        )
        rate_col = "power"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = tt.Experiment(metrics).simulate(
            functools.partial(
                proportion_tests.data.make_data,
                sample_size=sample_size,
                ratio=ratio,
                prop=prop,
                effect_size=effect_size,
            ),  # ty:ignore[invalid-argument-type]
            n_simulations=n_simulations,
            rng=rng,
            map_=executor.map,
            progress=functools.partial(
                tqdm.tqdm,
                desc=f"    {rate_col.capitalize()} simulation",
            ),
        )

    return (
        result.to_polars().lazy()
        .filter(pl.col("pvalue").is_not_nan())
        .group_by("metric")
        .agg(
            pl.col("pvalue").le(alpha).cast(int).sum().alias("null rejected"),
            pl.col("pvalue").count().alias("total"),
        )
        .select(
            pl.col("metric").alias("test"),
            pl.col("null rejected").truediv(pl.col("total")).alias(rate_col),
            pl.concat_list("null rejected", "total")
                .map_elements(calc_binom_ci, return_dtype=pl.List(pl.Float64))
                .alias(rate_col + " ci"),
        )
        .collect()  # ty:ignore[invalid-return-type]
    )


def calc_effect_size(
    sample_size: int,
    ratio: float,
    prop: float,
    z_stat: float,
    prev_effect_size: float = 0,
    n_iter: int = 1,
) -> float:
    effect_size = z_stat * calc_scale(
        sample_size=sample_size,
        ratio=ratio,
        prop=prop,
        effect_size=prev_effect_size,
    )

    if (
        n_iter >= MAX_EFFECT_SIZE_ITER or
        abs(prev_effect_size/effect_size - 1) < MAX_EFFECT_SIZE_ERROR
    ):
        return effect_size

    return calc_effect_size(
        sample_size=sample_size,
        ratio=ratio,
        prop=prop,
        z_stat=z_stat,
        prev_effect_size=effect_size,
        n_iter=n_iter + 1,
    )


def calc_scale(
    sample_size: int,
    ratio: float,
    prop: float,
    effect_size: float = 0,
) -> float:
    n0 = sample_size / (1 + ratio)
    n1 = sample_size * ratio / (1 + ratio)
    p = (prop * n0 + (prop + effect_size) * n1) / sample_size
    return math.sqrt(p * (1 - p) * (1/n0 + 1/n1))


def calc_binom_ci(k_n: list[int]) -> list[float]:
    k, n = k_n
    low, upp = scipy.stats.binomtest(k, n).proportion_ci(method="wilsoncc")
    return [low, upp]
