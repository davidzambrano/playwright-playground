# Playwright Python Test Framework

A Playwright + pytest UI automation framework using Page Object Model, targeting a self-hosted clone of "the-internet" on Render.

## Project Structure

```
playwright-playground/
├── .github/workflows/      # CI pipelines
│   ├── regression.yml      # Manual trigger, runs Playwright tests
│   ├── code-quality.yml    # Push/PR, pylint, black, isort checks
│   └── sonarcloud.yml      # Push/PR to main, SonarCloud analysis
├── fixtures/               # Pytest fixtures (registered via pytest_plugins)
│   ├── page_fixtures.py    # Page-object fixtures
│   └── network_fixtures.py # Mock API, viewport, offline, slow network
├── pages/                  # Page Object Model
│   ├── base_page.py        # Base page class with common functionality
│   └── [page_classes].py   # Page classes inheriting from BasePage
├── tests/                  # Test cases
│   └── [test_files].py     # Test files, one per page/feature
├── utils/                  # Utility classes
│   └── helpers.py          # Logger
├── conftest.py             # Infrastructure fixtures (browser, page, logging, timeouts)
├── pytest.ini              # Pytest settings and markers
├── pyproject.toml          # Black and isort config
├── requirements.txt        # Runtime dependencies (source of truth)
├── requirements.lock       # Locked runtime dependencies with SHA256 hashes
├── requirements-dev.txt    # Development dependencies (pylint, black, isort, pre-commit)
└── requirements-dev.lock   # Locked dev dependencies with SHA256 hashes
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

## Dependency Lock Files

This project uses `pip-tools` to generate lock files with SHA256 hashes for all dependencies (including transitive ones). CI installs from the lock files using `pip install --require-hashes` for secure, reproducible builds.

When you change `requirements.txt` or `requirements-dev.txt`, regenerate the corresponding lock file:

```bash
pip-compile requirements.txt --output-file requirements.lock --generate-hashes --strip-extras
pip-compile requirements-dev.txt --output-file requirements-dev.lock --generate-hashes --strip-extras
```

Commit both the source file and the regenerated lock file together.

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
| `pipelinedebug` | Temporary marker for debugging in CI pipeline only |

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
3. **New fixture:** Add to the appropriate file in `fixtures/` (page or network)

## CI / GitHub Actions

- **`regression.yml`** - Manual trigger. Wakes up Render app, then runs Playwright tests with configurable browser and markers. Tests are sharded across 4 parallel runners for faster execution. Use `pipelinedebug` marker to run only specific tests in CI for quick debugging. Publishes an Allure report per branch (see [Allure Reporting](#allure-reporting)).
- **`code-quality.yml`** - Runs on push/PR to `main`/`develop`. Checks pylint (≥8.0), black, and isort.
- **`sonarcloud.yml`** - Runs on push/PR to `main`. Runs tests in 4 parallel shards, combines coverage, and performs SonarCloud analysis. Requires `SONAR_TOKEN` secret.

### Test Sharding

The regression workflow uses test sharding to parallelize test execution across 4 GitHub Actions runners:

- **Sharding library**: `pytest-shard` divides tests into 4 equal groups
- **Matrix strategy**: Each shard runs on a separate Ubuntu runner
- **Isolation**: Each shard has its own test results directory and Allure results
- **Fail-fast disabled**: All shards complete even if one fails
- **Artifacts**: Each shard uploads its own results (reports, test-results, logs)

This reduces total execution time by approximately 75% compared to running all tests sequentially.

## Allure Reporting

Test results are recorded with [`allure-pytest`](https://pypi.org/project/allure-pytest/). Raw results are written to `reports/allure-results` (configured via `--alluredir` in `pytest.ini`).

### Viewing a report locally

```bash
pytest                                          # generates reports/allure-results
allure serve reports/allure-results             # builds and opens the report in your browser
```

`allure serve` requires the [Allure commandline](https://allurereport.org/docs/install/) (`npm install -g allure-commandline`, or via `scoop`/`brew`).

To generate a persistent report folder instead of a temporary one:

```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

### CI reports

The `regression.yml` `publish-report` job merges Allure results from all 4 shards, generates a single report, and publishes it to the `gh-pages` branch under a folder named after the triggering branch (e.g. `develop/`, `main/`), so different branches keep independent reports and trend history. The report link is posted to the workflow run's Job Summary. A downloadable `allure-report-<branch>` artifact is also uploaded for each run.

The latest `main` branch report is available at [https://davidzambrano.github.io/playwright-playground/main/](https://davidzambrano.github.io/playwright-playground/main/).

## Configuration

| Setting | Location |
|---|---|
| pytest options (`--headed`, artifacts) | `pytest.ini` |
| Black/isort (line-length: 100) | `pyproject.toml` |
| Base URL | `BASE_URL` env var, fallback to `https://auto-things.onrender.com/` |
| Timeouts | 30s default (`conftest.py`) |
