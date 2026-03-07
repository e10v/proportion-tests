from __future__ import annotations

import argparse
import concurrent.futures
import functools
import math
import tomllib

import numpy as np
import polars as pl
import scipy.stats
import tea_tasting as tt
import tea_tasting.aggr
import tqdm


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
    seed: int,
    *,
    n_simulations: int,
    n_obs_small: int,
    n_obs_large: int,
    imbalanced_ratio: float,
    imbalanced_prop: float,
    alpha: float,
    power: float,
) -> None:
    write_text(
        output,
        "# Comparison of two-sample proportion tests",
        mode="w",
        new_line_before=False,
    )
    write_data(output, pl.from_records(
        (
            ("number of simulations", n_simulations),
            ("alpha", alpha),
            ("power", power),
        ),
        schema=("parameter", "value"),
        orient="row",
    ))
    for size, n_obs in (("Small", n_obs_small), ("Large", n_obs_large)):
        write_text(output, f"## {size} sample")
        append_simulation_results(
            output,
            "### Balanced ratio, balanced proportion",
            seed=seed,
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
            seed=seed,
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
            seed=seed,
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
            seed=seed,
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
    seed: int,
    n_simulations: int,
    n_obs: int,
    ratio: float,
    prop: float,
    alpha: float,
    power: float,
) -> None:
    write_text(output, header)
    for test_type, is_aa in (("A/A", True), ("Power", False)):
        write_text(output, f"{test_type} tests")
        write_data(output, *simulate_experiments(
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=ratio,
            prop=prop,
            is_aa=is_aa,
            alpha=alpha,
            power=power,
        ))


def simulate_experiments(
    seed: int,
    *,
    n_simulations: int,
    n_obs: int,
    ratio: float,
    prop: float,
    is_aa: bool,
    alpha: float,
    power: float,
) -> tuple[pl.DataFrame, pl.DataFrame]:
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
        results = tt.Experiment(metrics).simulate(
            functools.partial(
                make_data,
                n_obs=n_obs,
                ratio=ratio,
                prop=prop,
                effect_size=effect_size,
            ),
            n_simulations=n_simulations,
            seed=seed,
            map_=executor.map,
            progress=tqdm.tqdm,
        )

    params = pl.from_records(
        (
            ("number of observations", n_obs),
            ("treatment to control allocation ratio", ratio),
            ("proportion in control", prop),
            ("effect size", round(effect_size, 3)),
            ("relative effect size", round(effect_size / prop, 2)),
        ),
        schema=("parameter", "value"),
        orient="row",
    )

    return params, (
        results.to_polars().lazy()
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
    )  # ty:ignore[invalid-return-type]


def make_data(
    seed: int | np.random.Generator,
    *,
    n_obs: int,
    ratio: float,
    prop: float,
    effect_size: float,
) -> dict[object, tea_tasting.aggr.Aggregates]:
    rng = np.random.default_rng(seed=seed)
    n0 = np.clip(rng.binomial(n=n_obs, p=1 / (1 + ratio)), 2, n_obs - 2)
    n1 = n_obs - n0
    k0 = rng.binomial(n=n0, p=prop)
    k1 = rng.binomial(n=n1, p=prop + effect_size)
    m0 = k0 / n0
    m1 = k1 / n1
    v0 = m0 * (1 - m0) * n0 / (n0 - 1)
    v1 = m1 * (1 - m1) * n1 / (n1 - 1)
    return {
        0: tea_tasting.aggr.Aggregates(
            count_=n0,
            mean_={"value": m0},
            var_={"value": v0},
        ),
        1: tea_tasting.aggr.Aggregates(
            count_=n1,
            mean_={"value": m1},
            var_={"value": v1},
        ),
    }


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


def write_text(
    output: str,
    text: str,
    *,
    mode: str = "a",
    new_line_before: bool=True,
) -> None:
    with open(output, mode) as f:
        if new_line_before:
            f.write("\n")
        f.write(text + "\n")


def write_data(output: str, *data: pl.DataFrame) -> None:
    with pl.Config(
        fmt_float="full",
        fmt_str_lengths=50,
        tbl_formatting="MARKDOWN",
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
        tbl_rows=-1,
    ):
        write_text(output, "\n\n".join(str(df).replace("|--", "|:-") for df in data))


if __name__ == "__main__":
    main()
