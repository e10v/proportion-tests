# Comparison of two-sample proportion tests

## Small sample

### Balanced ratio, balanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.058        | [0.054, 0.063]  |
| mean z-test unpooled | 0.057        | [0.053, 0.062]  |
| mean z-test          | 0.057        | [0.052, 0.061]  |
| log-likelihood       | 0.055        | [0.051, 0.060]  |
| norm                 | 0.055        | [0.051, 0.060]  |
| pearson              | 0.055        | [0.051, 0.060]  |
| mean t-test          | 0.054        | [0.050, 0.059]  |
| mean t-test unpooled | 0.054        | [0.050, 0.059]  |
| barnard              | 0.049        | [0.045, 0.054]  |
| boschloo             | 0.049        | [0.045, 0.053]  |
| barnard unpooled     | 0.047        | [0.043, 0.052]  |
| fisher               | 0.045        | [0.042, 0.050]  |
| norm unpooled cc     | 0.038        | [0.034, 0.042]  |
| log-likelihood cc    | 0.035        | [0.032, 0.039]  |
| norm cc              | 0.035        | [0.031, 0.039]  |
| pearson cc           | 0.035        | [0.031, 0.039]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0.269 |
| relative effect size                  | 0.54  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.814 | [0.807, 0.822] |
| mean z-test          | 0.809 | [0.802, 0.817] |
| mean z-test unpooled | 0.809 | [0.801, 0.817] |
| log-likelihood       | 0.807 | [0.800, 0.815] |
| norm                 | 0.807 | [0.799, 0.815] |
| pearson              | 0.807 | [0.799, 0.815] |
| mean t-test          | 0.805 | [0.797, 0.812] |
| mean t-test unpooled | 0.803 | [0.795, 0.811] |
| barnard              | 0.797 | [0.789, 0.805] |
| boschloo             | 0.793 | [0.785, 0.801] |
| barnard unpooled     | 0.790 | [0.782, 0.798] |
| fisher               | 0.770 | [0.761, 0.778] |
| norm unpooled cc     | 0.755 | [0.746, 0.763] |
| log-likelihood cc    | 0.747 | [0.738, 0.755] |
| norm cc              | 0.743 | [0.734, 0.751] |
| pearson cc           | 0.743 | [0.734, 0.751] |

### Balanced ratio, imbalanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| log-likelihood       | 0.059        | [0.055, 0.064]  |
| norm unpooled        | 0.055        | [0.051, 0.060]  |
| mean z-test unpooled | 0.053        | [0.049, 0.058]  |
| mean z-test          | 0.052        | [0.047, 0.056]  |
| mean t-test unpooled | 0.050        | [0.046, 0.054]  |
| norm                 | 0.050        | [0.045, 0.054]  |
| pearson              | 0.050        | [0.045, 0.054]  |
| mean t-test          | 0.048        | [0.044, 0.053]  |
| barnard              | 0.046        | [0.042, 0.050]  |
| barnard unpooled     | 0.045        | [0.041, 0.049]  |
| boschloo             | 0.035        | [0.031, 0.038]  |
| fisher               | 0.032        | [0.028, 0.035]  |
| norm unpooled cc     | 0.024        | [0.021, 0.027]  |
| log-likelihood cc    | 0.024        | [0.021, 0.027]  |
| norm cc              | 0.019        | [0.016, 0.022]  |
| pearson cc           | 0.019        | [0.016, 0.022]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0.228 |
| relative effect size                  | 2.28  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.828 | [0.821, 0.836] |
| log-likelihood       | 0.824 | [0.816, 0.831] |
| mean z-test          | 0.823 | [0.815, 0.831] |
| mean z-test unpooled | 0.821 | [0.813, 0.828] |
| norm                 | 0.820 | [0.812, 0.827] |
| pearson              | 0.820 | [0.812, 0.827] |
| mean t-test          | 0.818 | [0.810, 0.825] |
| mean t-test unpooled | 0.815 | [0.807, 0.822] |
| barnard              | 0.808 | [0.800, 0.815] |
| barnard unpooled     | 0.802 | [0.794, 0.810] |
| boschloo             | 0.796 | [0.788, 0.804] |
| fisher               | 0.777 | [0.769, 0.785] |
| norm unpooled cc     | 0.756 | [0.748, 0.765] |
| log-likelihood cc    | 0.752 | [0.743, 0.761] |
| norm cc              | 0.743 | [0.734, 0.751] |
| pearson cc           | 0.743 | [0.734, 0.751] |

### Imbalanced ratio, balanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.062        | [0.057, 0.067]  |
| mean z-test unpooled | 0.058        | [0.054, 0.063]  |
| log-likelihood       | 0.048        | [0.044, 0.053]  |
| mean z-test          | 0.048        | [0.044, 0.052]  |
| norm                 | 0.047        | [0.043, 0.051]  |
| pearson              | 0.047        | [0.043, 0.051]  |
| mean t-test unpooled | 0.046        | [0.042, 0.051]  |
| mean t-test          | 0.046        | [0.042, 0.050]  |
| boschloo             | 0.042        | [0.038, 0.046]  |
| norm unpooled cc     | 0.033        | [0.030, 0.037]  |
| barnard              | 0.033        | [0.030, 0.037]  |
| fisher               | 0.031        | [0.027, 0.034]  |
| log-likelihood cc    | 0.025        | [0.022, 0.028]  |
| norm cc              | 0.023        | [0.020, 0.026]  |
| pearson cc           | 0.023        | [0.020, 0.026]  |
| barnard unpooled     | 0.006        | [0.005, 0.008]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0.347 |
| relative effect size                  | 0.69  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.893 | [0.887, 0.899] |
| mean z-test unpooled | 0.888 | [0.882, 0.894] |
| mean t-test unpooled | 0.870 | [0.864, 0.877] |
| log-likelihood       | 0.860 | [0.852, 0.866] |
| mean z-test          | 0.853 | [0.846, 0.860] |
| norm                 | 0.849 | [0.842, 0.856] |
| pearson              | 0.849 | [0.842, 0.856] |
| mean t-test          | 0.847 | [0.840, 0.854] |
| boschloo             | 0.846 | [0.839, 0.853] |
| norm unpooled cc     | 0.840 | [0.833, 0.847] |
| fisher               | 0.809 | [0.801, 0.816] |
| barnard              | 0.788 | [0.780, 0.796] |
| log-likelihood cc    | 0.782 | [0.774, 0.791] |
| norm cc              | 0.766 | [0.758, 0.774] |
| pearson cc           | 0.766 | [0.758, 0.774] |
| barnard unpooled     | 0.624 | [0.615, 0.634] |

### Imbalanced ratio, imbalanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.153        | [0.146, 0.160]  |
| mean z-test unpooled | 0.151        | [0.144, 0.158]  |
| mean t-test unpooled | 0.147        | [0.140, 0.154]  |
| log-likelihood       | 0.073        | [0.068, 0.078]  |
| norm unpooled cc     | 0.072        | [0.067, 0.077]  |
| mean z-test          | 0.040        | [0.036, 0.044]  |
| norm                 | 0.039        | [0.035, 0.043]  |
| pearson              | 0.039        | [0.035, 0.043]  |
| mean t-test          | 0.038        | [0.034, 0.042]  |
| barnard unpooled     | 0.034        | [0.031, 0.038]  |
| barnard              | 0.031        | [0.028, 0.035]  |
| fisher               | 0.025        | [0.022, 0.028]  |
| boschloo             | 0.023        | [0.020, 0.026]  |
| norm cc              | 0.015        | [0.013, 0.018]  |
| pearson cc           | 0.015        | [0.013, 0.018]  |
| log-likelihood cc    | 0.013        | [0.011, 0.016]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0.249 |
| relative effect size                  | 2.49  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| mean z-test          | 0.753 | [0.744, 0.761] |
| mean t-test          | 0.749 | [0.740, 0.757] |
| norm                 | 0.749 | [0.740, 0.757] |
| pearson              | 0.749 | [0.740, 0.757] |
| barnard              | 0.707 | [0.698, 0.716] |
| log-likelihood       | 0.707 | [0.698, 0.716] |
| fisher               | 0.701 | [0.692, 0.710] |
| boschloo             | 0.691 | [0.682, 0.700] |
| norm cc              | 0.649 | [0.640, 0.659] |
| pearson cc           | 0.649 | [0.640, 0.659] |
| norm unpooled        | 0.606 | [0.596, 0.616] |
| log-likelihood cc    | 0.598 | [0.589, 0.608] |
| mean z-test unpooled | 0.589 | [0.579, 0.599] |
| mean t-test unpooled | 0.538 | [0.529, 0.548] |
| norm unpooled cc     | 0.485 | [0.475, 0.495] |
| barnard unpooled     | 0.196 | [0.188, 0.204] |

## Large sample

### Balanced ratio, balanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.055        | [0.051, 0.060]  |
| mean z-test          | 0.055        | [0.050, 0.059]  |
| mean z-test unpooled | 0.055        | [0.050, 0.059]  |
| log-likelihood       | 0.054        | [0.050, 0.059]  |
| mean t-test          | 0.054        | [0.049, 0.058]  |
| mean t-test unpooled | 0.054        | [0.049, 0.058]  |
| norm                 | 0.054        | [0.049, 0.058]  |
| pearson              | 0.054        | [0.049, 0.058]  |
| fisher               | 0.051        | [0.046, 0.055]  |
| norm unpooled cc     | 0.046        | [0.042, 0.051]  |
| log-likelihood cc    | 0.046        | [0.042, 0.050]  |
| norm cc              | 0.046        | [0.042, 0.050]  |
| pearson cc           | 0.046        | [0.042, 0.050]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0.088 |
| relative effect size                  | 0.18  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.801 | [0.793, 0.809] |
| mean z-test unpooled | 0.801 | [0.793, 0.808] |
| mean z-test          | 0.801 | [0.793, 0.808] |
| log-likelihood       | 0.800 | [0.792, 0.808] |
| mean t-test          | 0.800 | [0.792, 0.808] |
| norm                 | 0.800 | [0.792, 0.808] |
| pearson              | 0.800 | [0.792, 0.808] |
| mean t-test unpooled | 0.800 | [0.792, 0.808] |
| fisher               | 0.796 | [0.788, 0.804] |
| norm unpooled cc     | 0.782 | [0.773, 0.790] |
| log-likelihood cc    | 0.780 | [0.772, 0.788] |
| norm cc              | 0.780 | [0.772, 0.788] |
| pearson cc           | 0.780 | [0.772, 0.788] |

### Balanced ratio, imbalanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| log-likelihood       | 0.052        | [0.048, 0.057]  |
| mean z-test          | 0.052        | [0.048, 0.057]  |
| norm unpooled        | 0.052        | [0.048, 0.057]  |
| mean z-test unpooled | 0.052        | [0.048, 0.057]  |
| mean t-test          | 0.052        | [0.048, 0.056]  |
| norm                 | 0.052        | [0.048, 0.056]  |
| pearson              | 0.052        | [0.048, 0.056]  |
| mean t-test unpooled | 0.052        | [0.047, 0.056]  |
| fisher               | 0.045        | [0.041, 0.049]  |
| log-likelihood cc    | 0.039        | [0.036, 0.043]  |
| norm unpooled cc     | 0.039        | [0.036, 0.043]  |
| norm cc              | 0.039        | [0.035, 0.043]  |
| pearson cc           | 0.039        | [0.035, 0.043]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0.059 |
| relative effect size                  | 0.59  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| log-likelihood       | 0.797 | [0.789, 0.805] |
| mean z-test          | 0.797 | [0.789, 0.805] |
| norm                 | 0.797 | [0.789, 0.805] |
| norm unpooled        | 0.797 | [0.789, 0.805] |
| pearson              | 0.797 | [0.789, 0.805] |
| mean t-test          | 0.797 | [0.789, 0.804] |
| mean z-test unpooled | 0.796 | [0.788, 0.804] |
| mean t-test unpooled | 0.796 | [0.788, 0.804] |
| fisher               | 0.782 | [0.774, 0.790] |
| norm unpooled cc     | 0.770 | [0.762, 0.778] |
| log-likelihood cc    | 0.770 | [0.762, 0.778] |
| norm cc              | 0.769 | [0.761, 0.778] |
| pearson cc           | 0.769 | [0.761, 0.778] |

### Imbalanced ratio, balanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.048        | [0.043, 0.052]  |
| mean z-test unpooled | 0.047        | [0.043, 0.051]  |
| log-likelihood       | 0.046        | [0.042, 0.051]  |
| mean z-test          | 0.046        | [0.042, 0.051]  |
| mean t-test          | 0.046        | [0.042, 0.050]  |
| mean t-test unpooled | 0.046        | [0.042, 0.050]  |
| norm                 | 0.046        | [0.042, 0.050]  |
| pearson              | 0.046        | [0.042, 0.050]  |
| fisher               | 0.042        | [0.038, 0.046]  |
| norm unpooled cc     | 0.039        | [0.035, 0.043]  |
| log-likelihood cc    | 0.038        | [0.034, 0.042]  |
| norm cc              | 0.037        | [0.034, 0.041]  |
| pearson cc           | 0.037        | [0.034, 0.041]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0.111 |
| relative effect size                  | 0.22  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.808 | [0.801, 0.816] |
| mean z-test unpooled | 0.807 | [0.799, 0.815] |
| mean t-test unpooled | 0.805 | [0.797, 0.812] |
| log-likelihood       | 0.803 | [0.795, 0.811] |
| mean z-test          | 0.802 | [0.794, 0.810] |
| norm                 | 0.802 | [0.794, 0.809] |
| pearson              | 0.802 | [0.794, 0.809] |
| mean t-test          | 0.802 | [0.794, 0.809] |
| fisher               | 0.789 | [0.781, 0.797] |
| norm unpooled cc     | 0.785 | [0.777, 0.793] |
| log-likelihood cc    | 0.780 | [0.772, 0.788] |
| norm cc              | 0.778 | [0.770, 0.786] |
| pearson cc           | 0.778 | [0.770, 0.786] |

### Imbalanced ratio, imbalanced proportion

AA tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.058        | [0.054, 0.063]  |
| mean z-test unpooled | 0.058        | [0.053, 0.062]  |
| mean t-test unpooled | 0.057        | [0.053, 0.062]  |
| log-likelihood       | 0.054        | [0.050, 0.059]  |
| mean z-test          | 0.053        | [0.049, 0.058]  |
| mean t-test          | 0.053        | [0.049, 0.058]  |
| norm                 | 0.053        | [0.049, 0.058]  |
| pearson              | 0.053        | [0.049, 0.058]  |
| fisher               | 0.045        | [0.042, 0.050]  |
| norm unpooled cc     | 0.044        | [0.040, 0.048]  |
| log-likelihood cc    | 0.040        | [0.036, 0.044]  |
| norm cc              | 0.038        | [0.035, 0.043]  |
| pearson cc           | 0.038        | [0.035, 0.043]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of simulations                 | 10000 |
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0.07  |
| relative effect size                  | 0.7   |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| mean z-test          | 0.770 | [0.762, 0.778] |
| norm                 | 0.769 | [0.761, 0.778] |
| pearson              | 0.769 | [0.761, 0.778] |
| mean t-test          | 0.769 | [0.760, 0.777] |
| log-likelihood       | 0.752 | [0.743, 0.760] |
| fisher               | 0.746 | [0.738, 0.755] |
| norm cc              | 0.731 | [0.722, 0.740] |
| pearson cc           | 0.731 | [0.722, 0.740] |
| log-likelihood cc    | 0.710 | [0.700, 0.718] |
| norm unpooled        | 0.699 | [0.689, 0.707] |
| mean z-test unpooled | 0.696 | [0.687, 0.705] |
| mean t-test unpooled | 0.693 | [0.684, 0.702] |
| norm unpooled cc     | 0.657 | [0.647, 0.666] |
