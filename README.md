# Comparison of two-sample proportion tests

## TL;DR

Recommended two-sample proportion tests:

- Conventional choice:
    - Z-test of proportions (with pooled variance, without continuity correction): for sample sizes of 100 or more (with some [additional conditions](https://en.wikipedia.org/wiki/Two-proportion_Z-test#Assumptions_and_conditions)).
    - Barnard's exact test (with pooled variance): in other cases.
- Unconventional choice: Student's t-test for three reasons:
    - Student's t-distribution makes it robust even with smaller samples.
    - For sample sizes above 100, it is about as powerful as the Z-test of proportions and Pearson's chi-squared test.
    - Its power can be further improved using [CUPED](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf).

## Problem

There are many statistical tests that can be used for the analysis of proportions in a two-sample experiment (aka A/B test):

- Exact: [Barnard's](https://en.wikipedia.org/wiki/Barnard%27s_test), [Boschloo's](https://en.wikipedia.org/wiki/Boschloo%27s_test), [Fisher's](https://en.wikipedia.org/wiki/Fisher%27s_exact_test).
- Asymptotic: [G-test](https://en.wikipedia.org/wiki/G-test), [Pearson's chi-squared](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test), [proportion z-test](https://en.wikipedia.org/wiki/Two-proportion_Z-test).

Besides, analysis of proportions can be considered as analysis of means, if outcomes are represented as values 1 or 0. In this case, two-sample [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test), [Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test), and [z-test](https://en.wikipedia.org/wiki/Z-test) of means can be used for the analysis of proportions as well.

We are interested in choosing a test with the highest [statistical power](https://en.wikipedia.org/wiki/Power_(statistics)) while keeping the [type I error](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) rate at a desired level (for example, `0.05`).

Factors to take into account:

- Sample parameters: sample size, treatment to control allocation ratio, expected proportion value.
- Test parameters (depending on the test): [continuity correction](https://en.wikipedia.org/wiki/Continuity_correction), [pooled](https://en.wikipedia.org/wiki/Pooled_variance) or unpooled variance.
- Computational complexity: Barnard's and especially Boschloo's exact tests are computationally expensive when applied with a large sample.

## Simulation

The code in this repository simulates multiple experiments, estimates both type I error rate and statistical power, and saves the results.

The simulations are performed for each combination of factors:

- Sample size: small (`100`), medium (`1000`) and large (`10_000`).
- Treatment to control allocation ratio: balanced (1:1 treatment to control) and imbalanced (1:4 treatment to control).
- Proportion value: balanced (`0.5`) and imbalanced (`0.1`).

Two types of simulations are performed for each combination of parameters:

- A/A simulation: without true difference between the proportions of two groups.
- Power simulation: with true difference between the proportions of two groups.

Type I error rate and statistical power are estimated using the [significance](https://en.wikipedia.org/wiki/Statistical_significance) level equal to `0.05`. Effect size for the power tests is estimated using the target power equal to `0.8`.

The results are saved in a file [`reports/simulation.md`](reports/simulation.md).

Exact tests in simulations:

| test               | variance |
| :----------------- | :------- |
| Barnard            | pooled   |
| Barnard (unpooled) | unpooled |
| Boschloo           | -        |
| Fisher             | -        |

Barnard's exact tests uses the Wald statistic. Boschloo's exact test is also known as Barnard's exact test with p-value of Fisher's exact test as a statistic. Both Barnard's and Boschloo's tests are computationally expensive and simulated only with small samples.

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

The code in this repository benchmarks execution time of multiple tests and saves the results.

The benchmark is performed for each sample size:

- Small: `100`.
- Medium: `1000`.
- Large: `10_000`.

For each sample size, a synthetic dataset is generated. Each test is then executed multiple times on the same data. Execution time is estimated in milliseconds per run by taking the fastest result across repeated timings and dividing it by the number of runs in each repeat. By default, the benchmark uses `10` timing repeats with `10` runs in each repeat.

The results are saved in a file [`reports/benchmark.md`](reports/benchmark.md).

Only one variant of each test is measured because there is no meaningful performance difference between a test with pooled vs. unpooled variance or with vs. without continuity correction.

The execution time of Barnard's and Boschloo's tests is estimated only for small and medium samples.

*Note: Execution time of Student's t-test, Z-test of means, and Z-test of proportions includes calculation of confidence interval.*

## How to reproduce the results

[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) (if not already installed).

Clone the repository and change the directory:

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

Across all scenarios in [`reports/simulation.md`](reports/simulation.md), the following tests have a maximum type I error rate with a confidence interval entirely above `0.05`:

| test                                 | max type I error | max type I error ci |
| :----------------------------------- | ---------------: | ------------------: |
| Z-test of proportions (unpooled)     |            0.138 |      [0.131, 0.145] |
| Z-test of means (unpooled)           |            0.136 |      [0.129, 0.143] |
| Welch's t-test                       |            0.132 |      [0.126, 0.139] |
| G-test                               |           0.0699 |    [0.0650, 0.0751] |
| Z-test of proportions (unpooled, cc) |           0.0663 |    [0.0615, 0.0714] |
| Z-test of means                      |           0.0558 |    [0.0514, 0.0605] |

All of them occur with small samples. All tests except the Z-test of means have a maximum type I error rate in the setup with an imbalanced treatment-to-control ratio and an imbalanced proportion.

Among the remaining tests, Student's t-test, Z-test of proportions, and Pearson's chi-squared test have the highest power in small samples. Student's t-test power can be further improved using [CUPED](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf).

In most small-sample settings, Barnard's exact test has the highest power among the exact tests. In every small-sample setting, at least one exact test is more powerful than Fisher's exact test.

With medium and large samples:

- Student's t-test, Z-test of means, Z-test of proportions, and Pearson's chi-squared test are among the best-performing tests across all settings, including settings with an imbalanced treatment-to-control ratio and an imbalanced proportion (within measurement accuracy).
- Continuity correction hurts the power even with large samples.
- Unpooled variance hurts power in the setting with an imbalanced treatment-to-control ratio and an imbalanced proportion.
- Fisher's exact test underperforms relative to asymptotic tests without continuity correction.

### Benchmark

For the aggregated inputs used in this benchmark, all asymptotic tests run in O(1) time with respect to sample size. The execution times for Student's t-test, the Z-test of means, and the Z-test of proportions include confidence-interval calculation, which explains why they are slower than the G-test and Pearson's chi-squared test.

Fisher is the fastest among the exact tests. In theory, it has linear time complexity, O(N). In practice, however, its execution time grows more slowly than sample size.

Execution time of Barnard's and especially Boschloo's exact tests explodes as sample size increases. They should be used only with relatively small samples.
