# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
source .venv/bin/activate
pip install -e ".[dev]"   # installs ipython and any other dev deps
```

## Running tests

```bash
pytest tests/ -v
pytest tests/test_foo.py::test_bar  # single test
```

## Running scripts

```bash
python scripts/my_script.py
python algorithms/my_algo.py
```

## Structure

- `scripts/` — one-off scripts (e.g. `monte_carlo_pi.py`)
- `algorithms/` — algorithm explorations
- `tests/` — pytest tests mirroring `scripts/` and `algorithms/`
- `utils.py` — shared helpers (create if/when needed)

Scripts expose a function (e.g. `estimate_pi`) importable by tests, with a `__main__` block for direct execution. Tests import from `scripts.<module>` or `algorithms.<module>`.

## Dependencies

Add runtime deps to `[project] dependencies` in `pyproject.toml`, dev-only tools to `[project.optional-dependencies] dev`.
