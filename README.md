# Playwright Python Test Framework

Playwright + pytest UI automation framework using Page Object Model, targeting a self-hosted clone of "the-internet" on Render.

## Project Structure

```
playwright-playground/
├── .github/workflows/      # CI pipelines
│   ├── regression.yml      # Manual trigger, runs Playwright tests
│   └── code-quality.yml    # Push/PR, pylint, black, isort checks
├── fixtures/               # Pytest fixtures (registered via pytest_plugins)
│   ├── page_fixtures.py    # Page-object fixtures
│   ├── data_fixtures.py    # Synthetic test data generators
│   └── network_fixtures.py # Mock API, viewport, offline, slow network
├── pages/                  # Page Object Model
│   ├── base_page.py        # Base page class with common functionality
│   └── [page_classes].py   # Page classes inheriting from BasePage
├── tests/                  # Test cases
│   └── [test_files].py     # Test files, one per page/feature
├── utils/                  # Utility classes
│   └── helpers.py          # Logger, TestDataGenerator, WaitHelper
├── conftest.py             # Infrastructure fixtures (browser, page, logging, timeouts)
├── pytest.ini              # Pytest settings and markers
├── pyproject.toml          # Black and isort config
├── requirements.txt        # Runtime dependencies
└── requirements-dev.txt    # Development dependencies (pylint, black, isort, pre-commit)
```

## Quick Start

Install dependencies and Playwright browsers:

```bash
pip install -r requirements.txt
playwright install
```

Run the tests:

```bash
pytest                              # Run all tests (headed by default)
pytest -m smoke                     # Only smoke tests
pytest -m "regression and not slow" # Skip slow tests
pytest --browser firefox            # Use Firefox
```

## Development Setup

Install code quality tools:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Run quality checks manually:

```bash
black .
isort .
pylint tests/ pages/ utils/ fixtures/
```

## Test Markers

| Marker | Description |
|---|---|
| `smoke` | Fast, essential tests |
| `regression` | Full regression suite |
| `ui` | UI tests |
| `slow` | Tests with long waits |

## Writing Tests

Tests use fixture-injected page objects. Never create page instances directly:

```python
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestExample:

    @pytest.fixture(autouse=True)
    def setup_pages(self, home_page, page, base_url):
        self.page = page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.mark.smoke
    def test_page_loads(self):
        self.home_page.goto_home_page(self.base_url)
        expect(self.home_page.get_page_heading()).to_be_visible()
```

## Extending the Framework

1. **New page:** Create `pages/<name>_page.py` inheriting `BasePage`, add a fixture in `fixtures/page_fixtures.py`
2. **New marker:** Declare it in `pytest.ini` first (strict markers enabled)
3. **New fixture:** Add to the appropriate file in `fixtures/` (page, data, or network)

## CI / GitHub Actions

- **`regression.yml`** - Manual trigger. Wakes up Render app, then runs Playwright tests with configurable browser and markers.
- **`code-quality.yml`** - Runs on push/PR to `main`/`develop`. Checks pylint (≥8.0), black, and isort.

## Configuration

| Setting | Location |
|---|---|
| pytest options (`--headed`, artifacts) | `pytest.ini` |
| Black/isort (line-length: 100) | `pyproject.toml` |
| Base URL | `BASE_URL` env var, fallback to `https://auto-things.onrender.com/` |
| Timeouts | 30s default (`conftest.py`) |
