# Benchmark

| parameter                 | value |
| :------------------------ | ----: |
| number of repeats         |    10 |
| number of runs per repeat |    10 |

Execution time, ms

| test           | small sample (100) | medium sample (1000) | large sample (10000) |
| :------------- | -----------------: | -------------------: | -------------------: |
| barnard        |               5.98 |                  589 |                    - |
| boschloo       |               6.33 |                 2148 |                    - |
| fisher         |              0.258 |                0.379 |                0.766 |
| log-likelihood |              0.121 |                0.128 |                0.119 |
| pearson        |              0.120 |                0.121 |                0.119 |
| norm           |              0.457 |                0.453 |                0.479 |
| mean z-test    |              0.507 |                0.493 |                0.505 |
| mean t-test    |              0.500 |                0.501 |                0.488 |
