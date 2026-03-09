from __future__ import annotations

import numpy as np
import tea_tasting.aggr


def make_data(
    rng: int | np.random.Generator,
    *,
    sample_size: int,
    ratio: float = 1,
    prop: float = 0.5,
    effect_size: float = 0,
) -> dict[int, tea_tasting.aggr.Aggregates]:
    rng = np.random.default_rng(rng)
    n0 = np.clip(rng.binomial(n=sample_size, p=1 / (1 + ratio)), 2, sample_size - 2)
    n1 = sample_size - n0
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
