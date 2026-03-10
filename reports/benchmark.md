# Benchmark

| parameter                 | value |
| :------------------------ | ----: |
| number of repeats         |    10 |
| number of runs per repeat |    10 |

Execution time, ms

| test                  | small sample (100) | medium sample (1000) | large sample (10000) |
| :-------------------- | -----------------: | -------------------: | -------------------: |
| Barnard               |               4.46 |                  583 |                    - |
| Boschloo              |               6.16 |                 1842 |                    - |
| Fisher                |              0.251 |                0.361 |                0.762 |
| G-test                |              0.120 |                0.122 |                0.135 |
| Pearson's chi-squared |              0.123 |                0.119 |                0.120 |
| Z-test of proportions |              0.453 |                0.457 |                0.444 |
| Z-test of means       |              0.483 |                0.508 |                0.488 |
| Student's t-test      |              0.489 |                0.483 |                0.488 |
