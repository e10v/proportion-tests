# Comparison of two-sample proportion tests

| parameter             | value |
|:----------------------|:------|
| number of simulations | 10000 |
| alpha                 | 0.05  |
| power                 | 0.8   |

## Small sample

### Balanced ratio, balanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.057        | [0.053, 0.062]  |
| mean z-test unpooled | 0.057        | [0.053, 0.062]  |
| mean z-test          | 0.057        | [0.052, 0.062]  |
| log-likelihood       | 0.055        | [0.051, 0.060]  |
| norm                 | 0.055        | [0.051, 0.060]  |
| pearson              | 0.055        | [0.051, 0.060]  |
| mean t-test          | 0.054        | [0.050, 0.059]  |
| mean t-test unpooled | 0.053        | [0.049, 0.058]  |
| boschloo             | 0.048        | [0.044, 0.052]  |
| barnard              | 0.048        | [0.044, 0.052]  |
| barnard unpooled     | 0.046        | [0.042, 0.050]  |
| fisher               | 0.044        | [0.040, 0.048]  |
| norm unpooled cc     | 0.036        | [0.033, 0.040]  |
| log-likelihood cc    | 0.034        | [0.030, 0.037]  |
| norm cc              | 0.033        | [0.030, 0.037]  |
| pearson cc           | 0.033        | [0.030, 0.037]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0.269 |
| relative effect size                  | 0.54  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.820 | [0.813, 0.828] |
| mean z-test unpooled | 0.815 | [0.807, 0.822] |
| mean z-test          | 0.814 | [0.806, 0.821] |
| log-likelihood       | 0.812 | [0.804, 0.820] |
| norm                 | 0.812 | [0.804, 0.819] |
| pearson              | 0.812 | [0.804, 0.819] |
| mean t-test          | 0.810 | [0.802, 0.818] |
| mean t-test unpooled | 0.808 | [0.800, 0.816] |
| barnard              | 0.803 | [0.795, 0.811] |
| boschloo             | 0.799 | [0.791, 0.807] |
| barnard unpooled     | 0.796 | [0.788, 0.803] |
| fisher               | 0.775 | [0.767, 0.784] |
| norm unpooled cc     | 0.762 | [0.754, 0.771] |
| log-likelihood cc    | 0.751 | [0.743, 0.760] |
| norm cc              | 0.748 | [0.739, 0.756] |
| pearson cc           | 0.748 | [0.739, 0.756] |

### Balanced ratio, imbalanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| log-likelihood       | 0.060        | [0.055, 0.065]  |
| norm unpooled        | 0.056        | [0.051, 0.060]  |
| mean z-test unpooled | 0.053        | [0.049, 0.058]  |
| mean z-test          | 0.052        | [0.048, 0.057]  |
| norm                 | 0.050        | [0.046, 0.055]  |
| pearson              | 0.050        | [0.046, 0.055]  |
| mean t-test unpooled | 0.049        | [0.045, 0.053]  |
| mean t-test          | 0.049        | [0.045, 0.053]  |
| barnard              | 0.046        | [0.042, 0.050]  |
| barnard unpooled     | 0.043        | [0.040, 0.048]  |
| boschloo             | 0.035        | [0.031, 0.039]  |
| fisher               | 0.031        | [0.027, 0.034]  |
| log-likelihood cc    | 0.022        | [0.020, 0.026]  |
| norm unpooled cc     | 0.022        | [0.019, 0.025]  |
| norm cc              | 0.018        | [0.016, 0.021]  |
| pearson cc           | 0.018        | [0.016, 0.021]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0.228 |
| relative effect size                  | 2.28  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.829 | [0.821, 0.836] |
| mean z-test          | 0.824 | [0.816, 0.831] |
| log-likelihood       | 0.824 | [0.816, 0.831] |
| mean z-test unpooled | 0.822 | [0.814, 0.829] |
| norm                 | 0.821 | [0.813, 0.828] |
| pearson              | 0.821 | [0.813, 0.828] |
| mean t-test          | 0.820 | [0.812, 0.827] |
| mean t-test unpooled | 0.815 | [0.807, 0.822] |
| barnard              | 0.810 | [0.802, 0.818] |
| barnard unpooled     | 0.804 | [0.796, 0.812] |
| boschloo             | 0.798 | [0.790, 0.805] |
| fisher               | 0.779 | [0.771, 0.787] |
| norm unpooled cc     | 0.755 | [0.746, 0.763] |
| log-likelihood cc    | 0.751 | [0.743, 0.760] |
| norm cc              | 0.740 | [0.731, 0.749] |
| pearson cc           | 0.740 | [0.731, 0.749] |

### Imbalanced ratio, balanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.068        | [0.063, 0.073]  |
| mean z-test unpooled | 0.063        | [0.058, 0.068]  |
| mean z-test          | 0.053        | [0.049, 0.058]  |
| log-likelihood       | 0.053        | [0.048, 0.057]  |
| norm                 | 0.051        | [0.047, 0.056]  |
| pearson              | 0.051        | [0.047, 0.056]  |
| mean t-test          | 0.051        | [0.046, 0.055]  |
| mean t-test unpooled | 0.050        | [0.046, 0.055]  |
| boschloo             | 0.048        | [0.044, 0.052]  |
| norm unpooled cc     | 0.038        | [0.035, 0.042]  |
| barnard              | 0.036        | [0.033, 0.040]  |
| fisher               | 0.036        | [0.033, 0.040]  |
| log-likelihood cc    | 0.029        | [0.026, 0.033]  |
| norm cc              | 0.027        | [0.024, 0.031]  |
| pearson cc           | 0.027        | [0.024, 0.031]  |
| barnard unpooled     | 0.007        | [0.005, 0.008]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0.347 |
| relative effect size                  | 0.69  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.892 | [0.886, 0.898] |
| mean z-test unpooled | 0.886 | [0.880, 0.892] |
| mean t-test unpooled | 0.867 | [0.860, 0.874] |
| log-likelihood       | 0.856 | [0.849, 0.863] |
| mean z-test          | 0.847 | [0.839, 0.854] |
| norm                 | 0.842 | [0.835, 0.849] |
| pearson              | 0.842 | [0.835, 0.849] |
| mean t-test          | 0.840 | [0.833, 0.847] |
| boschloo             | 0.837 | [0.829, 0.844] |
| norm unpooled cc     | 0.834 | [0.826, 0.841] |
| fisher               | 0.802 | [0.794, 0.810] |
| barnard              | 0.781 | [0.773, 0.790] |
| log-likelihood cc    | 0.774 | [0.766, 0.782] |
| norm cc              | 0.755 | [0.747, 0.764] |
| pearson cc           | 0.755 | [0.747, 0.764] |
| barnard unpooled     | 0.613 | [0.603, 0.622] |

### Imbalanced ratio, imbalanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.146        | [0.140, 0.154]  |
| mean z-test unpooled | 0.144        | [0.137, 0.151]  |
| mean t-test unpooled | 0.142        | [0.135, 0.149]  |
| log-likelihood       | 0.071        | [0.066, 0.077]  |
| norm unpooled cc     | 0.068        | [0.063, 0.073]  |
| mean z-test          | 0.042        | [0.038, 0.046]  |
| norm                 | 0.041        | [0.037, 0.045]  |
| pearson              | 0.041        | [0.037, 0.045]  |
| mean t-test          | 0.040        | [0.037, 0.044]  |
| barnard unpooled     | 0.034        | [0.031, 0.038]  |
| barnard              | 0.034        | [0.030, 0.037]  |
| fisher               | 0.025        | [0.022, 0.029]  |
| boschloo             | 0.024        | [0.021, 0.027]  |
| norm cc              | 0.017        | [0.015, 0.020]  |
| pearson cc           | 0.017        | [0.015, 0.020]  |
| log-likelihood cc    | 0.013        | [0.011, 0.015]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 100   |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0.249 |
| relative effect size                  | 2.49  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| mean z-test          | 0.749 | [0.740, 0.757] |
| norm                 | 0.744 | [0.735, 0.752] |
| pearson              | 0.744 | [0.735, 0.752] |
| mean t-test          | 0.743 | [0.735, 0.752] |
| barnard              | 0.703 | [0.694, 0.712] |
| log-likelihood       | 0.701 | [0.692, 0.710] |
| fisher               | 0.694 | [0.685, 0.703] |
| boschloo             | 0.684 | [0.675, 0.693] |
| norm cc              | 0.645 | [0.636, 0.655] |
| pearson cc           | 0.645 | [0.636, 0.655] |
| norm unpooled        | 0.602 | [0.592, 0.611] |
| log-likelihood cc    | 0.596 | [0.586, 0.605] |
| mean z-test unpooled | 0.582 | [0.572, 0.592] |
| mean t-test unpooled | 0.530 | [0.521, 0.540] |
| norm unpooled cc     | 0.478 | [0.468, 0.488] |
| barnard unpooled     | 0.189 | [0.181, 0.196] |

## Large sample

### Balanced ratio, balanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.050        | [0.046, 0.054]  |
| mean z-test          | 0.050        | [0.046, 0.054]  |
| mean z-test unpooled | 0.050        | [0.046, 0.054]  |
| log-likelihood       | 0.050        | [0.045, 0.054]  |
| norm                 | 0.049        | [0.045, 0.054]  |
| pearson              | 0.049        | [0.045, 0.054]  |
| mean t-test          | 0.049        | [0.045, 0.054]  |
| mean t-test unpooled | 0.049        | [0.045, 0.054]  |
| fisher               | 0.047        | [0.043, 0.051]  |
| norm unpooled cc     | 0.044        | [0.040, 0.048]  |
| log-likelihood cc    | 0.043        | [0.039, 0.047]  |
| norm cc              | 0.043        | [0.039, 0.047]  |
| pearson cc           | 0.043        | [0.039, 0.047]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.5   |
| effect size                           | 0.088 |
| relative effect size                  | 0.18  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.801 | [0.793, 0.809] |
| mean z-test unpooled | 0.800 | [0.793, 0.808] |
| mean z-test          | 0.800 | [0.792, 0.808] |
| log-likelihood       | 0.800 | [0.792, 0.808] |
| norm                 | 0.800 | [0.792, 0.808] |
| pearson              | 0.800 | [0.792, 0.808] |
| mean t-test          | 0.800 | [0.792, 0.807] |
| mean t-test unpooled | 0.800 | [0.792, 0.807] |
| fisher               | 0.797 | [0.789, 0.805] |
| norm unpooled cc     | 0.784 | [0.776, 0.792] |
| log-likelihood cc    | 0.784 | [0.775, 0.792] |
| norm cc              | 0.783 | [0.775, 0.792] |
| pearson cc           | 0.783 | [0.775, 0.792] |

### Balanced ratio, imbalanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| log-likelihood       | 0.048        | [0.044, 0.053]  |
| norm unpooled        | 0.048        | [0.044, 0.053]  |
| mean z-test unpooled | 0.048        | [0.044, 0.053]  |
| mean z-test          | 0.048        | [0.044, 0.052]  |
| mean t-test unpooled | 0.048        | [0.044, 0.052]  |
| norm                 | 0.048        | [0.044, 0.052]  |
| pearson              | 0.048        | [0.044, 0.052]  |
| mean t-test          | 0.048        | [0.044, 0.052]  |
| fisher               | 0.041        | [0.037, 0.045]  |
| norm unpooled cc     | 0.037        | [0.033, 0.041]  |
| log-likelihood cc    | 0.037        | [0.033, 0.041]  |
| norm cc              | 0.036        | [0.033, 0.040]  |
| pearson cc           | 0.036        | [0.033, 0.040]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 1     |
| proportion in control                 | 0.1   |
| effect size                           | 0.059 |
| relative effect size                  | 0.59  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| log-likelihood       | 0.804 | [0.796, 0.811] |
| norm unpooled        | 0.804 | [0.796, 0.811] |
| mean z-test unpooled | 0.803 | [0.796, 0.811] |
| mean z-test          | 0.803 | [0.795, 0.811] |
| mean t-test unpooled | 0.803 | [0.795, 0.811] |
| norm                 | 0.803 | [0.795, 0.811] |
| pearson              | 0.803 | [0.795, 0.811] |
| mean t-test          | 0.803 | [0.795, 0.811] |
| fisher               | 0.788 | [0.780, 0.796] |
| log-likelihood cc    | 0.775 | [0.767, 0.784] |
| norm unpooled cc     | 0.775 | [0.767, 0.784] |
| norm cc              | 0.774 | [0.766, 0.783] |
| pearson cc           | 0.774 | [0.766, 0.783] |

### Imbalanced ratio, balanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.052        | [0.048, 0.056]  |
| mean z-test unpooled | 0.051        | [0.047, 0.056]  |
| mean z-test          | 0.051        | [0.047, 0.055]  |
| log-likelihood       | 0.051        | [0.047, 0.055]  |
| mean t-test unpooled | 0.051        | [0.047, 0.055]  |
| mean t-test          | 0.051        | [0.046, 0.055]  |
| norm                 | 0.051        | [0.046, 0.055]  |
| pearson              | 0.051        | [0.046, 0.055]  |
| fisher               | 0.046        | [0.042, 0.050]  |
| norm unpooled cc     | 0.044        | [0.040, 0.048]  |
| log-likelihood cc    | 0.042        | [0.039, 0.047]  |
| norm cc              | 0.042        | [0.038, 0.046]  |
| pearson cc           | 0.042        | [0.038, 0.046]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.5   |
| effect size                           | 0.111 |
| relative effect size                  | 0.22  |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| norm unpooled        | 0.811 | [0.803, 0.819] |
| mean z-test unpooled | 0.810 | [0.802, 0.818] |
| mean t-test unpooled | 0.809 | [0.801, 0.816] |
| log-likelihood       | 0.807 | [0.800, 0.815] |
| mean z-test          | 0.806 | [0.799, 0.814] |
| norm                 | 0.806 | [0.798, 0.814] |
| pearson              | 0.806 | [0.798, 0.814] |
| mean t-test          | 0.806 | [0.798, 0.814] |
| fisher               | 0.795 | [0.787, 0.803] |
| norm unpooled cc     | 0.791 | [0.783, 0.799] |
| log-likelihood cc    | 0.786 | [0.778, 0.794] |
| norm cc              | 0.784 | [0.776, 0.792] |
| pearson cc           | 0.784 | [0.776, 0.792] |

### Imbalanced ratio, imbalanced proportion

A/A tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0     |
| relative effect size                  | 0     |

| metric               | type I error | type I error ci |
|:---------------------|:-------------|:----------------|
| norm unpooled        | 0.054        | [0.050, 0.059]  |
| mean z-test unpooled | 0.054        | [0.050, 0.059]  |
| mean t-test unpooled | 0.054        | [0.049, 0.058]  |
| mean z-test          | 0.051        | [0.047, 0.056]  |
| mean t-test          | 0.051        | [0.047, 0.056]  |
| norm                 | 0.051        | [0.047, 0.056]  |
| pearson              | 0.051        | [0.047, 0.056]  |
| log-likelihood       | 0.051        | [0.047, 0.055]  |
| fisher               | 0.044        | [0.040, 0.048]  |
| norm unpooled cc     | 0.042        | [0.038, 0.046]  |
| log-likelihood cc    | 0.038        | [0.035, 0.042]  |
| norm cc              | 0.037        | [0.033, 0.041]  |
| pearson cc           | 0.037        | [0.033, 0.041]  |

Power tests

| parameter                             | value |
|:--------------------------------------|:------|
| number of observations                | 1000  |
| treatment to control allocation ratio | 0.25  |
| proportion in control                 | 0.1   |
| effect size                           | 0.07  |
| relative effect size                  | 0.7   |

| metric               | power | power ci       |
|:---------------------|:------|:---------------|
| mean z-test          | 0.778 | [0.769, 0.786] |
| norm                 | 0.777 | [0.769, 0.785] |
| pearson              | 0.777 | [0.769, 0.785] |
| mean t-test          | 0.777 | [0.768, 0.785] |
| log-likelihood       | 0.761 | [0.752, 0.769] |
| fisher               | 0.756 | [0.748, 0.765] |
| norm cc              | 0.743 | [0.734, 0.752] |
| pearson cc           | 0.743 | [0.734, 0.752] |
| log-likelihood cc    | 0.725 | [0.716, 0.734] |
| norm unpooled        | 0.716 | [0.707, 0.725] |
| mean z-test unpooled | 0.714 | [0.705, 0.723] |
| mean t-test unpooled | 0.711 | [0.701, 0.719] |
| norm unpooled cc     | 0.669 | [0.660, 0.679] |
