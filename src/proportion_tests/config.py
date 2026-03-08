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

    n_obs = config["n_obs"]
    tea_tasting.utils.check_scalar(n_obs, "tool.proportion_tests.n_obs", typ=dict)
    for key, val in n_obs.items():
        tea_tasting.utils.check_scalar(
            val, f"tool.proportion_tests.{key}", typ=int, gt=0)

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

    metrics = config["metrics"]
    tea_tasting.utils.check_scalar(metrics, "tool.proportion_tests.metrics", typ=list)
    for i, metric in enumerate(metrics):
        tea_tasting.utils.check_scalar(
            metric, f"tool.proportion_tests.metrics[{i}]", typ=dict)
        tea_tasting.utils.check_scalar(
            metric["name"], f"tool.proportion_tests.metrics[{i}].name", typ=str)
        tea_tasting.utils.check_scalar(
            metric["path"], f"tool.proportion_tests.metrics[{i}].path", typ=str)
        tea_tasting.utils.check_scalar(
            metric["kwargs"], f"tool.proportion_tests.metrics[{i}].kwargs", typ=dict)
        tea_tasting.utils.check_scalar(
            metric["max_simulation_obs"],
            f"tool.proportion_tests.metrics[{i}].max_simulation_obs",
            typ=int | float,
            ge=0,
        )
        tea_tasting.utils.check_scalar(
            metric["max_benchmark_obs"],
            f"tool.proportion_tests.metrics[{i}].max_benchmark_obs",
            typ=int | float,
            ge=0,
        )
        metric["object"] = init_metric(metric["path"], **metric["kwargs"])

    return config


def init_metric(path: str, **kwargs: dict[str, Any]) -> tea_tasting.metrics.MetricBase:
    mod_name, attr_name = path.rsplit(".", 1)
    module = importlib.import_module(mod_name)
    metric = getattr(module, attr_name)
    return metric("value", **kwargs)
