# Simulation

| parameter             | value |
| :-------------------- | ----: |
| number of simulations | 10000 |
| alpha                 |  0.05 |
| power                 |   0.8 |

## Small sample

### Balanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |   100 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.269 |
| relative effect size (in power)       |  0.54 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of proportions (unpooled)     | 0.812 | [0.804, 0.819] |       0.0561 | [0.0517, 0.0608] |
| Z-test of means                      | 0.807 | [0.799, 0.814] |       0.0553 | [0.0509, 0.0600] |
| Z-test of means (unpooled)           | 0.806 | [0.799, 0.814] |       0.0555 | [0.0511, 0.0602] |
| G-test                               | 0.805 | [0.797, 0.813] |       0.0530 | [0.0487, 0.0576] |
| Pearson's chi-squared                | 0.804 | [0.796, 0.812] |       0.0530 | [0.0487, 0.0576] |
| Z-test of proportions                | 0.804 | [0.796, 0.812] |       0.0530 | [0.0487, 0.0576] |
| Student's t-test                     | 0.801 | [0.793, 0.809] |       0.0519 | [0.0477, 0.0565] |
| Welch's t-test                       | 0.800 | [0.792, 0.808] |       0.0512 | [0.0470, 0.0557] |
| Barnard                              | 0.794 | [0.786, 0.801] |       0.0454 | [0.0414, 0.0497] |
| Boschloo                             | 0.787 | [0.779, 0.795] |       0.0450 | [0.0411, 0.0493] |
| Barnard (unpooled)                   | 0.784 | [0.776, 0.792] |       0.0423 | [0.0385, 0.0465] |
| Fisher                               | 0.763 | [0.755, 0.771] |       0.0402 | [0.0365, 0.0443] |
| Z-test of proportions (unpooled, cc) | 0.749 | [0.740, 0.757] |       0.0347 | [0.0312, 0.0385] |
| G-test (cc)                          | 0.739 | [0.731, 0.748] |       0.0324 | [0.0291, 0.0361] |
| Pearson's chi-squared (cc)           | 0.735 | [0.727, 0.744] |       0.0319 | [0.0286, 0.0356] |
| Z-test of proportions (cc)           | 0.735 | [0.727, 0.744] |       0.0319 | [0.0286, 0.0356] |

### Balanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |   100 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.1 |
| effect size (in power)                | 0.228 |
| relative effect size (in power)       |  2.28 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of proportions (unpooled)     | 0.830 | [0.823, 0.838] |       0.0612 | [0.0566, 0.0661] |
| G-test                               | 0.824 | [0.817, 0.832] |       0.0630 | [0.0584, 0.0680] |
| Z-test of means                      | 0.824 | [0.816, 0.831] |       0.0558 | [0.0514, 0.0605] |
| Z-test of means (unpooled)           | 0.821 | [0.813, 0.828] |       0.0585 | [0.0540, 0.0633] |
| Pearson's chi-squared                | 0.821 | [0.813, 0.828] |       0.0538 | [0.0495, 0.0584] |
| Z-test of proportions                | 0.821 | [0.813, 0.828] |       0.0538 | [0.0495, 0.0584] |
| Student's t-test                     | 0.820 | [0.812, 0.827] |       0.0523 | [0.0481, 0.0569] |
| Welch's t-test                       | 0.815 | [0.807, 0.822] |       0.0538 | [0.0495, 0.0584] |
| Barnard                              | 0.808 | [0.800, 0.816] |       0.0488 | [0.0447, 0.0533] |
| Barnard (unpooled)                   | 0.805 | [0.797, 0.812] |       0.0473 | [0.0433, 0.0517] |
| Boschloo                             | 0.796 | [0.788, 0.804] |       0.0356 | [0.0321, 0.0395] |
| Fisher                               | 0.777 | [0.768, 0.785] |       0.0344 | [0.0310, 0.0382] |
| Z-test of proportions (unpooled, cc) | 0.752 | [0.743, 0.761] |       0.0249 | [0.0220, 0.0282] |
| G-test (cc)                          | 0.746 | [0.738, 0.755] |       0.0256 | [0.0226, 0.0289] |
| Pearson's chi-squared (cc)           | 0.737 | [0.728, 0.745] |       0.0218 | [0.0191, 0.0249] |
| Z-test of proportions (cc)           | 0.737 | [0.728, 0.745] |       0.0218 | [0.0191, 0.0249] |

### Imbalanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |   100 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.347 |
| relative effect size (in power)       |  0.69 |

| test                                 | power |       power ci | type I error |   type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ----------------: |
| Z-test of proportions (unpooled)     | 0.896 | [0.890, 0.902] |       0.0666 |  [0.0618, 0.0717] |
| Z-test of means (unpooled)           | 0.892 | [0.886, 0.898] |       0.0628 |  [0.0582, 0.0678] |
| Welch's t-test                       | 0.874 | [0.868, 0.881] |       0.0513 |  [0.0471, 0.0559] |
| G-test                               | 0.864 | [0.857, 0.870] |       0.0527 |  [0.0484, 0.0573] |
| Z-test of means                      | 0.856 | [0.849, 0.862] |       0.0524 |  [0.0482, 0.0570] |
| Pearson's chi-squared                | 0.850 | [0.843, 0.857] |       0.0509 |  [0.0467, 0.0554] |
| Z-test of proportions                | 0.850 | [0.843, 0.857] |       0.0509 |  [0.0467, 0.0554] |
| Student's t-test                     | 0.848 | [0.841, 0.855] |       0.0503 |  [0.0461, 0.0548] |
| Boschloo                             | 0.848 | [0.841, 0.855] |       0.0471 |  [0.0431, 0.0515] |
| Z-test of proportions (unpooled, cc) | 0.845 | [0.837, 0.852] |       0.0382 |  [0.0346, 0.0422] |
| Fisher                               | 0.811 | [0.803, 0.819] |       0.0364 |  [0.0329, 0.0403] |
| Barnard                              | 0.791 | [0.783, 0.799] |       0.0384 |  [0.0348, 0.0424] |
| G-test (cc)                          | 0.784 | [0.776, 0.792] |       0.0296 |  [0.0264, 0.0332] |
| Pearson's chi-squared (cc)           | 0.765 | [0.756, 0.773] |       0.0278 |  [0.0247, 0.0313] |
| Z-test of proportions (cc)           | 0.765 | [0.756, 0.773] |       0.0278 |  [0.0247, 0.0313] |
| Barnard (unpooled)                   | 0.622 | [0.612, 0.631] |      0.00810 | [0.00648, 0.0101] |

### Imbalanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |   100 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.1 |
| effect size (in power)                | 0.249 |
| relative effect size (in power)       |  2.49 |

| test                                 | power |       power ci | type I error |   type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ----------------: |
| Z-test of means                      | 0.755 | [0.746, 0.763] |       0.0430 |  [0.0391, 0.0472] |
| Student's t-test                     | 0.750 | [0.742, 0.759] |       0.0414 |  [0.0376, 0.0455] |
| Pearson's chi-squared                | 0.750 | [0.742, 0.759] |       0.0419 |  [0.0381, 0.0461] |
| Z-test of proportions                | 0.750 | [0.742, 0.759] |       0.0419 |  [0.0381, 0.0461] |
| Barnard                              | 0.712 | [0.702, 0.720] |       0.0328 |  [0.0294, 0.0365] |
| G-test                               | 0.706 | [0.697, 0.715] |       0.0699 |  [0.0650, 0.0751] |
| Fisher                               | 0.699 | [0.690, 0.708] |       0.0245 |  [0.0216, 0.0278] |
| Boschloo                             | 0.689 | [0.680, 0.698] |       0.0233 |  [0.0205, 0.0265] |
| Pearson's chi-squared (cc)           | 0.649 | [0.640, 0.659] |       0.0155 |  [0.0132, 0.0182] |
| Z-test of proportions (cc)           | 0.649 | [0.640, 0.659] |       0.0155 |  [0.0132, 0.0182] |
| Z-test of proportions (unpooled)     | 0.608 | [0.599, 0.618] |        0.138 |    [0.131, 0.145] |
| G-test (cc)                          | 0.601 | [0.591, 0.610] |       0.0115 | [0.00954, 0.0138] |
| Z-test of means (unpooled)           | 0.588 | [0.578, 0.598] |        0.136 |    [0.129, 0.143] |
| Welch's t-test                       | 0.531 | [0.522, 0.541] |        0.132 |    [0.126, 0.139] |
| Z-test of proportions (unpooled, cc) | 0.477 | [0.467, 0.487] |       0.0663 |  [0.0615, 0.0714] |
| Barnard (unpooled)                   | 0.195 | [0.187, 0.203] |       0.0338 |  [0.0304, 0.0376] |

## Medium sample

### Balanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |  1000 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.088 |
| relative effect size (in power)       |  0.18 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of proportions (unpooled)     | 0.803 | [0.795, 0.811] |       0.0541 | [0.0498, 0.0588] |
| Z-test of means                      | 0.803 | [0.795, 0.811] |       0.0538 | [0.0495, 0.0584] |
| Z-test of means (unpooled)           | 0.803 | [0.795, 0.811] |       0.0538 | [0.0495, 0.0584] |
| G-test                               | 0.803 | [0.795, 0.810] |       0.0533 | [0.0490, 0.0579] |
| Pearson's chi-squared                | 0.802 | [0.794, 0.810] |       0.0530 | [0.0487, 0.0576] |
| Z-test of proportions                | 0.802 | [0.794, 0.810] |       0.0530 | [0.0487, 0.0576] |
| Student's t-test                     | 0.802 | [0.794, 0.810] |       0.0528 | [0.0485, 0.0574] |
| Welch's t-test                       | 0.802 | [0.794, 0.810] |       0.0528 | [0.0485, 0.0574] |
| Fisher                               | 0.798 | [0.790, 0.806] |       0.0505 | [0.0463, 0.0550] |
| Z-test of proportions (unpooled, cc) | 0.787 | [0.779, 0.795] |       0.0472 | [0.0432, 0.0516] |
| G-test (cc)                          | 0.786 | [0.778, 0.794] |       0.0465 | [0.0425, 0.0509] |
| Pearson's chi-squared (cc)           | 0.786 | [0.778, 0.794] |       0.0460 | [0.0420, 0.0503] |
| Z-test of proportions (cc)           | 0.786 | [0.778, 0.794] |       0.0460 | [0.0420, 0.0503] |

### Balanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |  1000 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.1 |
| effect size (in power)                | 0.059 |
| relative effect size (in power)       |  0.59 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| G-test                               | 0.806 | [0.798, 0.813] |       0.0503 | [0.0461, 0.0548] |
| Z-test of means                      | 0.805 | [0.797, 0.813] |       0.0497 | [0.0456, 0.0542] |
| Z-test of proportions (unpooled)     | 0.805 | [0.797, 0.813] |       0.0503 | [0.0461, 0.0548] |
| Pearson's chi-squared                | 0.805 | [0.797, 0.812] |       0.0495 | [0.0454, 0.0540] |
| Z-test of proportions                | 0.805 | [0.797, 0.812] |       0.0495 | [0.0454, 0.0540] |
| Z-test of means (unpooled)           | 0.805 | [0.797, 0.812] |       0.0501 | [0.0459, 0.0546] |
| Student's t-test                     | 0.805 | [0.797, 0.812] |       0.0495 | [0.0454, 0.0540] |
| Welch's t-test                       | 0.804 | [0.796, 0.812] |       0.0500 | [0.0459, 0.0545] |
| Fisher                               | 0.789 | [0.781, 0.797] |       0.0436 | [0.0397, 0.0478] |
| Z-test of proportions (unpooled, cc) | 0.776 | [0.768, 0.784] |       0.0397 | [0.0360, 0.0438] |
| G-test (cc)                          | 0.776 | [0.767, 0.784] |       0.0399 | [0.0362, 0.0440] |
| Pearson's chi-squared (cc)           | 0.775 | [0.767, 0.783] |       0.0392 | [0.0355, 0.0432] |
| Z-test of proportions (cc)           | 0.775 | [0.767, 0.783] |       0.0392 | [0.0355, 0.0432] |

### Imbalanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |  1000 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.111 |
| relative effect size (in power)       |  0.22 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of proportions (unpooled)     | 0.807 | [0.799, 0.814] |       0.0527 | [0.0484, 0.0573] |
| Z-test of means (unpooled)           | 0.805 | [0.798, 0.813] |       0.0522 | [0.0480, 0.0568] |
| Welch's t-test                       | 0.803 | [0.795, 0.811] |       0.0510 | [0.0468, 0.0555] |
| G-test                               | 0.802 | [0.794, 0.810] |       0.0512 | [0.0470, 0.0557] |
| Z-test of means                      | 0.802 | [0.794, 0.809] |       0.0512 | [0.0470, 0.0557] |
| Pearson's chi-squared                | 0.801 | [0.793, 0.809] |       0.0512 | [0.0470, 0.0557] |
| Z-test of proportions                | 0.801 | [0.793, 0.809] |       0.0512 | [0.0470, 0.0557] |
| Student's t-test                     | 0.801 | [0.793, 0.809] |       0.0512 | [0.0470, 0.0557] |
| Fisher                               | 0.791 | [0.782, 0.799] |       0.0463 | [0.0423, 0.0506] |
| Z-test of proportions (unpooled, cc) | 0.786 | [0.778, 0.794] |       0.0434 | [0.0395, 0.0476] |
| G-test (cc)                          | 0.781 | [0.773, 0.790] |       0.0422 | [0.0384, 0.0464] |
| Pearson's chi-squared (cc)           | 0.780 | [0.771, 0.788] |       0.0419 | [0.0381, 0.0461] |
| Z-test of proportions (cc)           | 0.780 | [0.771, 0.788] |       0.0419 | [0.0381, 0.0461] |

### Imbalanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           |  1000 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.1 |
| effect size (in power)                |  0.07 |
| relative effect size (in power)       |   0.7 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of means                      | 0.770 | [0.762, 0.778] |       0.0503 | [0.0461, 0.0548] |
| Pearson's chi-squared                | 0.770 | [0.761, 0.778] |       0.0501 | [0.0459, 0.0546] |
| Z-test of proportions                | 0.770 | [0.761, 0.778] |       0.0501 | [0.0459, 0.0546] |
| Student's t-test                     | 0.769 | [0.761, 0.778] |       0.0501 | [0.0459, 0.0546] |
| G-test                               | 0.749 | [0.740, 0.757] |       0.0510 | [0.0468, 0.0555] |
| Fisher                               | 0.745 | [0.737, 0.754] |       0.0433 | [0.0394, 0.0475] |
| Pearson's chi-squared (cc)           | 0.731 | [0.722, 0.739] |       0.0363 | [0.0328, 0.0402] |
| Z-test of proportions (cc)           | 0.731 | [0.722, 0.739] |       0.0363 | [0.0328, 0.0402] |
| G-test (cc)                          | 0.710 | [0.701, 0.719] |       0.0360 | [0.0325, 0.0399] |
| Z-test of proportions (unpooled)     | 0.701 | [0.692, 0.710] |       0.0543 | [0.0500, 0.0590] |
| Z-test of means (unpooled)           | 0.700 | [0.691, 0.709] |       0.0540 | [0.0497, 0.0587] |
| Welch's t-test                       | 0.697 | [0.688, 0.706] |       0.0532 | [0.0489, 0.0578] |
| Z-test of proportions (unpooled, cc) | 0.660 | [0.651, 0.670] |       0.0400 | [0.0363, 0.0441] |

## Large sample

### Balanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           | 10000 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.028 |
| relative effect size (in power)       |  0.06 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of means                      | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Z-test of means (unpooled)           | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Z-test of proportions (unpooled)     | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| G-test                               | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Pearson's chi-squared                | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Z-test of proportions                | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Student's t-test                     | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Welch's t-test                       | 0.797 | [0.789, 0.805] |       0.0465 | [0.0425, 0.0509] |
| Fisher                               | 0.797 | [0.789, 0.804] |       0.0457 | [0.0417, 0.0500] |
| Pearson's chi-squared (cc)           | 0.791 | [0.783, 0.799] |       0.0447 | [0.0408, 0.0490] |
| Z-test of proportions (cc)           | 0.791 | [0.783, 0.799] |       0.0447 | [0.0408, 0.0490] |
| G-test (cc)                          | 0.791 | [0.783, 0.799] |       0.0448 | [0.0409, 0.0491] |
| Z-test of proportions (unpooled, cc) | 0.791 | [0.783, 0.799] |       0.0449 | [0.0410, 0.0492] |

### Balanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           | 10000 |
| treatment to control allocation ratio |     1 |
| proportion in control                 |   0.1 |
| effect size (in power)                | 0.017 |
| relative effect size (in power)       |  0.17 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| G-test                               | 0.797 | [0.789, 0.805] |       0.0492 | [0.0451, 0.0537] |
| Z-test of proportions (unpooled)     | 0.797 | [0.789, 0.805] |       0.0492 | [0.0451, 0.0537] |
| Student's t-test                     | 0.797 | [0.789, 0.805] |       0.0492 | [0.0451, 0.0537] |
| Z-test of means (unpooled)           | 0.797 | [0.789, 0.805] |       0.0492 | [0.0451, 0.0537] |
| Pearson's chi-squared                | 0.797 | [0.789, 0.805] |       0.0493 | [0.0452, 0.0538] |
| Z-test of means                      | 0.797 | [0.789, 0.805] |       0.0493 | [0.0452, 0.0538] |
| Z-test of proportions                | 0.797 | [0.789, 0.805] |       0.0493 | [0.0452, 0.0538] |
| Welch's t-test                       | 0.797 | [0.789, 0.805] |       0.0492 | [0.0451, 0.0537] |
| Fisher                               | 0.793 | [0.785, 0.801] |       0.0477 | [0.0436, 0.0521] |
| G-test (cc)                          | 0.788 | [0.780, 0.796] |       0.0459 | [0.0419, 0.0502] |
| Z-test of proportions (unpooled, cc) | 0.788 | [0.780, 0.796] |       0.0459 | [0.0419, 0.0502] |
| Pearson's chi-squared (cc)           | 0.788 | [0.780, 0.796] |       0.0458 | [0.0418, 0.0501] |
| Z-test of proportions (cc)           | 0.788 | [0.780, 0.796] |       0.0458 | [0.0418, 0.0501] |

### Imbalanced ratio, balanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           | 10000 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.5 |
| effect size (in power)                | 0.035 |
| relative effect size (in power)       |  0.07 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Z-test of proportions (unpooled)     | 0.806 | [0.798, 0.814] |       0.0521 | [0.0479, 0.0567] |
| Z-test of means (unpooled)           | 0.806 | [0.798, 0.814] |       0.0521 | [0.0479, 0.0567] |
| Welch's t-test                       | 0.805 | [0.797, 0.813] |       0.0519 | [0.0477, 0.0565] |
| G-test                               | 0.805 | [0.797, 0.813] |       0.0519 | [0.0477, 0.0565] |
| Z-test of means                      | 0.805 | [0.797, 0.813] |       0.0519 | [0.0477, 0.0565] |
| Pearson's chi-squared                | 0.805 | [0.797, 0.813] |       0.0519 | [0.0477, 0.0565] |
| Z-test of proportions                | 0.805 | [0.797, 0.813] |       0.0519 | [0.0477, 0.0565] |
| Student's t-test                     | 0.805 | [0.797, 0.813] |       0.0518 | [0.0476, 0.0564] |
| Fisher                               | 0.802 | [0.794, 0.810] |       0.0504 | [0.0462, 0.0549] |
| Z-test of proportions (unpooled, cc) | 0.799 | [0.791, 0.807] |       0.0491 | [0.0450, 0.0536] |
| Pearson's chi-squared (cc)           | 0.799 | [0.791, 0.807] |       0.0486 | [0.0445, 0.0530] |
| Z-test of proportions (cc)           | 0.799 | [0.791, 0.807] |       0.0486 | [0.0445, 0.0530] |
| G-test (cc)                          | 0.799 | [0.791, 0.807] |       0.0487 | [0.0446, 0.0531] |

### Imbalanced ratio, imbalanced proportion

| parameter                             | value |
| :------------------------------------ | ----: |
| sample size                           | 10000 |
| treatment to control allocation ratio |  0.25 |
| proportion in control                 |   0.1 |
| effect size (in power)                | 0.021 |
| relative effect size (in power)       |  0.21 |

| test                                 | power |       power ci | type I error |  type I error ci |
| :----------------------------------- | ----: | -------------: | -----------: | ---------------: |
| Student's t-test                     | 0.793 | [0.785, 0.801] |       0.0526 | [0.0483, 0.0572] |
| Pearson's chi-squared                | 0.793 | [0.785, 0.801] |       0.0527 | [0.0484, 0.0573] |
| Z-test of means                      | 0.793 | [0.785, 0.801] |       0.0527 | [0.0484, 0.0573] |
| Z-test of proportions                | 0.793 | [0.785, 0.801] |       0.0527 | [0.0484, 0.0573] |
| G-test                               | 0.787 | [0.779, 0.795] |       0.0526 | [0.0483, 0.0572] |
| Fisher                               | 0.786 | [0.778, 0.794] |       0.0497 | [0.0456, 0.0542] |
| Pearson's chi-squared (cc)           | 0.782 | [0.774, 0.790] |       0.0470 | [0.0430, 0.0514] |
| Z-test of proportions (cc)           | 0.782 | [0.774, 0.790] |       0.0470 | [0.0430, 0.0514] |
| G-test (cc)                          | 0.775 | [0.766, 0.783] |       0.0481 | [0.0440, 0.0525] |
| Z-test of proportions (unpooled)     | 0.772 | [0.763, 0.780] |       0.0537 | [0.0494, 0.0583] |
| Z-test of means (unpooled)           | 0.772 | [0.763, 0.780] |       0.0537 | [0.0494, 0.0583] |
| Welch's t-test                       | 0.771 | [0.763, 0.780] |       0.0536 | [0.0493, 0.0582] |
| Z-test of proportions (unpooled, cc) | 0.760 | [0.751, 0.768] |       0.0481 | [0.0440, 0.0525] |
