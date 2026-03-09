from __future__ import annotations

import argparse
import importlib
import tomllib
from typing import TYPE_CHECKING

import tea_tasting.utils


if TYPE_CHECKING:
    from typing import Any

    import tea_tasting.metrics  # noqa: TC004


def load_config() -> dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="proportion-tests.toml",
        help="Config file",
        required=False,
    )
    with open(parser.parse_args().config, "rb") as f:
        config = tomllib.load(f)

    tea_tasting.utils.check_scalar(config["rng"], "rng", typ=int)

    samples = config["samples"]
    tea_tasting.utils.check_scalar(samples, "samples", typ=dict)
    for key, val in samples.items():
        tea_tasting.utils.check_scalar(val, f"samples.{key}", typ=int, ge=10)

    benchmark = config["benchmark"]
    tea_tasting.utils.check_scalar(benchmark, "benchmark", typ=dict)
    tea_tasting.utils.check_scalar(
        benchmark["repeat"], "benchmark.repeat", typ=int, gt=0)
    tea_tasting.utils.check_scalar(
        benchmark["number"], "benchmark.number", typ=int, gt=0)
    tea_tasting.utils.check_scalar(benchmark["output"], "benchmark.output", typ=str)

    simulation = config["simulation"]
    tea_tasting.utils.check_scalar(simulation, "simulation", typ=dict)
    tea_tasting.utils.check_scalar(
        simulation["n_simulations"], "simulation.n_simulations", typ=int, gt=0)
    tea_tasting.utils.check_scalar(
        simulation["alpha"], "simulation.alpha", typ=float, gt=0, lt=1)
    tea_tasting.utils.check_scalar(
        simulation["power"], "simulation.power", typ=float, gt=0, lt=1)
    tea_tasting.utils.check_scalar(simulation["output"], "simulation.output", typ=str)

    options = simulation["options"]
    tea_tasting.utils.check_scalar(options, "simulation.options", typ=list)
    for i, option in enumerate(options):
        tea_tasting.utils.check_scalar(option, f"simulation.options[{i}]", typ=dict)
        tea_tasting.utils.check_scalar(
            option["name"], f"simulation.options[{i}].name", typ=str)
        tea_tasting.utils.check_scalar(
            option["ratio"], f"simulation.options[{i}].ratio", typ=float | int, gt=0)
        tea_tasting.utils.check_scalar(
            option["prop"], f"simulation.options[{i}].prop", typ=float, gt=0, le=0.5)

    tests = config["tests"]
    tea_tasting.utils.check_scalar(tests, "tests", typ=list)
    for i, test in enumerate(tests):
        tea_tasting.utils.check_scalar(test, f"tests[{i}]", typ=dict)
        tea_tasting.utils.check_scalar(test["name"], f"tests[{i}].name", typ=str)
        tea_tasting.utils.check_scalar(test["path"], f"tests[{i}].path", typ=str)
        tea_tasting.utils.check_scalar(test["kwargs"], f"tests[{i}].kwargs", typ=dict)
        tea_tasting.utils.check_scalar(
            test["max_simulation_size"],
            f"tests[{i}].max_simulation_size",
            typ=int | float,
            ge=0,
        )
        tea_tasting.utils.check_scalar(
            test["max_benchmark_size"],
            f"tests[{i}].max_benchmark_size",
            typ=int | float,
            ge=0,
        )
        test["metric"] = init_metric(test["path"], **test["kwargs"])

    return config


def init_metric(path: str, **kwargs: dict[str, Any]) -> tea_tasting.metrics.MetricBase:
    mod_name, attr_name = path.rsplit(".", 1)
    module = importlib.import_module(mod_name)
    metric = getattr(module, attr_name)
    return metric("value", **kwargs)
