from __future__ import annotations

import argparse
import concurrent.futures
import functools
import math
import tomllib
from typing import TYPE_CHECKING

import polars as pl
import scipy.stats
import tea_tasting as tt
import tqdm

import utils


if TYPE_CHECKING:
    from typing import Any


MAX_EFFECT_SIZE_ERROR = 0.05
MAX_EFFECT_SIZE_ITER = 100
MAX_PROP = 0.9
MAX_SLOW_OBS = 100

SLOW = {
    "barnard": tt.Proportion("value", method="barnard", equal_var=True),
    "barnard unpooled": tt.Proportion("value", method="barnard", equal_var=False),
    "boschloo": tt.Proportion("value", method="boschloo"),
}

FAST = {
    "fisher": tt.Proportion("value", method="fisher"),
    "log-likelihood": tt.Proportion("value", method="log-likelihood", correction=False),
    "log-likelihood cc": tt.Proportion(
        "value", method="log-likelihood", correction=True),
    "pearson": tt.Proportion("value", method="pearson", correction=False),
    "pearson cc": tt.Proportion("value", method="pearson", correction=True),
    "norm": tt.Proportion("value", method="norm", correction=False, equal_var=True),
    "norm unpooled": tt.Proportion(
        "value", method="norm", correction=False, equal_var=False),
    "norm cc": tt.Proportion("value", method="norm", correction=True, equal_var=True),
    "norm unpooled cc": tt.Proportion(
        "value", method="norm", correction=True, equal_var=False),
    "mean z-test": tt.Mean("value", use_t=False, equal_var=True),
    "mean z-test unpooled": tt.Mean("value", use_t=False, equal_var=False),
    "mean t-test": tt.Mean("value", use_t=True, equal_var=True),
    "mean t-test unpooled": tt.Mean("value", use_t=True, equal_var=False),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="simulation.toml",
        help="Config file",
        required=False,
    )
    with open(parser.parse_args().config, "rb") as f:
        config = tomllib.load(f)
    generate_simulation_report(**config)


def generate_simulation_report(
    output: str,
    rng: int,
    *,
    n_simulations: int,
    n_obs_small: int,
    n_obs_large: int,
    imbalanced_ratio: float,
    imbalanced_prop: float,
    alpha: float,
    power: float,
) -> None:
    utils.write_text(
        output,
        "# Comparison of two-sample proportion tests",
        mode="w",
        new_line_before=False,
    )
    utils.write_params(output, {
        "number of simulations": n_simulations,
        "alpha": alpha,
        "power": power,
    })
    for size, n_obs in (("Small", n_obs_small), ("Large", n_obs_large)):
        utils.write_text(output, f"## {size} sample")
        append_simulation_results(
            output,
            "### Balanced ratio, balanced proportion",
            rng=rng,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=1,
            prop=0.5,
            alpha=alpha,
            power=power,
        )
        append_simulation_results(
            output,
            "### Balanced ratio, imbalanced proportion",
            rng=rng,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=1,
            prop=imbalanced_prop,
            alpha=alpha,
            power=power,
        )
        append_simulation_results(
            output,
            "### Imbalanced ratio, balanced proportion",
            rng=rng,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=imbalanced_ratio,
            prop=0.5,
            alpha=alpha,
            power=power,
        )
        append_simulation_results(
            output,
            "### Imbalanced ratio, imbalanced proportion",
            rng=rng,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=imbalanced_ratio,
            prop=imbalanced_prop,
            alpha=alpha,
            power=power,
        )


def append_simulation_results(
    output: str,
    header: str,
    *,
    rng: int,
    n_simulations: int,
    n_obs: int,
    ratio: float,
    prop: float,
    alpha: float,
    power: float,
) -> None:
    utils.write_text(output, header)
    for test_type, is_aa in (("A/A", True), ("Power", False)):
        utils.write_text(output, f"{test_type} simulations")
        params, results = simulate_experiments(
            rng=rng,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=ratio,
            prop=prop,
            is_aa=is_aa,
            alpha=alpha,
            power=power,
        )
        utils.write_params(output, params)
        utils.write_results(output, results)


def simulate_experiments(
    rng: int,
    *,
    n_simulations: int,
    n_obs: int,
    ratio: float,
    prop: float,
    is_aa: bool,
    alpha: float,
    power: float,
) -> tuple[dict[str, Any], pl.DataFrame]:
    if is_aa:
        effect_size = 0
        rate_col = "type I error"
    else:
        z_stat = scipy.stats.norm.isf(alpha / 2) + scipy.stats.norm.ppf(power)
        effect_size = min(
            calc_effect_size(n_obs=n_obs, ratio=ratio, prop=prop, z_stat=z_stat),
            MAX_PROP - prop,
        )
        rate_col = "power"

    metrics = FAST if n_obs > MAX_SLOW_OBS else SLOW | FAST
    with concurrent.futures.ProcessPoolExecutor() as executor:
        simulation_results = tt.Experiment(metrics).simulate(  # ty:ignore[invalid-argument-type]
            functools.partial(
                utils.make_data,
                n_obs=n_obs,
                ratio=ratio,
                prop=prop,
                effect_size=effect_size,
            ),
            n_simulations=n_simulations,
            rng=rng,
            map_=executor.map,
            progress=tqdm.tqdm,
        )

    params = {
        "number of observations": n_obs,
        "treatment to control allocation ratio": ratio,
        "proportion in control": prop,
        "effect size": round(effect_size, 3),
        "relative effect size": round(effect_size / prop, 2),
    }

    results: pl.DataFrame = (
        simulation_results.to_polars().lazy()
        .filter(pl.col("pvalue").is_not_nan())
        .group_by("metric")
        .agg(
            pl.col("pvalue").le(alpha).cast(int).sum().alias("null rejected"),
            pl.col("pvalue").count().alias("total"),
        )
        .sort(
            pl.col("null rejected").truediv(pl.col("total")),
            "metric",
            descending=(True, False),
        )
        .select(
            "metric",
            pl.col("null rejected")
                .truediv(pl.col("total"))
                .map_elements(lambda x: f"{x:.3f}")
                .alias(rate_col),
            pl.col("null rejected")
                .map_elements(
                    functools.partial(calc_binom_ci, n=n_simulations),
                    return_dtype=pl.String,
                )
                .alias(rate_col + " ci"),
        )
        .collect()
    )  # ty:ignore[invalid-assignment]

    return params, results


def calc_effect_size(
    n_obs: int,
    ratio: float,
    prop: float,
    z_stat: float,
    prev_effect_size: float = 0,
    n_iter: int = 1,
) -> float:
    effect_size = z_stat * calc_scale(
        n_obs=n_obs,
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
        n_obs=n_obs,
        ratio=ratio,
        prop=prop,
        z_stat=z_stat,
        prev_effect_size=effect_size,
        n_iter=n_iter + 1,
    )


def calc_scale(prop: float, n_obs: int, ratio: float, effect_size: float = 0) -> float:
    n0 = n_obs / (1 + ratio)
    n1 = n_obs * ratio / (1 + ratio)
    p = (prop * n0 + (prop + effect_size) * n1) / n_obs
    return math.sqrt(p * (1 - p) * (1/n0 + 1/n1))


def calc_binom_ci(k: int, n: int) -> str:
    ci_lower, ci_upper = scipy.stats.binomtest(k, n).proportion_ci(method="wilsoncc")
    return f"[{ci_lower:.3f}, {ci_upper:.3f}]"


if __name__ == "__main__":
    main()
