from __future__ import annotations

import argparse
import timeit
import tomllib

import tea_tasting as tt
import tea_tasting.utils

import utils


TESTS = {
    "barnard": tt.Proportion("value", method="barnard", equal_var=True),
    "boschloo": tt.Proportion("value", method="boschloo"),
    "fisher": tt.Proportion("value", method="fisher"),
    "log-likelihood": tt.Proportion("value", method="log-likelihood", correction=False),
    "pearson": tt.Proportion("value", method="pearson", correction=False),
    "norm": tt.Proportion("value", method="norm", correction=False, equal_var=True),
    "mean z-test": tt.Mean("value", use_t=False, equal_var=True),
    "mean t-test": tt.Mean("value", use_t=True, equal_var=True),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="benchmark.toml",
        help="Config file",
        required=False,
    )
    with open(parser.parse_args().config, "rb") as f:
        config = tomllib.load(f)
    generate_benchmark_report(**config)


def generate_benchmark_report(
    output: str,
    rng: int,
    *,
    n_obs: int,
    repeat: int,
    number: int,
) -> None:
    utils.write_text(
        output,
        "# Benchmark of two-sample proportion tests",
        mode="w",
        new_line_before=False,
    )
    utils.write_params(output, {
        "number of observations": n_obs,
        "number of runs": repeat,
        "number of repeats per run": number,
    })
    data = utils.make_data(rng, n_obs=n_obs)
    results = []

    for metric, test in TESTS.items():
        print(metric)
        t = timeit.repeat(
            "test.analyze_aggregates(data[0], data[1])",
            repeat=repeat,
            number=number,
            globals={"test": test, "data": data},
        )
        results.append({
            "metric": metric,
            "time, ms": tea_tasting.utils.format_num(min(t) * 1000 / number),
        })

    utils.write_dicts(output, results, text_keys=("metric",))


if __name__ == "__main__":
    main()
