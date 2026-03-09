from __future__ import annotations

import timeit
from typing import TYPE_CHECKING

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
        sample=config["sample"],
        tests=config["tests"],
        **config["benchmark"],
    )


def generate_benchmark_report(
    rng: int,
    sample: dict[str, int],
    tests: list[dict[str, Any]],
    repeat: int,
    number: int,
    output: str,
) -> None:
    results = {}
    for sample_key, sample_size in sample.items():
        tqdm.tqdm.write(f"{sample_key} sample: {sample_size}")
        data = proportion_tests.data.make_data(rng, sample_size=sample_size)
        metrics = proportion_tests.utils.filter_metrics(
            tests,
            key="max_benchmark_size",
            sample_size=sample_size,
        )
        result = run_benchmark(data, metrics, repeat=repeat, number=number)
        results[f"{sample_key} sample ({sample_size})"] = result
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
    data: dict[int, tea_tasting.aggr.Aggregates],
    metrics: dict[str, tea_tasting.metrics.MetricBase],
    *,
    repeat: int,
    number: int,
) -> dict[str, float]:
    result = {}
    for name, metric in metrics.items():
        tqdm.tqdm.write(f"    metric: {name}")
        t = timeit.repeat(
            "metric.analyze(data, 0, 1)",
            repeat=repeat,
            number=number,
            globals={"metric": metric, "data": data},
        )
        result[name] = min(t) * 1000 / number
    return result
