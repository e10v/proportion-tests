from __future__ import annotations

from typing import TYPE_CHECKING

import tea_tasting.utils


if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any

    import polars as pl


def render_results(
    results: pl.DataFrame,
    text_keys: Sequence[str] = ("test",),
) -> str:
    return render_dicts(results.to_dicts(), text_keys)


def render_params(params: dict[str, Any]) -> str:
    return render_dicts(
        tuple({"parameter": par, "value": str(val)} for par, val in params.items()),
        ("parameter",),
    )


def render_dicts(dicts: Sequence[dict[str, Any]], text_keys: Sequence[str]) -> str:
    return PrettyDicts(dicts, text_keys).to_markdown()


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
