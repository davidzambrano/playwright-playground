"""Pytest configuration and fixtures for Playwright testing."""

import logging
import os
from datetime import datetime
from typing import Dict, Generator

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect

from utils.helpers import Logger

# Register fixture modules from fixtures/ package
pytest_plugins = [
    "fixtures.page_fixtures",
    "fixtures.data_fixtures",
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
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "locale": "en-US",
        "timezone_id": "America/New_York",
        "extra_http_headers": {"Cache-Control": "no-cache", "Pragma": "no-cache"},
    }


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
