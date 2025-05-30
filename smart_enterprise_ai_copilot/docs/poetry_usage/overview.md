# 🧪 Poetry 2.0.0: In-Depth Guide for Modern Python Projects

## 📅 Updated for Poetry 2.0.0+

This guide is tailored for **Poetry v2.0.0 and beyond**, which includes significant changes to environment activation, plugin architecture, and workflow.

---

## 🚀 What is Poetry?

Poetry is a modern dependency and package manager for Python that simplifies project management by handling:

* Dependency resolution
* Virtual environment creation
* Packaging and publishing
* Lock files for reproducible builds

It replaces `pip`, `requirements.txt`, `virtualenv`, `setuptools`, and even `pipenv`.

---

## 🔧 Installation

### ✔️ Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

> Confirm version:

```bash
poetry --version
```

Should output: `Poetry (version 2.x.x)`

---

## 🔄 Project Initialization

### ✔️ Create a New Poetry Project

```bash
poetry new your_project_name
```

Creates:

```
your_project_name/
├── pyproject.toml
├── your_project_name/
│   └── __init__.py
└── tests/
    └── __init__.py
```

### ✔️ Or Initialize in Existing Project

```bash
poetry init
```

Follow the prompts or use flags:

```bash
poetry init --name my-project --python "^3.12" --description "My AI Agent system"
```

---

## 🤖 Virtual Environment Management in Poetry 2.0

### ❌ `poetry shell` is NOT installed by default

Instead:

### ✔️ Use:

```bash
poetry env info --path
```

This returns the path to the environment:

```
/Users/you/Library/Caches/pypoetry/virtualenvs/project-xyz-py3.12
```

Activate manually:

```bash
source /Users/you/.../bin/activate
```

### 🐞 Optional: Restore `poetry shell` command

```bash
poetry self add poetry-plugin-shell
```

Then:

```bash
poetry shell
```

---

## 📊 Add Dependencies

### ✔️ Add runtime dependencies:

```bash
poetry add fastapi uvicorn python-dotenv
```

### ✔️ Add development tools:

```bash
poetry add --group dev black pytest mypy pylint isort
```

---

## 🎓 Installing Packages

### Install all dependencies (from lock file)

```bash
poetry install
```

### Update dependencies

```bash
poetry update
```

---

## 🚩 Exporting requirements.txt

For Docker or legacy tools:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

---

## 🚀 Build & Publish (Optional)

### Build package

```bash
poetry build
```

Outputs:

```
dist/
├── my_project-0.1.0.tar.gz
├── my_project-0.1.0-py3-none-any.whl
```

### Publish to PyPI

```bash
poetry config pypi-token.pypi <your-token>
poetry publish --build
```

---

## ⚙️ Useful Commands Summary

| Command                               | Description                                         |
| ------------------------------------- | --------------------------------------------------- |
| `poetry init`                         | Start a new project or config in an existing folder |
| `poetry add <pkg>`                    | Add runtime dependency                              |
| `poetry add --group dev <pkg>`        | Add dev-only dependency                             |
| `poetry install`                      | Install everything from lock file                   |
| `poetry update`                       | Upgrade dependencies                                |
| `poetry env info --path`              | Show env path for manual activation                 |
| `poetry self add poetry-plugin-shell` | Add back `poetry shell`                             |
| `poetry build`                        | Package project for PyPI/local distribution         |
| `poetry publish`                      | Upload your package to PyPI                         |

---

## 📆 Best Practices with Poetry 2.0

* Always commit `poetry.lock` for consistent builds.
* Use `[tool.poetry.scripts]` to define CLI entry points.
* Organize source code under a top-level package (e.g., `src/` or `project_name/`).
* For Docker, export `requirements.txt` and install with `pip install -r requirements.txt`
* Use `pyproject.toml` as the single source of truth.

---

## 🌟 Example `pyproject.toml`

```toml
[tool.poetry]
name = "smart-enterprise-ai-copilot"
version = "0.1.0"
description = "Modular AI Agent system for enterprise workflows"
authors = ["Ish Mishra <ish@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.110.0"
uvicorn = { extras = ["standard"], version = "^0.29.0" }
python-dotenv = "^1.0.1"

[tool.poetry.group.dev.dependencies]
black = "^24.0.0"
pytest = "^8.0.0"
mypy = "^1.8.0"
pylint = "^3.0.0"
isort = "^5.13.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

For full docs, visit [https://python-poetry.org/docs/](https://python-poetry.org/docs/)

Happy coding with Poetry 2.0! 🎉
