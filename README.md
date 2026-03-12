# Comparison of two-sample proportion tests

## TL;DR

Recommended two-sample proportion tests:

- Conventional choice:
    - Z-test of proportions (with pooled variance, without continuity correction): for sample sizes of 100 or more, subject to some [additional conditions](https://en.wikipedia.org/wiki/Two-proportion_Z-test#Assumptions_and_conditions).
    - Barnard's exact test (with pooled variance): in other cases.
- Unconventional choice: Student's t-test, for three reasons:
    - Using Student's t-distribution makes it robust with smaller samples.
    - For sample sizes above 100, it is about as powerful as the z-test of proportions and Pearson's chi-squared test.
    - Its power can be improved further with [CUPED](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf).

## Problem

There are many statistical tests that can be used for the analysis of proportions in a two-sample experiment (aka A/B test):

- Exact: [Barnard's](https://en.wikipedia.org/wiki/Barnard%27s_test), [Boschloo's](https://en.wikipedia.org/wiki/Boschloo%27s_test), [Fisher's](https://en.wikipedia.org/wiki/Fisher%27s_exact_test).
- Asymptotic: [G-test](https://en.wikipedia.org/wiki/G-test), [Pearson's chi-squared](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test), [proportion z-test](https://en.wikipedia.org/wiki/Two-proportion_Z-test).

In addition, proportion analysis can be framed as mean analysis by encoding outcomes as 1 and 0. In that case, two-sample [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test), [Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test), and the [z-test](https://en.wikipedia.org/wiki/Z-test) of means can also be used.

We want a test with high [statistical power](https://en.wikipedia.org/wiki/Power_(statistics)) while keeping the [type I error](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) rate at the desired level (for example, `0.05`).

Factors to consider:

- Sample parameters: sample size, treatment to control allocation ratio, expected proportion value.
- Test parameters (depending on the test): [continuity correction](https://en.wikipedia.org/wiki/Continuity_correction), [pooled](https://en.wikipedia.org/wiki/Pooled_variance) or unpooled variance.
- Computational complexity: Barnard's and especially Boschloo's exact tests are computationally expensive on large samples.

## Simulation

The code in this repository simulates many experiments, estimates both type I error rate and statistical power, and saves the results.

The simulations are run for every combination of these factors:

- Sample size: small (`100`), medium (`1000`) and large (`10_000`).
- Treatment to control allocation ratio: balanced (1:1 treatment to control) and imbalanced (1:4 treatment to control).
- Control-group proportion: balanced (`0.5`) and imbalanced (`0.1`).

Two types of simulations are run for each parameter combination:

- A/A simulation: without true difference between the proportions of two groups.
- Power simulation: with true difference between the proportions of two groups.

Type I error rate and statistical power are estimated at a [significance](https://en.wikipedia.org/wiki/Statistical_significance) level of `0.05`. For the power simulations, the effect size is chosen to target power `0.8`.

The results are saved to [`reports/simulation.md`](reports/simulation.md).

Exact tests in simulations:

| test               | variance |
| :----------------- | :------- |
| Barnard            | pooled   |
| Barnard (unpooled) | unpooled |
| Boschloo           | -        |
| Fisher             | -        |

The Barnard variants use the Wald statistic. Boschloo's exact test uses the p-value from Fisher's exact test as its statistic. Both Barnard's and Boschloo's tests are computationally expensive, so they are simulated only for small samples.

Asymptotic tests in simulations:

| test                                 | variance | continuity correction |
| :----------------------------------- | :------- | :-------------------- |
| G-test                               | -        | no                    |
| G-test (cc)                          | -        | yes                   |
| Pearson's chi-squared                | -        | no                    |
| Pearson's chi-squared (cc)           | -        | yes                   |
| Z-test of proportions                | pooled   | no                    |
| Z-test of proportions (unpooled)     | unpooled | no                    |
| Z-test of proportions (cc)           | pooled   | yes                   |
| Z-test of proportions (unpooled, cc) | unpooled | yes                   |
| Z-test of means                      | pooled   | no                    |
| Z-test of means (unpooled)           | unpooled | no                    |
| Student's t-test                     | pooled   | no                    |
| Welch's t-test                       | unpooled | no                    |

## Benchmark

The code in this repository benchmarks the execution time of multiple tests and saves the results.

The benchmark is performed for each sample size:

- Small: `100`.
- Medium: `1000`.
- Large: `10_000`.

For each sample size, a synthetic dataset is generated. Each test is then executed multiple times on the same data. Execution time is estimated in milliseconds per run by taking the fastest timing result across repeats and dividing it by the number of runs per repeat. By default, the benchmark uses `10` timing repeats with `10` runs per repeat.

The results are saved to [`reports/benchmark.md`](reports/benchmark.md).

Only one variant of each test is measured because pooled vs. unpooled variance and continuity correction do not meaningfully affect runtime.

The execution time of Barnard's and Boschloo's tests is estimated only for small and medium samples.

*Note: The execution time of Student's t-test, the z-test of means, and the z-test of proportions includes confidence interval calculation.*

## How to reproduce the results

[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) (if not already installed).

Clone the repository and change into the directory:

```bash
git clone git@github.com:e10v/proportion-tests.git && cd proportion-tests
```

Install dependencies:

```bash
uv sync --frozen
```

Run the simulation:

```bash
uv run simulation
```

Run the benchmark:

```bash
uv run benchmark
```

Optionally, you can change parameters in the configuration file [`proportion-tests.toml`](proportion-tests.toml).

## Discussion of the results

### Simulation

Across all scenarios in [`reports/simulation.md`](reports/simulation.md), the following tests have a worst case type I error rate whose confidence interval lies entirely above `0.05`:

| test                                 | max type I error | max type I error ci |
| :----------------------------------- | ---------------: | ------------------: |
| Z-test of proportions (unpooled)     |            0.138 |      [0.131, 0.145] |
| Z-test of means (unpooled)           |            0.136 |      [0.129, 0.143] |
| Welch's t-test                       |            0.132 |      [0.126, 0.139] |
| G-test                               |           0.0699 |    [0.0650, 0.0751] |
| Z-test of proportions (unpooled, cc) |           0.0663 |    [0.0615, 0.0714] |
| Z-test of means                      |           0.0558 |    [0.0514, 0.0605] |

All of these cases occur with small samples. For every test except the z-test of means, the worst case occurs in the setup with an imbalanced treatment-to-control ratio and an imbalanced proportion.

Among the remaining tests, Student's t-test, the z-test of proportions, and Pearson's chi-squared test have the highest power in small samples. Student's t-test can gain additional power with [CUPED](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf).

In most small sample settings, Barnard's exact test has the highest power among the exact tests. In every small sample setting, at least one exact test is more powerful than Fisher's exact test.

With medium and large samples:

- Student's t-test, the z-test of means, the z-test of proportions, and Pearson's chi-squared test are among the best performing tests across all settings, including settings with an imbalanced treatment-to-control ratio and an imbalanced proportion (within measurement error).
- Continuity correction hurts the power even with large samples.
- Unpooled variance hurts power in the setting with an imbalanced treatment-to-control ratio and an imbalanced proportion.
- Fisher's exact test underperforms relative to asymptotic tests without continuity correction.

### Benchmark

For the aggregated inputs used in this benchmark, all asymptotic tests run in O(1) time with respect to sample size. The execution times for Student's t-test, the z-test of means, and the z-test of proportions include confidence-interval calculation, which helps explain why they are slower than the G-test and Pearson's chi-squared test.

Fisher is the fastest exact test in this benchmark, and its measured runtime grows much more slowly than the runtimes of Barnard's and Boschloo's tests.

The execution time of Barnard's and especially Boschloo's exact tests increases sharply with sample size. In practice, they should be used only with relatively small samples.
