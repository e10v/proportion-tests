from __future__ import annotations

import importlib
import tomllib
from typing import TYPE_CHECKING

import tea_tasting.metrics
import tea_tasting.utils


if TYPE_CHECKING:
    from typing import Any


def load_config() -> dict[str, Any]:
    with open("pyproject.toml", "rb") as f:
        pyproject = tomllib.load(f)

    config = pyproject["tool"]["proportion_tests"]
    tea_tasting.utils.check_scalar(config["rng"], "tool.proportion_tests.rng", typ=int)

    sample = config["sample"]
    tea_tasting.utils.check_scalar(sample, "tool.proportion_tests.sample", typ=dict)
    for key, val in sample.items():
        tea_tasting.utils.check_scalar(
            val, f"tool.proportion_tests.sample.{key}", typ=int, gt=0)

    benchmark = config["benchmark"]
    tea_tasting.utils.check_scalar(
        benchmark, "tool.proportion_tests.benchmark", typ=dict)
    tea_tasting.utils.check_scalar(
        benchmark["repeat"],
        "tool.proportion_tests.benchmark.repeat",
        typ=int,
        gt=0,
    )
    tea_tasting.utils.check_scalar(
        benchmark["number"],
        "tool.proportion_tests.benchmark.number",
        typ=int,
        gt=0,
    )
    tea_tasting.utils.check_scalar(
        benchmark["output"],
        "tool.proportion_tests.benchmark.output",
        typ=str,
    )

    simulation = config["simulation"]
    tea_tasting.utils.check_scalar(
        simulation, "tool.proportion_tests.simulation", typ=dict)
    tea_tasting.utils.check_scalar(
        simulation["n_simulations"],
        "tool.proportion_tests.simulation.n_simulations",
        typ=int,
        gt=0,
    )
    tea_tasting.utils.check_scalar(
        simulation["alpha"],
        "tool.proportion_tests.simulation.alpha",
        typ=float,
        gt=0,
        lt=1,
    )
    tea_tasting.utils.check_scalar(
        simulation["power"],
        "tool.proportion_tests.simulation.power",
        typ=float,
        gt=0,
        lt=1,
    )
    tea_tasting.utils.check_scalar(
        simulation["output"],
        "tool.proportion_tests.simulation.output",
        typ=str,
    )

    options = simulation["options"]
    tea_tasting.utils.check_scalar(
        options, "tool.proportion_tests.simulation.options", typ=list)
    for i, option in enumerate(options):
        tea_tasting.utils.check_scalar(
            option, f"tool.proportion_tests.simulation.options[{i}]", typ=dict)
        tea_tasting.utils.check_scalar(
            option["name"],
            f"tool.proportion_tests.simulation.options[{i}].name",
            typ=str,
        )
        tea_tasting.utils.check_scalar(
            option["ratio"],
            f"tool.proportion_tests.simulation.options[{i}].ratio",
            typ=float | int,
            gt=0,
        )
        tea_tasting.utils.check_scalar(
            option["prop"],
            f"tool.proportion_tests.simulation.options[{i}].prop",
            typ=float,
            gt=0,
            lt=1,
        )

    tests = config["tests"]
    tea_tasting.utils.check_scalar(tests, "tool.proportion_tests.metrics", typ=list)
    for i, test in enumerate(tests):
        tea_tasting.utils.check_scalar(
            test, f"tool.proportion_tests.tests{i}]", typ=dict)
        tea_tasting.utils.check_scalar(
            test["name"], f"tool.proportion_tests.tests{i}].name", typ=str)
        tea_tasting.utils.check_scalar(
            test["path"], f"tool.proportion_tests.tests{i}].path", typ=str)
        tea_tasting.utils.check_scalar(
            test["kwargs"], f"tool.proportion_tests.tests{i}].kwargs", typ=dict)
        tea_tasting.utils.check_scalar(
            test["max_simulation_size"],
            f"tool.proportion_tests.tests{i}].max_simulation_size",
            typ=int | float,
            ge=0,
        )
        tea_tasting.utils.check_scalar(
            test["max_benchmark_size"],
            f"tool.proportion_tests.tests{i}].max_benchmark_size",
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
