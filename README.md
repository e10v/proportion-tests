# Comparison of two-sample proportion tests

## Problem

There are many statistical tests that can be used for the analysis of proportions in a two-sample experiment (aka A/B test):

- Exact: [Barnard's](https://en.wikipedia.org/wiki/Barnard%27s_test), [Boschloo's](https://en.wikipedia.org/wiki/Boschloo%27s_test), [Fisher's](https://en.wikipedia.org/wiki/Fisher%27s_exact_test).
- Asymptotic: [G-test](https://en.wikipedia.org/wiki/G-test), [Pearson's chi-squared](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test), [proportion Z-test](https://en.wikipedia.org/wiki/Two-proportion_Z-test).

Besides, analysis of proportions can be considered as analysis of means, if outcomes are represented as values 1 or 0. In this case, two-sample [Student's t-test](https://en.wikipedia.org/wiki/Student%27s_t-test) and [Z-test](https://en.wikipedia.org/wiki/Z-test) of means can be used for the analysis of proportions as well.

We are interested in choosing a test with the highest statistical power while keeping the type I error rate at a desired level (for example, 0.05).

Factors to take into account:

- Sample parameters: sample size, treatment to control sample size ratio, expected proportion value.
- Test parameters (depending on the test): [continuity correction](https://en.wikipedia.org/wiki/Continuity_correction), [pooled](https://en.wikipedia.org/wiki/Pooled_variance) or unpooled variance.
- Computational complexity: Barnard's and especially Boschloo's exact tests are computationally expensive when applied with a large sample.

## Simulations

The code in this repository simulates multiple experiments, estimates both type I error rate and statistical power, and saves the results.

The simulations are performed for each combination of factors:

- Number of observations: small (100) and large (1000).
- Treatment to control ratio of the number of observations: balanced (1:1 treatment to control) and unbalanced (1:4 treatment to control).
- Proportion value: balanced (0.5) and unbalanced (0.1).

Two types of simulations are performed for each combination of parameters:

- AA tests: without true difference between the proportions of two groups.
- Power tests: with true difference between the proportions of two groups.

The results are saved in a file named "results.md".

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

Run the simulations:

```bash
uv run main.py
```

Optionally, you can change parameters in the configuration file (config.toml).

## Discussion of the results

TODO
