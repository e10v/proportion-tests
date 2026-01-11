from __future__ import annotations

import argparse
import concurrent.futures
import functools
import tomllib
from typing import TYPE_CHECKING

import numpy as np
import polars as pl
import scipy.stats
import tea_tasting as tt
import tqdm


if TYPE_CHECKING:
    from typing import TextIO


MAX_EXACT_OBS = 100
MAX_PROP = 0.9

EXACT = {
    "barnard": tt.Proportion("value", method="barnard", equal_var=False),
    "barnard pooled": tt.Proportion("value", method="barnard", equal_var=True),
    "boschloo": tt.Proportion("value", method="boschloo"),
    "fisher": tt.Proportion("value", method="fisher"),
}

APPROX = {
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
    *,
    output: str,
    seed: int,
    n_simulations: int,
    n_obs_small: int,
    n_obs_large: int,
    unbalanced_ratio: float,
    unbalanced_prop: float,
) -> None:
    file = open(output, mode="w")  # noqa: SIM115
    file.write("# Comparison of two-sample proportion tests\n")

    file.write("\n## Small sample\n")
    n_obs = n_obs_small
    run_aa_and_power_tests(
        "Balanced ratio, balanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
    )
    run_aa_and_power_tests(
        "Balanced ratio, unbalanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        prop=unbalanced_prop,
    )
    run_aa_and_power_tests(
        "Unbalanced ratio, balanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=unbalanced_ratio,
    )
    run_aa_and_power_tests(
        "Unbalanced ratio, unbalanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=unbalanced_ratio,
        prop=unbalanced_prop,
    )

    file.write("\n## Large sample\n")
    n_obs = n_obs_large
    run_aa_and_power_tests(
        "Balanced ratio, balanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
    )
    run_aa_and_power_tests(
        "Balanced ratio, unbalanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        prop=unbalanced_prop,
    )
    run_aa_and_power_tests(
        "Unbalanced ratio, balanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=unbalanced_ratio,
    )
    run_aa_and_power_tests(
        "Unbalanced ratio, unbalanced proportion",
        file,
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=unbalanced_ratio,
        prop=unbalanced_prop,
    )

    file.close()


def run_aa_and_power_tests(
    header: str,
    file: TextIO,
    *,
    seed: int,
    n_simulations: int,
    n_obs: int,
    ratio: float = 1,
    prop: float = 0.5,
) -> None:
    file.write(f"\n### {header}\n")

    file.write("\nAA tests\n")
    aa_params, aa_results = run_tests(
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=ratio,
        prop=prop,
        aa_tests=True,
    )
    with pl.Config(
        tbl_formatting="MARKDOWN",
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
        tbl_rows=-1,
    ):
        file.write("\n" + str(aa_params) + "\n")
        file.write("\n" + str(aa_results) + "\n")

    file.write("\nPower tests\n")
    power_params, power_results = run_tests(
        seed=seed,
        n_simulations=n_simulations,
        n_obs=n_obs,
        ratio=ratio,
        prop=prop,
        aa_tests=False,
    )
    with pl.Config(
        tbl_formatting="MARKDOWN",
        tbl_hide_column_data_types=True,
        tbl_hide_dataframe_shape=True,
        tbl_rows=-1,
    ):
        file.write("\n" + str(power_params) + "\n")
        file.write("\n" + str(power_results) + "\n")


def run_tests(
    *,
    seed: int,
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
        except:  # noqa: E722
            effect_size = MAX_PROP - prop
        rate_col = "power"

    metrics = APPROX if n_obs > MAX_EXACT_OBS else EXACT | APPROX
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
            descending=True,
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
