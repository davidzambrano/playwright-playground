"""Page-object fixtures for all page classes."""

import pytest
from playwright.sync_api import Page

from pages.ab_testing_page import ABTestingPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage
from pages.broken_images_page import BrokenImagesPage
from pages.challenging_dom_page import ChallengingDomPage
from pages.checkboxes_page import CheckboxesPage
from pages.dropdown_page import DropdownPage
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


@pytest.fixture(scope="function")
def ab_testing_page(page: Page) -> ABTestingPage:
    """Fixture for ABTestingPage object."""
    return ABTestingPage(page)


# Broken Images page fixture
@pytest.fixture(scope="function")
def broken_images_page(page: Page) -> BrokenImagesPage:
    """Fixture for BrokenImagesPage object."""
    return BrokenImagesPage(page)


@pytest.fixture(scope="function")
def challenging_dom_page(page: Page) -> ChallengingDomPage:
    """Fixture for ChallengingDomPage object."""
    return ChallengingDomPage(page)


@pytest.fixture(scope="function")
def checkboxes_page(page: Page) -> CheckboxesPage:
    """Fixture for CheckboxesPage object."""
    return CheckboxesPage(page)


@pytest.fixture(scope="function")
def dropdown_page(page: Page) -> DropdownPage:
    """Fixture for DropdownPage object."""
    return DropdownPage(page)
