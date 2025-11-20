# Python algorithms

---

---

# Dev

## Dev deployment

### Install uv

Install uv for development.

Use command from the [previous section](#uv-install-or-update).

### Ruff install or update

Install ruff for manual linting, if needed.

https://docs.astral.sh/ruff/installation/

```bash
if ! command -v ruff &> /dev/null; then
    uv tool install ruff
else
    uv tool upgrade ruff
fi

ruff --version
```

### Install pre-commit

Needed for automatic linting.

```shell
if ! command -v pre-commit &> /dev/null; then
    uv tool install pre-commit
else
    uv tool upgrade pre-commit
fi

pre-commit --version
```

### Clone the repository

Make this if you haven't done it yet.

### Create venv

Make this in the project directory.

```bash
uv sync --all-packages
```

It must be used automatically in the IDE (PyCharm, VSCode).

It will be used automatically without manual activation with command like `uv run something`.

### Register pre-commit hooks

Make this after cloning the repository.

```shell
pre-commit install
```

Make this each time after cloning the repository.

Don't need to do it after changing the hooks, commit or pull.

### Run pre-commit hooks

If needed, run them manually.

```shell
pre-commit run --all-files
```

Useful after changing the hooks. Or just to check if everything is fine.

### Check code quality

```shell
uv run poe quality
```

---

## Extra

- Why is the `.idea` folder is partially stored in the repository?
  - [read (UKR)](https://github.com/Alirex/notes/blob/main/notes/ignore_or_not_ide_config/ukr.md)
- Why `py.typed`?
  - [mypy (ENG)](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages)
  - [typing (ENG)](https://typing.python.org/en/latest/spec/distributing.html#packaging-type-information)

### Create a new project

In case, if you need to create a new project with `src-layout` instead of default, created by PyCharm,
use the following command inside the project directory:

```shell
rm --recursive --force src pyproject.toml &&\
uv init --package --vcs none &&\
touch src/$(basename $PWD | tr '-' '_')/py.typed &&\
uv sync
```
