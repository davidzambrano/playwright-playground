"""Pytest configuration and fixtures for Playwright testing."""

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Generator

import pytest
from allure_commons.types import LabelType
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from utils.helpers import Logger

# Register fixture modules from fixtures/ package
pytest_plugins = [
    "fixtures.page_fixtures",
    "fixtures.network_fixtures",
]

load_dotenv()

# Set default expect timeout to 30 seconds
expect.set_options(timeout=30000)


def pytest_configure(config):
    """Configure pytest to capture logging output."""
    config.option.log_cli_level = "INFO"


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """Configure logging for the test session."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/test_execution_{timestamp}.log"
    Logger.setup_logger(
        name="",
        log_file=log_file,
        level=logging.DEBUG,
        file_level=logging.DEBUG,
        console_level=logging.INFO,
    )
    logging.info("Logging configured for test session")


@pytest.fixture(scope="function", autouse=True)
def log_test_info(request):
    """Log test start and end for HTML report."""
    test_name = request.node.name
    logging.info("=" * 80)
    logging.info("TEST START: %s", test_name)
    yield
    logging.info("TEST END: %s", test_name)
    logging.info("=" * 80)


@pytest.fixture(scope="session")
def browser_context_args(
    browser_context_args: Dict,
) -> Dict:  # pylint: disable=redefined-outer-name
    """Configure browser context with default settings."""
    return {
        **browser_context_args,
        "no_viewport": True,
        "ignore_https_errors": True,
        "locale": "en-US",
        "timezone_id": "America/New_York",
        "extra_http_headers": {"Cache-Control": "no-cache", "Pragma": "no-cache"},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(
    browser_type_launch_args: Dict,
    browser_name: str,
) -> Dict:  # pylint: disable=redefined-outer-name
    """Configure browser launch args so the OS window matches the CSS viewport.

    --start-maximized is only supported by Chromium, not Firefox or WebKit.
    """
    launch_args = {**browser_type_launch_args}

    # Only add Chromium-specific args for Chromium browser
    if browser_name == "chromium":
        launch_args["args"] = ["--start-maximized"]

    return launch_args


@pytest.fixture(scope="function")
def page(
    page: Page,
) -> Generator[Page, None, None]:  # pylint: disable=redefined-outer-name
    """Page fixture with automatic cleanup and error handling."""
    # Set default timeout to 30 seconds
    page.set_default_timeout(30000)

    # Add error handling
    def handle_error(error):
        logging.error("Page error: %s", error)

    page.on("pageerror", handle_error)

    yield page


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the application under test."""
    return os.getenv("BASE_URL", "https://auto-things.onrender.com/")


# ---------------------------------------------------------------------------
# Allure report labeling
# ---------------------------------------------------------------------------
# allure-pytest auto-derives the "Suites" facet (parentSuite/suite/subSuite)
# from the pytest node id, but the "Features" facet is left empty by default.
# Each test module in this repo maps to one the-internet page, so both the
# "feature" label and the "Suites" hierarchy are derived here and applied to
# every test in one place, avoiding per-test @allure decorators.
# Result: Suites = UI > Smoke|Regression > <Page>, Behaviors = <Page feature>.
# Label hierarchy reference: https://allurereport.org/docs/how-it-works/
_ALLURE_FEATURE_OVERRIDES = {
    "ab_testing": "A/B Testing",
    "add_remove_elements": "Add/Remove Elements",
    "challenging_dom": "Challenging DOM",
    "drag_and_drop": "Drag and Drop",
    "iframe": "iFrame",
    "javascript_alerts": "JavaScript Alerts",
    "javascript_onload_error": "JavaScript onload event error",
}


def _allure_feature_for_item(item) -> str:
    """Build a human-friendly Allure feature name from the test module."""
    module_stem = Path(item.nodeid.split("::", 1)[0]).stem  # e.g. test_dropdown_page
    key = module_stem.removeprefix("test_").removesuffix("_page")  # e.g. dropdown
    return _ALLURE_FEATURE_OVERRIDES.get(key, key.replace("_", " ").title())


def _allure_suite_for_item(item) -> str:
    """Use the Smoke marker to pick the Allure suite; default to Regression."""
    return "Smoke" if "smoke" in item.keywords else "Regression"


def pytest_collection_modifyitems(items):
    """Auto-tag every test with Allure feature + suite labels.

    Feature comes from the test module (the page under test); the Suites
    hierarchy is fixed to UI > Smoke|Regression > <Page feature>, so every
    test lands under a named suite instead of the bare `tests` node.
    """
    for item in items:
        feature = _allure_feature_for_item(item)
        suite = _allure_suite_for_item(item)
        # Equivalent to applying @allure.feature/suite decorators from one place.
        item.add_marker(pytest.mark.allure_label(feature, label_type=LabelType.FEATURE))
        item.add_marker(pytest.mark.allure_label("UI", label_type=LabelType.PARENT_SUITE))
        item.add_marker(pytest.mark.allure_label(suite, label_type=LabelType.SUITE))
        item.add_marker(pytest.mark.allure_label(feature, label_type=LabelType.SUB_SUITE))
