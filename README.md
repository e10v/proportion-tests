# Comparison of two-sample proportion tests

## Problem

There are many statistical tests that can be used for the analysis of proportions in a two-sample experiment (aka A/B test):

- Exact: [Barnard's](https://en.wikipedia.org/wiki/Barnard%27s_test), [Boschloo's](https://en.wikipedia.org/wiki/Boschloo%27s_test), [Fisher's](https://en.wikipedia.org/wiki/Fisher%27s_exact_test).
- Asymptotic: [G-test](https://en.wikipedia.org/wiki/G-test), [Pearson's chi-squared](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test), [proportion Z-test](https://en.wikipedia.org/wiki/Two-proportion_Z-test).

Besides, analysis of proportions can be considered as analysis of means, if outcomes are represented as values 1 or 0. In this case, two-sample [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test) and [Z-test](https://en.wikipedia.org/wiki/Z-test) of means can be used for the analysis of proportions as well.

We are interested in choosing a test with the highest [statistical power](https://en.wikipedia.org/wiki/Power_(statistics)) while keeping the [type I error](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) rate at a desired level (for example, `0.05`).

Factors to take into account:

- Sample parameters: sample size, treatment to control allocation ratio, expected proportion value.
- Test parameters (depending on the test): [continuity correction](https://en.wikipedia.org/wiki/Continuity_correction), [pooled](https://en.wikipedia.org/wiki/Pooled_variance) or unpooled variance.
- Computational complexity: Barnard's and especially Boschloo's exact tests are computationally expensive when applied with a large sample.

## Statistical tests

The code (`stat_tests.py`) in this repository simulates multiple experiments, estimates both type I error rate and statistical power, and saves the results.

The simulations are performed for each combination of factors:

- Number of observations: small (`100`) and large (`1000`).
- Treatment to control allocation ratio: balanced (1:1 treatment to control) and imbalanced (1:4 treatment to control).
- Proportion value: balanced (`0.5`) and imbalanced (`0.1`).

Two types of simulations are performed for each combination of parameters:

- AA tests: without true difference between the proportions of two groups.
- Power tests: with true difference between the proportions of two groups.

Type I error rate and statistical power are estimated using the [significance](https://en.wikipedia.org/wiki/Statistical_significance) level equal to `0.05`. Effect size for the power tests is estimated using the target power equal to `0.8`.

The results are saved in a file (`stat_tests.md`).

Exact tests in simulations:

| metric           | test       | variance |
|:-----------------|:-----------|:---------|
| barnard          | Barnard's  | pooled   |
| barnard unpooled | Barnard's  | unpooled |
| boschloo         | Boschloo's | -        |
| fisher           | Fisher's   | -        |

Barnard's exact tests uses the Wald statistic. Boschloo's exact test is also known as Barnard's exact test with p-value of Fisher's exact test as a statistic. Both Barnard's and Boschloo's tests are computationally expensive and tested only with small samples.

Asymptotic tests in simulations:

| metric               | test                  | variance | continuity correction |
|:---------------------|:----------------------|:---------|:----------------------|
| log-likelihood       | G-test                | -        | no                    |
| log-likelihood cc    | G-test                | -        | yes                   |
| pearson              | Pearson's chi-squared | -        | no                    |
| pearson cc           | Pearson's chi-squared | -        | yes                   |
| norm                 | Proportion Z-test     | pooled   | no                    |
| norm unpooled        | Proportion Z-test     | unpooled | no                    |
| norm cc              | Proportion Z-test     | pooled   | yes                   |
| norm unpooled cc     | Proportion Z-test     | unpooled | yes                   |
| mean z-test          | Z-test of means       | pooled   | no                    |
| mean z-test unpooled | Z-test of means       | unpooled | no                    |
| mean t-test          | Student's t-test      | pooled   | no                    |
| mean t-test unpooled | Student's t-test      | unpooled | no                    |

## How to reproduce the results

[Install uv](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) (if not already installed).

Clone the repository and change the directory:

```bash
git clone git@github.com:e10v/proportion_tests.git && cd proportion_tests
```

Install dependencies:

```bash
uv sync --frozen
```

Run the statistical tests:

```bash
uv run stat_tests.py
```

Optionally, you can change parameters in the configuration file (`stat_tests.toml`).

## Discussion of the results

TODO
