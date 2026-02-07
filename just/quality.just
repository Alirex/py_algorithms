# Run some fast linters
q-lint:
    ruff format .
    ruff check . --fix --unsafe-fixes
    basedpyright --level error

# Run pre-commit hooks on all files
q-pre-commit-all:
    prek run --all-files

# Check code quality: dead code, complexity, and maintainability
q-metrics:
    vulture . --min-confidence 80 --exclude .venv,build,dist,docs,scripts,tests
    radon cc . -a -nb
    radon mi . -nb

# Full quality check: format, lint, type check, and metrics
q-quality: q-pre-commit-all q-metrics
