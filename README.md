# Image Training

An image generation tool to create a training set of images for use in machine learning.

![Tests](https://github.com/Teffluvium/imageTraining_py/actions/workflows/tests.yml/badge.svg)

## Development

Use `uv` for local tooling:

```bash
uv venv
uv pip install -r requirements_dev.txt -e .
uv run pytest
uv run mypy src
uv run ruff check src tests
uv run ruff format --check src tests
```
