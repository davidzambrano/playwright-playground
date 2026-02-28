# Playwright Python Test Framework

This is a Playwright test framework for Python that uses the Page Object Model pattern for maintainable and professional testing.

## Project Structure

```
playwright-playground/
├── fixtures/               # Custom pytest fixtures
│   ├── __init__.py
│   └── custom_fixtures.py  # Custom test fixtures
├── pages/                  # Page Object Model
│   ├── __init__.py
│   ├── base_page.py       # Base page class with common functionality
│   └── [page_classes].py  # Page classes inheriting from BasePage (e.g., home_page.py, login_page.py)
├── tests/                  # Test cases
│   ├── __init__.py
│   └── [test_files].py     # Test files (e.g., test_home.py, test_login.py)
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── helpers.py         # Helper functions
├── conftest.py            # Pytest configuration and fixtures
├── pytest.ini             # Pytest settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Quick Start

To get started, install the dependencies and set up your environment.

First, install the required packages:

```bash
pip install -r requirements.txt
playwright install
```

Then, copy the environment file and configure it:

```bash
cp .env.example .env
# Edit .env with your settings
```

Now you can run the tests:

```bash
pytest  # Run all tests
pytest --browser firefox  # Use Firefox
pytest --headed=false  # Headless mode
pytest -m smoke  # Only smoke tests
```

## Key Features

The framework uses the Page Object Model for clean separation between page logic and test logic. The BasePage provides common methods like navigation and waiting, while specific pages like HomePage handle their own elements.

Tests are organized with fixtures for setup, and include markers for different test types. It supports parametrization for data-driven tests and generates reports with screenshots on failures.

Utilities include helpers for common tasks.

## Writing Tests

Here's a basic test example:

```python
import pytest
from pages.home_page import HomePage

class TestHome:
    @pytest.fixture(autouse=True)
    def setup(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.home_page = HomePage(page)
    
    def test_home_page_loads(self):
        self.home_page.goto_home_page(self.base_url)
        # Assertions here
```

You can use custom fixtures and parametrize tests as needed.

## Configuration

Configuration is handled through pytest.ini for test settings, and test data can be managed in the helpers if needed. Environment variables are used for sensitive data.

## Reporting

Tests generate screenshots and traces on failure.

## Best Practices

The framework follows Page Object Model, uses fixtures for setup, manages configuration securely, and provides good error handling.

## Extending the Framework

To add new pages, create a class in pages/ inheriting from BasePage.

Add new fixtures in fixtures/custom_fixtures.py.

Add utilities in utils/helpers.py.
