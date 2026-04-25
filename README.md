# Playwright Python Test Framework

A scalable, maintainable UI and API test automation framework built with **Playwright for Python** and **pytest**. Implements the Page Object Model (POM) and Flow Model patterns, with full CI/CD integration via GitHub Actions.

---

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development Setup](#development-setup)
- [Writing Tests](#writing-tests)
  - [Page Objects](#page-objects)
  - [Test Files](#test-files)
  - [Fixtures](#fixtures)
  - [Markers](#markers)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [CI/CD](#cicd)
- [Reporting](#reporting)
- [Extending the Framework](#extending-the-framework)
- [Code Quality](#code-quality)

---

## Architecture Overview

The framework is organized into three layers, following the TAF layering principle:

```
┌─────────────────────────────────────┐
│           Test Scripts              │  tests/
│  (test logic, assertions, markers)  │
├─────────────────────────────────────┤
│          Business Logic             │  pages/ + fixtures/
│  (page objects, flows, helpers)     │
├─────────────────────────────────────┤
│          Core Libraries             │  utils/ + conftest.py
│  (base page, config, shared setup)  │
└─────────────────────────────────────┘
```

**Design patterns used:**
- **Page Object Model** — isolates locators and page interactions from test logic
- **Flow Model** — composes multi-step user journeys from page object actions
- **Facade** — `BasePage` hides low-level Playwright API details from page classes
- **Fixtures** — pytest fixtures manage setup/teardown at the right scope (session, module, function)

---

## Project Structure

```
playwright-playground/
├── .github/
│   └── workflows/
│       ├── regression.yml       # On-demand regression runs with configurable markers
│       └── code-quality.yml     # Lint + format checks on push/PR
├── fixtures/
│   ├── __init__.py
│   └── custom_fixtures.py       # Reusable domain-specific fixtures
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # BasePage: navigation, waits, shared actions
│   ├── home_page.py             # Example: HomePage(BasePage)
│   └── login_page.py            # Example: LoginPage(BasePage)
├── tests/
│   ├── __init__.py
│   ├── test_home.py
│   └── test_login.py
├── utils/
│   ├── __init__.py
│   └── helpers.py               # Stateless utility functions
├── conftest.py                  # Root fixtures: browser, page, base_url
├── pytest.ini                   # Markers, log settings, default options
├── pyproject.toml               # Black + isort config (line-length: 100)
├── .pylintrc                    # Pylint rules
├── .pre-commit-config.yaml      # Pre-commit hooks: black, isort, pylint
├── requirements.txt             # Runtime dependencies
├── requirements-dev.txt         # Dev dependencies: linters, pre-commit
├── .env.example                 # Environment variable template
└── logs/                        # Test execution logs (gitignored)
```

---

## Prerequisites

- Python 3.11+
- pip
- A Chromium-compatible browser (installed via `playwright install`)

---

## Quick Start

```bash
# 1. Clone and install dependencies
pip install -r requirements.txt
playwright install

# 2. Configure environment
cp .env.example .env
# Edit .env — set BASE_URL and any credentials

# 3. Run all tests
pytest

# 4. Run with options
pytest --browser firefox          # Use Firefox instead of Chromium
pytest --headed                   # Run with visible browser window
pytest -m smoke                   # Only smoke-tagged tests
pytest -k "login"                 # Tests matching keyword
pytest --html=report.html         # Generate HTML report
```

---

## Development Setup

```bash
# Install dev dependencies (linters, pre-commit)
pip install -r requirements-dev.txt

# Install pre-commit hooks (runs black, isort, pylint before each commit)
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

---

## Writing Tests

### Page Objects

All page classes inherit from `BasePage`, which wraps common Playwright operations. Page objects own locators and expose business-meaningful actions — never raw selectors.

```python
# pages/login_page.py
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Locators are defined here, not in tests
        self._username_input = page.get_by_label("Username")
        self._password_input = page.get_by_label("Password")
        self._submit_button = page.get_by_role("button", name="Log in")
        self._error_message = page.get_by_role("alert")

    def login(self, username: str, password: str) -> None:
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._submit_button.click()

    def get_error_message(self) -> str:
        return self._error_message.inner_text()
```

> **Anti-pattern to avoid:** Never put `page.locator(...)` calls or `page.click()` calls directly inside test functions. That breaks the abstraction and makes locator changes expensive.

### Test Files

Tests call page object methods and assert on outcomes. No selectors, no `page.locator()` in test files.

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page, base_url):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.login_page.navigate(base_url + "/login")

    def test_valid_login_redirects_to_home(self, valid_credentials):
        self.login_page.login(**valid_credentials)
        assert self.home_page.is_loaded(), "Expected redirect to home page after login"

    def test_invalid_login_shows_error(self):
        self.login_page.login(username="bad_user", password="wrong")
        assert "Invalid credentials" in self.login_page.get_error_message()
```

### Fixtures

Shared fixtures live in `conftest.py`. Domain-specific fixtures belong in `fixtures/custom_fixtures.py` and are imported via `conftest.py`.

```python
# conftest.py
import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ["BASE_URL"]


@pytest.fixture(scope="session")
def valid_credentials() -> dict:
    return {
        "username": os.environ["TEST_USERNAME"],
        "password": os.environ["TEST_PASSWORD"],
    }
```

> **Note:** Use `scope="session"` for expensive setup (auth tokens, DB connections). Use `scope="function"` (the default) when tests must be fully isolated.

### Markers

Available markers are declared in `pytest.ini`:

| Marker       | Purpose                                      |
|--------------|----------------------------------------------|
| `smoke`      | Fast, critical-path tests — run on every build |
| `regression` | Full regression suite                        |
| `slow`       | Long-running tests excluded from quick runs  |
| `ui`         | Browser-based tests                          |
| `api`        | API-level tests (no browser)                 |

```python
@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_loads(self):
    ...
```

---

## Configuration

| File              | Purpose                                                         |
|-------------------|-----------------------------------------------------------------|
| `pytest.ini`      | Default CLI options, markers, log level, test paths            |
| `pyproject.toml`  | Black (line-length: 100) and isort configuration               |
| `.pylintrc`       | Pylint rules and disabled checks                               |
| `.env`            | Runtime secrets and environment config — **never commit this** |
| `.env.example`    | Template showing required variables (no values)                |

**Required environment variables** (see `.env.example`):

```bash
BASE_URL=https://your-app.example.com
TEST_USERNAME=testuser@example.com
TEST_PASSWORD=supersecret
```

---

## Running Tests

```bash
# By browser
pytest --browser chromium        # default
pytest --browser firefox
pytest --browser webkit

# By marker
pytest -m smoke
pytest -m "regression and not slow"
pytest -m api                    # API tests only — no browser needed

# Headed / headless
pytest --headed                  # Show browser window
pytest --headed=false            # Headless (CI default)

# Parallel execution (requires pytest-xdist)
pytest -n 4                      # 4 parallel workers

# Output and reporting
pytest -v                        # Verbose output
pytest --html=report.html --self-contained-html
pytest --tb=short                # Shorter tracebacks

# Rerun failures (requires pytest-rerunfailures)
pytest --reruns 2 --reruns-delay 1
```

---

## CI/CD

### Regression Workflow (`.github/workflows/regression.yml`)

Triggered manually via the GitHub Actions UI (`workflow_dispatch`).

**Inputs:**

| Input              | Type     | Options                                           | Default                              |
|--------------------|----------|---------------------------------------------------|--------------------------------------|
| `test_environment` | `string` | Any valid URL                                     | `https://auto-things.onrender.com/`  |
| `test_markers`     | `choice` | `all`, `smoke`, `regression`, `slow`, `api`, `ui` | `all`                                |
| `browser`          | `choice` | `chromium`, `firefox`, `webkit`                   | `chromium`                           |

**Jobs:**

`wake-app` → `run-tests`

The workflow has two sequential jobs. `wake-app` pings the target URL up to 5 times (30s apart) and fails the pipeline immediately if the app never responds with HTTP 200 — this prevents tests from running against a down environment. `run-tests` only starts once `wake-app` succeeds.

**Artifacts:**

On completion (pass or fail), a `playwright-results` artifact is uploaded and retained for 7 days. It contains:

```
reports/          # HTML report (pytest-html)
test-results/     # Playwright screenshots and videos on failure
logs/             # Execution logs
```

To download: **Actions → your run → Artifacts → playwright-results**

To view a trace file locally after downloading:
```bash
playwright show-trace test-results/<trace>.zip
```

### Code Quality Workflow (`.github/workflows/code-quality.yml`)

Runs automatically on every push and pull request to `main`, `master`, and `develop`.

Checks:
- **Pylint** — static analysis and code smell detection
- **Black** — code formatting (`--check` mode, no writes)
- **isort** — import order (`--check-only` mode)

All three must pass before a PR can be merged.

---

## Reporting

| Output         | Location                          | When generated        |
|----------------|-----------------------------------|-----------------------|
| HTML report    | `reports/playwright-report.html`  | Every run             |
| Screenshots    | `test-results/`                   | On test failure       |
| Videos         | `test-results/`                   | On test failure       |
| Trace files    | `test-results/`                   | On test failure       |
| Execution logs | `logs/`                           | Every run             |

To view a Playwright trace file locally:

```bash
playwright show-trace test-results/<trace>.zip
```

---

## Extending the Framework

### Add a new page

```python
# pages/checkout_page.py
from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self._confirm_button = page.get_by_role("button", name="Confirm order")

    def confirm_order(self) -> None:
        self._confirm_button.click()
```

### Add a new fixture

```python
# fixtures/custom_fixtures.py
import pytest


@pytest.fixture(scope="function")
def logged_in_user(page, base_url, valid_credentials):
    """Returns a page already authenticated as a standard user."""
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate(base_url + "/login")
    login.login(**valid_credentials)
    return page
```

### Add a utility function

Utilities in `utils/helpers.py` should be **stateless pure functions** — no page or fixture references.

```python
# utils/helpers.py
import re


def extract_order_id(text: str) -> str | None:
    """Extract order ID from confirmation text like 'Order #ORD-12345 confirmed'."""
    match = re.search(r"ORD-\d+", text)
    return match.group(0) if match else None
```

---

## Code Quality

This project enforces consistent style through automated tooling:

```bash
black .                          # Auto-format all files
isort .                          # Sort imports
pylint tests/ pages/ utils/      # Static analysis
pre-commit run --all-files       # Run all checks at once
```

Line length is set to **100 characters** across Black, isort, and Pylint.
