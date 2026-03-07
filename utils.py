from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import tea_tasting.aggr
import tea_tasting.utils


if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any

    import polars as pl


def make_data(
    rng: int | np.random.Generator,
    *,
    n_obs: int,
    ratio: float = 1,
    prop: float = 0.5,
    effect_size: float = 0,
) -> dict[object, tea_tasting.aggr.Aggregates]:
    rng = np.random.default_rng(rng)
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


def write_results(
    output: str,
    results: pl.DataFrame,
    text_keys: Sequence[str] = ("metric",),
) -> None:
    write_dicts(output, results.to_dicts(), text_keys)


def write_params(output: str, params: dict[str, Any]) -> None:
    write_dicts(
        output,
        tuple({"parameter": par, "value": str(val)} for par, val in params.items()),
        ("parameter",),
    )


def write_dicts(
    output: str,
    dicts: Sequence[dict[str, Any]],
    text_keys: Sequence[str],
) -> None:
    write_text(output, PrettyDicts(dicts, text_keys).to_markdown())


class PrettyDicts(tea_tasting.utils.DictsReprMixin):
    def __init__(
        self,
        dicts: Sequence[dict[str, Any]],
        text_keys: Sequence[str],
    ) -> None:
        self.default_keys = tuple(dicts[0].keys())
        self.default_text_keys = text_keys
        self.dicts = dicts

    def to_dicts(self) -> Sequence[dict[str, Any]]:
        return self.dicts
