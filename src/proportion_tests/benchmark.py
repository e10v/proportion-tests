from __future__ import annotations

import timeit
from typing import TYPE_CHECKING

import numpy as np
import tqdm

import proportion_tests.config
import proportion_tests.data
import proportion_tests.utils


if TYPE_CHECKING:
    from typing import Any

    import tea_tasting.aggr
    import tea_tasting.metrics


def main() -> None:
    config = proportion_tests.config.load_config()
    generate_benchmark_report(
        rng=config["rng"],
        samples=config["samples"],
        tests=config["tests"],
        **config["benchmark"],
    )


def generate_benchmark_report(
    rng: int | np.random.Generator,
    samples: dict[str, int],
    tests: list[dict[str, Any]],
    repeat: int,
    number: int,
    output: str,
) -> None:
    rng = np.random.default_rng(rng)
    results = {}
    for sample_name, sample_size in samples.items():
        tqdm.tqdm.write(f"{sample_name} sample: {sample_size}")
        metrics = proportion_tests.utils.filter_metrics(
            tests,
            key="max_benchmark_size",
            sample_size=sample_size,
        )
        result = run_benchmark(
            rng.spawn(1)[0],
            metrics,
            sample_size=sample_size,
            repeat=repeat,
            number=number,
        )
        results[f"{sample_name} sample ({sample_size})"] = result
    dicts = proportion_tests.utils.pivot_dicts(results, "test")
    keys = ("test", *results.keys())
    report = (
        "# Benchmark",
        "Execution time, ms",
        proportion_tests.utils.render_dicts(dicts, keys),
    )
    with open(output, "w") as f:
        f.write("\n\n".join(report) + "\n")


def run_benchmark(
    rng: int | np.random.Generator,
    metrics: dict[str, tea_tasting.metrics.MetricBase],
    *,
    sample_size: int,
    repeat: int,
    number: int,
) -> dict[str, float]:
    rng = np.random.default_rng(rng)
    data = proportion_tests.data.make_data(rng.spawn(1)[0], sample_size=sample_size)
    result = {}
    for name, metric in metrics.items():
        tqdm.tqdm.write(f"  metric: {name}")
        t = timeit.repeat(
            "metric.analyze(data, 0, 1)",
            repeat=repeat,
            number=number,
            globals={"metric": metric, "data": data},
        )
        result[name] = min(t) * 1000 / number
    return result
