"""Page-object fixtures for all page classes."""

import pytest
from playwright.sync_api import Page

from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage
from pages.home_page import HomePage
from pages.slow_resources_page import SlowResourcesPage


@pytest.fixture(scope="function")
def home_page(page: Page) -> HomePage:
    """Fixture for HomePage object."""
    return HomePage(page)


@pytest.fixture(scope="function")
def slow_resources_page(page: Page) -> SlowResourcesPage:
    """Fixture for SlowResourcesPage object."""
    return SlowResourcesPage(page)


@pytest.fixture(scope="function")
def add_remove_elements_page(page: Page) -> AddRemoveElementsPage:
    """Fixture for AddRemoveElementsPage object."""
    return AddRemoveElementsPage(page)


@pytest.fixture(scope="function")
def basic_auth_page(page: Page) -> BasicAuthPage:
    """Fixture for BasicAuthPage object."""
    return BasicAuthPage(page)
