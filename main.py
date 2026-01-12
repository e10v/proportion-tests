from __future__ import annotations

import argparse
import concurrent.futures
import functools
import tomllib

import numpy as np
import polars as pl
import scipy.stats
import tea_tasting as tt
import tqdm


MAX_PROP = 0.9
MAX_SLOW_OBS = 100

SLOW = {
    "barnard": tt.Proportion("value", method="barnard", equal_var=False),
    "barnard pooled": tt.Proportion("value", method="barnard", equal_var=True),
    "boschloo": tt.Proportion("value", method="boschloo"),
}

FAST = {
    "fisher": tt.Proportion("value", method="fisher"),
    "log-likelihood": tt.Proportion("value", method="log-likelihood", correction=False),
    "log-likelihood cc": tt.Proportion(
        "value", method="log-likelihood", correction=True),
    "pearson": tt.Proportion("value", method="pearson", correction=False),
    "pearson cc": tt.Proportion("value", method="pearson", correction=True),
    "norm": tt.Proportion("value", method="norm", correction=False, equal_var=False),
    "norm pooled": tt.Proportion(
        "value", method="norm", correction=False, equal_var=True),
    "norm cc": tt.Proportion("value", method="norm", correction=True, equal_var=False),
    "norm pooled cc": tt.Proportion(
        "value", method="norm", correction=True, equal_var=True),
    "mean z-test": tt.Mean("value", use_t=False, equal_var=False),
    "mean z-test pooled": tt.Mean("value", use_t=False, equal_var=True),
    "mean t-test": tt.Mean("value", use_t=True, equal_var=False),
    "mean t-test pooled": tt.Mean("value", use_t=True, equal_var=True),
}


def main(
    output: str,
    seed: int,
    *,
    n_simulations: int,
    n_obs_small: int,
    n_obs_large: int,
    unbalanced_ratio: float,
    unbalanced_prop: float,
) -> None:
    write_text(
        output,
        "# Comparison of two-sample proportion tests",
        mode="w",
        br_before=False,
    )
    for size, n_obs in (("Small", n_obs_small), ("Large", n_obs_large)):
        write_text(output, f"## {size} sample")
        run_aa_and_power_tests(
            output,
            "### Balanced ratio, balanced proportion",
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
        )
        run_aa_and_power_tests(
            output,
            "### Balanced ratio, unbalanced proportion",
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
            prop=unbalanced_prop,
        )
        run_aa_and_power_tests(
            output,
            "### Unbalanced ratio, balanced proportion",
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=unbalanced_ratio,
        )
        run_aa_and_power_tests(
            output,
            "### Unbalanced ratio, unbalanced proportion",
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=unbalanced_ratio,
            prop=unbalanced_prop,
        )


def run_aa_and_power_tests(
    output: str,
    header: str,
    *,
    seed: int,
    n_simulations: int,
    n_obs: int,
    ratio: float = 1,
    prop: float = 0.5,
) -> None:
    write_text(output, header)
    for test_type, aa_tests in (("AA", True), ("Power", False)):
        write_text(output, f"{test_type} tests")
        write_data(output, *run_tests(
            seed=seed,
            n_simulations=n_simulations,
            n_obs=n_obs,
            ratio=ratio,
            prop=prop,
            aa_tests=aa_tests,
        ))


def run_tests(
    seed: int,
    *,
    n_simulations: int,
    n_obs: int,
    ratio: float = 1,
    prop: float = 0.5,
    aa_tests: bool = True,
) -> tuple[pl.DataFrame, pl.DataFrame]:
    if aa_tests:
        effect_size = 0
        rate_col = "type I error"
    else:
        data = make_data(seed, n_obs=n_obs, prop=prop)
        try:
            effect_size = min(
                tt.Mean("value", ratio=ratio)
                    .solve_power(data, "effect_size")[0]
                    .effect_size,
                MAX_PROP - prop,
            )
        except Exception:
            effect_size = MAX_PROP - prop
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
            ("number of simulations", n_simulations),
            ("number of observations", n_obs),
            ("treatment to control ratio", ratio),
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
            pl.col("pvalue").le(tt.get_config("alpha"))
                .cast(int).sum().alias("null rejected"),
            pl.col("pvalue").count().alias("not nan"),
        )
        .sort(
            pl.col("null rejected").truediv(pl.col("not nan")),
            "metric",
            descending=(True, False),
        )
        .select(
            "metric",
            pl.col("null rejected")
                .truediv(pl.col("not nan"))
                .map_elements(lambda x: f"{x:.3f}")
                .alias(rate_col),
            pl.col("null rejected")
                .map_elements(
                    functools.partial(calc_ci, n=n_simulations),
                    return_dtype=pl.String,
                )
                .alias(rate_col + " ci"),
        )
        .collect()
    )


def make_data(
    seed: int | np.random.Generator,
    *,
    n_obs: int,
    ratio: float = 1,
    prop: float = 0.5,
    effect_size: float = 0,
) -> pl.DataFrame:
    rng = np.random.default_rng(seed=seed)
    variant = rng.binomial(n=1, p=ratio / (1 + ratio), size=n_obs)
    value = rng.binomial(n=1, p=prop + effect_size*variant, size=n_obs)
    return pl.DataFrame({"variant": variant, "value": value})


def calc_ci(k: int, n: int) -> str:
    ci_lower, ci_upper = scipy.stats.binomtest(k, n).proportion_ci(method="wilsoncc")
    return f"[{ci_lower:.3f}, {ci_upper:.3f}]"


def write_text(
    output: str,
    text: str,
    *,
    mode: str = "a",
    br_before: bool=True,
    br_after: bool=True,
) -> None:
    with open(output, mode) as f:
        if br_before:
            f.write("\n")
        f.write(text)
        if br_after:
            f.write("\n")


def write_data(output: str, *data: pl.DataFrame) -> None:
    with pl.Config(
        tbl_formatting="MARKDOWN",
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
        tbl_rows=-1,
        fmt_float="full",
    ):
        write_text(output, "\n\n".join(str(df).replace("|--", "|:-") for df in data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="config.toml",
        help="Config file",
        required=False,
    )
    with open(parser.parse_args().config, "rb") as f:
        config = tomllib.load(f)
    main(**config)
