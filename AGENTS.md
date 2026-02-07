# AGENTS

## Project structure

- Statistical simulations:
    - `stat_tests.py`: main simulation engine and CLI entrypoint.
    - `stat_tests.toml`: runtime parameters (seed, sample sizes, alpha/power, output path).
    - `stat_tests.md`: generated results report (markdown tables).

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
