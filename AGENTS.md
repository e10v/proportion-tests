# AGENTS

## About the codebase

- `src/proportion_tests/`: project code:
    - `src/proportion_tests/simulation.py`: A/A and power simulations.
    - `src/proportion_tests/benchmark.py`: execution time benchmarks.
    - `src/proportion_tests/config.py`: config loader.
    - `src/proportion_tests/data.py`: data generator.
    - `src/proportion_tests/utils.py`: rendering and other helpers.
- Configs are defined in `pyproject.toml` in the `[tool.proportion_tests]` table.
- Scripts, that are supposed to run from the project root:
    - `uv run simulation`: simulates A/A and power experiment and creates a report in `reports/simulation.md`.
    - `uv run benchmark`: run test analysis many times to estimate execution time and creates a report in `reports/benchmark.md`.
    - Under any circumstances, never run these scripts yourself. They are time and resource expensive.

## Code style

- Follow PEP 8.
- Follow Google Python Style Guide.
- Exceptions:
    - Max line length: 88.
    - Use `uv run ruff check` for linting instead of `pylint`.
    - Use `uv run ty check` for type checking instead of `pytype`.
- When guides disagree, follow project tooling (Ruff/ty) and existing local conventions in this repo.
- Imports must satisfy Ruff isort rules (sorted within sections; two blank lines after imports).
- Type annotations are required for all modules including tests and internal tooling; keep type hints accurate and narrow.
- Using `cast` is usually discouraged: prefer correct annotations; if needed, use suppression (`# ty: ignore`) over `cast`.
- Prefer pure functions and deterministic numeric behavior.
- Tests are not required.

## Docs style

- When editing readme, follow the Microsoft Writing Style Guide and Google developer documentation style guide.
- Docstrings are not required.

## Code checking

- Checks for code changes:
    - Linting: `uv run ruff check`
    - Type checking: `uv run ty check`
- Run them after creating or updating Python modules; fix errors.
- Do not run a code formatter; `uv run ruff check --fix` is acceptable for lint autofixes.

## Docs checking

- Checks for docs changes:
    - Markdown lint: `markdownlint-cli2 "*.md"`
- Run them after creating or updating markdown files; fix errors.

## Code versioning

- Develop only in the `dev` branch, never merge into `main`; leave all merges to me.
- Make atomic commits.
- Follow the Conventional Commits standard in commit messages but skip optional scope after type.
