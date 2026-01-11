# Comparison of two-sample proportion tests

## Small sample

### Balanced ratio, balanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 1     |
| proportion in control      | 0.5   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.058        | [0.054, 0.063]  |
| mean z-test        | 0.057        | [0.053, 0.062]  |
| mean z-test pooled | 0.057        | [0.052, 0.061]  |
| log-likelihood     | 0.055        | [0.051, 0.060]  |
| norm pooled        | 0.055        | [0.051, 0.060]  |
| pearson            | 0.055        | [0.051, 0.060]  |
| mean t-test pooled | 0.054        | [0.050, 0.059]  |
| mean t-test        | 0.054        | [0.050, 0.059]  |
| barnard pooled     | 0.049        | [0.045, 0.054]  |
| boschloo           | 0.049        | [0.045, 0.053]  |
| barnard            | 0.047        | [0.043, 0.052]  |
| fisher             | 0.045        | [0.042, 0.050]  |
| norm cc            | 0.038        | [0.034, 0.042]  |
| log-likelihood cc  | 0.035        | [0.032, 0.039]  |
| norm pooled cc     | 0.035        | [0.031, 0.039]  |
| pearson cc         | 0.035        | [0.031, 0.039]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 1     |
| proportion in control      | 0.5   |
| effect size                | 0.284 |
| relative effect size       | 0.57  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| norm               | 0.858 | [0.850, 0.864] |
| mean z-test pooled | 0.853 | [0.846, 0.860] |
| mean z-test        | 0.852 | [0.844, 0.858] |
| log-likelihood     | 0.851 | [0.844, 0.858] |
| norm pooled        | 0.851 | [0.844, 0.858] |
| pearson            | 0.851 | [0.844, 0.858] |
| mean t-test pooled | 0.849 | [0.842, 0.856] |
| mean t-test        | 0.846 | [0.839, 0.853] |
| barnard pooled     | 0.841 | [0.834, 0.848] |
| boschloo           | 0.837 | [0.830, 0.844] |
| barnard            | 0.835 | [0.828, 0.842] |
| fisher             | 0.817 | [0.809, 0.825] |
| norm cc            | 0.805 | [0.797, 0.812] |
| log-likelihood cc  | 0.796 | [0.788, 0.804] |
| norm pooled cc     | 0.793 | [0.784, 0.800] |
| pearson cc         | 0.793 | [0.784, 0.800] |

### Balanced ratio, unbalanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 1     |
| proportion in control      | 0.1   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| log-likelihood     | 0.059        | [0.055, 0.064]  |
| norm               | 0.055        | [0.051, 0.060]  |
| mean z-test        | 0.053        | [0.049, 0.058]  |
| mean z-test pooled | 0.052        | [0.047, 0.056]  |
| mean t-test        | 0.050        | [0.046, 0.054]  |
| norm pooled        | 0.050        | [0.045, 0.054]  |
| pearson            | 0.050        | [0.045, 0.054]  |
| mean t-test pooled | 0.048        | [0.044, 0.053]  |
| barnard pooled     | 0.046        | [0.042, 0.050]  |
| barnard            | 0.045        | [0.041, 0.049]  |
| boschloo           | 0.035        | [0.031, 0.038]  |
| fisher             | 0.032        | [0.028, 0.035]  |
| norm cc            | 0.024        | [0.021, 0.027]  |
| log-likelihood cc  | 0.024        | [0.021, 0.027]  |
| norm pooled cc     | 0.019        | [0.016, 0.022]  |
| pearson cc         | 0.019        | [0.016, 0.022]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 1     |
| proportion in control      | 0.1   |
| effect size                | 0.178 |
| relative effect size       | 1.78  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| norm               | 0.657 | [0.647, 0.666] |
| log-likelihood     | 0.650 | [0.640, 0.659] |
| mean z-test pooled | 0.649 | [0.639, 0.658] |
| mean z-test        | 0.647 | [0.637, 0.656] |
| norm pooled        | 0.644 | [0.634, 0.653] |
| pearson            | 0.644 | [0.634, 0.653] |
| mean t-test pooled | 0.641 | [0.632, 0.651] |
| mean t-test        | 0.637 | [0.627, 0.646] |
| barnard pooled     | 0.628 | [0.619, 0.638] |
| barnard            | 0.620 | [0.611, 0.630] |
| boschloo           | 0.606 | [0.597, 0.616] |
| fisher             | 0.582 | [0.573, 0.592] |
| norm cc            | 0.550 | [0.540, 0.560] |
| log-likelihood cc  | 0.547 | [0.538, 0.557] |
| norm pooled cc     | 0.534 | [0.525, 0.544] |
| pearson cc         | 0.534 | [0.525, 0.544] |

### Unbalanced ratio, balanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.5   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.062        | [0.057, 0.067]  |
| mean z-test        | 0.058        | [0.054, 0.063]  |
| log-likelihood     | 0.048        | [0.044, 0.053]  |
| mean z-test pooled | 0.048        | [0.044, 0.052]  |
| norm pooled        | 0.047        | [0.043, 0.051]  |
| pearson            | 0.047        | [0.043, 0.051]  |
| mean t-test        | 0.046        | [0.042, 0.051]  |
| mean t-test pooled | 0.046        | [0.042, 0.050]  |
| boschloo           | 0.042        | [0.038, 0.046]  |
| norm cc            | 0.033        | [0.030, 0.037]  |
| barnard pooled     | 0.033        | [0.030, 0.037]  |
| fisher             | 0.031        | [0.027, 0.034]  |
| log-likelihood cc  | 0.025        | [0.022, 0.028]  |
| norm pooled cc     | 0.023        | [0.020, 0.026]  |
| pearson cc         | 0.023        | [0.020, 0.026]  |
| barnard            | 0.006        | [0.005, 0.008]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.5   |
| effect size                | 0.364 |
| relative effect size       | 0.73  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| norm               | 0.926 | [0.920, 0.931] |
| mean z-test        | 0.922 | [0.916, 0.927] |
| mean t-test        | 0.908 | [0.902, 0.914] |
| log-likelihood     | 0.899 | [0.893, 0.905] |
| mean z-test pooled | 0.892 | [0.886, 0.898] |
| norm pooled        | 0.889 | [0.882, 0.895] |
| pearson            | 0.889 | [0.882, 0.895] |
| mean t-test pooled | 0.887 | [0.881, 0.893] |
| boschloo           | 0.886 | [0.879, 0.892] |
| norm cc            | 0.882 | [0.876, 0.889] |
| fisher             | 0.853 | [0.846, 0.860] |
| barnard pooled     | 0.835 | [0.828, 0.843] |
| log-likelihood cc  | 0.831 | [0.823, 0.838] |
| norm pooled cc     | 0.815 | [0.807, 0.823] |
| pearson cc         | 0.815 | [0.807, 0.823] |
| barnard            | 0.693 | [0.684, 0.702] |

### Unbalanced ratio, unbalanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.1   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.153        | [0.146, 0.160]  |
| mean z-test        | 0.151        | [0.144, 0.158]  |
| mean t-test        | 0.147        | [0.140, 0.154]  |
| log-likelihood     | 0.073        | [0.068, 0.078]  |
| norm cc            | 0.072        | [0.067, 0.077]  |
| mean z-test pooled | 0.040        | [0.036, 0.044]  |
| norm pooled        | 0.039        | [0.035, 0.043]  |
| pearson            | 0.039        | [0.035, 0.043]  |
| mean t-test pooled | 0.038        | [0.034, 0.042]  |
| barnard            | 0.034        | [0.031, 0.038]  |
| barnard pooled     | 0.031        | [0.028, 0.035]  |
| fisher             | 0.025        | [0.022, 0.028]  |
| boschloo           | 0.023        | [0.020, 0.026]  |
| norm pooled cc     | 0.015        | [0.013, 0.018]  |
| pearson cc         | 0.015        | [0.013, 0.018]  |
| log-likelihood cc  | 0.013        | [0.011, 0.016]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 100   |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.1   |
| effect size                | 0.228 |
| relative effect size       | 2.28  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| mean z-test pooled | 0.695 | [0.685, 0.704] |
| mean t-test pooled | 0.689 | [0.680, 0.698] |
| norm pooled        | 0.689 | [0.680, 0.698] |
| pearson            | 0.689 | [0.680, 0.698] |
| barnard pooled     | 0.647 | [0.637, 0.656] |
| log-likelihood     | 0.643 | [0.633, 0.652] |
| fisher             | 0.635 | [0.625, 0.644] |
| boschloo           | 0.624 | [0.615, 0.634] |
| norm pooled cc     | 0.585 | [0.575, 0.594] |
| pearson cc         | 0.585 | [0.575, 0.594] |
| norm               | 0.536 | [0.527, 0.546] |
| log-likelihood cc  | 0.529 | [0.519, 0.539] |
| mean z-test        | 0.518 | [0.508, 0.528] |
| mean t-test        | 0.466 | [0.456, 0.476] |
| norm cc            | 0.409 | [0.399, 0.419] |
| barnard            | 0.152 | [0.145, 0.159] |

## Large sample

### Balanced ratio, balanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 1     |
| proportion in control      | 0.5   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.055        | [0.051, 0.060]  |
| mean z-test        | 0.055        | [0.050, 0.059]  |
| mean z-test pooled | 0.055        | [0.050, 0.059]  |
| log-likelihood     | 0.054        | [0.050, 0.059]  |
| mean t-test        | 0.054        | [0.049, 0.058]  |
| mean t-test pooled | 0.054        | [0.049, 0.058]  |
| norm pooled        | 0.054        | [0.049, 0.058]  |
| pearson            | 0.054        | [0.049, 0.058]  |
| norm cc            | 0.046        | [0.042, 0.051]  |
| log-likelihood cc  | 0.046        | [0.042, 0.050]  |
| norm pooled cc     | 0.046        | [0.042, 0.050]  |
| pearson cc         | 0.046        | [0.042, 0.050]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 1     |
| proportion in control      | 0.5   |
| effect size                | 0.089 |
| relative effect size       | 0.18  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| norm               | 0.806 | [0.798, 0.813] |
| mean z-test        | 0.805 | [0.797, 0.813] |
| mean z-test pooled | 0.805 | [0.797, 0.813] |
| log-likelihood     | 0.805 | [0.797, 0.812] |
| norm pooled        | 0.805 | [0.797, 0.812] |
| pearson            | 0.805 | [0.797, 0.812] |
| mean t-test pooled | 0.804 | [0.796, 0.812] |
| mean t-test        | 0.804 | [0.796, 0.812] |
| norm cc            | 0.786 | [0.778, 0.794] |
| log-likelihood cc  | 0.785 | [0.776, 0.793] |
| norm pooled cc     | 0.785 | [0.776, 0.793] |
| pearson cc         | 0.785 | [0.776, 0.793] |

### Balanced ratio, unbalanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 1     |
| proportion in control      | 0.1   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| log-likelihood     | 0.052        | [0.048, 0.057]  |
| mean z-test pooled | 0.052        | [0.048, 0.057]  |
| norm               | 0.052        | [0.048, 0.057]  |
| mean z-test        | 0.052        | [0.048, 0.057]  |
| mean t-test pooled | 0.052        | [0.048, 0.056]  |
| norm pooled        | 0.052        | [0.048, 0.056]  |
| pearson            | 0.052        | [0.048, 0.056]  |
| mean t-test        | 0.052        | [0.047, 0.056]  |
| log-likelihood cc  | 0.039        | [0.036, 0.043]  |
| norm cc            | 0.039        | [0.036, 0.043]  |
| norm pooled cc     | 0.039        | [0.035, 0.043]  |
| pearson cc         | 0.039        | [0.035, 0.043]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 1     |
| proportion in control      | 0.1   |
| effect size                | 0.056 |
| relative effect size       | 0.56  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| log-likelihood     | 0.750 | [0.741, 0.758] |
| norm               | 0.750 | [0.741, 0.758] |
| mean z-test        | 0.750 | [0.741, 0.758] |
| mean z-test pooled | 0.749 | [0.741, 0.758] |
| norm pooled        | 0.749 | [0.740, 0.757] |
| pearson            | 0.749 | [0.740, 0.757] |
| mean t-test        | 0.749 | [0.740, 0.757] |
| mean t-test pooled | 0.749 | [0.740, 0.757] |
| norm cc            | 0.720 | [0.711, 0.729] |
| log-likelihood cc  | 0.719 | [0.710, 0.728] |
| norm pooled cc     | 0.718 | [0.709, 0.727] |
| pearson cc         | 0.718 | [0.709, 0.727] |

### Unbalanced ratio, balanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.5   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.048        | [0.043, 0.052]  |
| mean z-test        | 0.047        | [0.043, 0.051]  |
| log-likelihood     | 0.046        | [0.042, 0.051]  |
| mean z-test pooled | 0.046        | [0.042, 0.051]  |
| mean t-test        | 0.046        | [0.042, 0.050]  |
| mean t-test pooled | 0.046        | [0.042, 0.050]  |
| norm pooled        | 0.046        | [0.042, 0.050]  |
| pearson            | 0.046        | [0.042, 0.050]  |
| norm cc            | 0.039        | [0.035, 0.043]  |
| log-likelihood cc  | 0.038        | [0.034, 0.042]  |
| norm pooled cc     | 0.037        | [0.034, 0.041]  |
| pearson cc         | 0.037        | [0.034, 0.041]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.5   |
| effect size                | 0.111 |
| relative effect size       | 0.22  |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| norm               | 0.813 | [0.805, 0.821] |
| mean z-test        | 0.812 | [0.804, 0.819] |
| mean t-test        | 0.810 | [0.802, 0.817] |
| log-likelihood     | 0.808 | [0.800, 0.816] |
| mean z-test pooled | 0.806 | [0.799, 0.814] |
| norm pooled        | 0.806 | [0.798, 0.814] |
| pearson            | 0.806 | [0.798, 0.814] |
| mean t-test pooled | 0.806 | [0.798, 0.814] |
| norm cc            | 0.790 | [0.781, 0.798] |
| log-likelihood cc  | 0.784 | [0.775, 0.792] |
| norm pooled cc     | 0.781 | [0.773, 0.789] |
| pearson cc         | 0.781 | [0.773, 0.789] |

### Unbalanced ratio, unbalanced proportion

AA tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.1   |
| effect size                | 0     |
| relative effect size       | 0     |

| metric             | type I error | type I error ci |
|:-------------------|:-------------|:----------------|
| norm               | 0.058        | [0.054, 0.063]  |
| mean z-test        | 0.058        | [0.053, 0.062]  |
| mean t-test        | 0.057        | [0.053, 0.062]  |
| log-likelihood     | 0.054        | [0.050, 0.059]  |
| mean z-test pooled | 0.053        | [0.049, 0.058]  |
| mean t-test pooled | 0.053        | [0.049, 0.058]  |
| norm pooled        | 0.053        | [0.049, 0.058]  |
| pearson            | 0.053        | [0.049, 0.058]  |
| norm cc            | 0.044        | [0.040, 0.048]  |
| log-likelihood cc  | 0.040        | [0.036, 0.044]  |
| norm pooled cc     | 0.038        | [0.035, 0.043]  |
| pearson cc         | 0.038        | [0.035, 0.043]  |

Power tests

| parameter                  | value |
|:---------------------------|:------|
| number of simulations      | 10000 |
| number of observations     | 1000  |
| treatment to control ratio | 0.25  |
| proportion in control      | 0.1   |
| effect size                | 0.07  |
| relative effect size       | 0.7   |

| metric             | power | power ci       |
|:-------------------|:------|:---------------|
| mean z-test pooled | 0.764 | [0.755, 0.772] |
| norm pooled        | 0.763 | [0.755, 0.772] |
| pearson            | 0.763 | [0.755, 0.772] |
| mean t-test pooled | 0.763 | [0.754, 0.771] |
| log-likelihood     | 0.745 | [0.736, 0.753] |
| norm pooled cc     | 0.724 | [0.715, 0.733] |
| pearson cc         | 0.724 | [0.715, 0.733] |
| log-likelihood cc  | 0.701 | [0.692, 0.710] |
| norm               | 0.690 | [0.681, 0.699] |
| mean z-test        | 0.688 | [0.679, 0.697] |
| mean t-test        | 0.685 | [0.676, 0.694] |
| norm cc            | 0.650 | [0.640, 0.659] |
