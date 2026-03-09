from __future__ import annotations

from typing import TYPE_CHECKING

import tea_tasting.utils


if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any, Literal


def filter_metrics(
    tests: list[dict[str, Any]],
    key: Literal["max_simulation_size", "max_benchmark_size"],
    sample_size: int,
) -> dict[str, tea_tasting.metrics.MetricBase]:
    metrics = {}
    for test in tests:
        if test[key] >= sample_size:
            metrics[test["name"]] = test["metric"]
    return metrics


def pivot_dicts(
    data: dict[str, dict[str, Any]],
    text_key: str,
) -> list[dict[str, Any]]:
    dicts = []
    index = {}
    for val_key, val_data in data.items():
        for key, val in val_data.items():
            if key in index:
                row = index[key]
            else:
                row = {text_key: key}
                index[key] = row
                dicts.append(row)
            row[val_key] = val
    return dicts


def render_dict(
    dict_: dict[str, Any],
    keys: tuple[str, str] = ("parameter", "value"),
    text_keys: Sequence[str] | None = None,
) -> str:
    return render_dicts(
        tuple({keys[0]: par, keys[1]: str(val)} for par, val in dict_.items()),
        keys,
        text_keys,
    )


def render_dicts(
    dicts: Sequence[dict[str, Any]],
    keys: Sequence[str] | None = None,
    text_keys: Sequence[str] | None = None,
) -> str:
    if keys is None:
        keys = tuple(dicts[0].keys())
    if text_keys is None:
        text_keys = (keys[0],)
    return PrettyDicts(dicts, keys, text_keys).to_markdown()


class PrettyDicts(tea_tasting.utils.DictsReprMixin):
    def __init__(
        self,
        dicts: Sequence[dict[str, Any]],
        keys: Sequence[str],
        text_keys: Sequence[str],
    ) -> None:
        self.default_keys = keys
        self.default_text_keys = text_keys
        self.dicts = dicts

    def to_dicts(self) -> Sequence[dict[str, Any]]:
        return self.dicts
