"""Page-object fixtures for all page classes."""

import pytest
from playwright.sync_api import Page

from pages.ab_testing_page import ABTestingPage
from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.basic_auth_page import BasicAuthPage
from pages.broken_images_page import BrokenImagesPage
from pages.challenging_dom_page import ChallengingDomPage
from pages.checkboxes_page import CheckboxesPage
from pages.context_menu_page import ContextMenuPage
from pages.disappearing_elements_page import DisappearingElementsPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.dropdown_page import DropdownPage
from pages.dynamic_content_page import DynamicContentPage
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.entry_ad_page import EntryAdPage
from pages.exit_intent_page import ExitIntentPage
from pages.file_download_page import FileDownloadPage
from pages.file_upload_page import FileUploadPage
from pages.floating_menu_page import FloatingMenuPage
from pages.geolocation_page import GeolocationPage
from pages.home_page import HomePage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoversPage
from pages.iframe_page import IFramePage
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.inputs_page import InputsPage
from pages.javascript_alerts_page import JavaScriptAlertsPage
from pages.javascript_onload_error_page import JavascriptOnloadErrorPage
from pages.key_presses_page import KeyPressesPage
from pages.large_deep_dom_page import LargeDeepDomPage
from pages.menus_page import MenusPage
from pages.multiple_windows_page import MultipleWindowsPage
from pages.notification_messages_page import NotificationMessagesPage
from pages.redirect_link_page import RedirectLinkPage
from pages.secure_file_download_page import SecureFileDownloadPage
from pages.slow_resources_page import SlowResourcesPage
from pages.stale_element_page import StaleElementPage


@pytest.fixture
def home_page(page: Page) -> HomePage:
    """Fixture for HomePage object."""
    return HomePage(page)


@pytest.fixture
def slow_resources_page(page: Page) -> SlowResourcesPage:
    """Fixture for SlowResourcesPage object."""
    return SlowResourcesPage(page)


@pytest.fixture
def add_remove_elements_page(page: Page) -> AddRemoveElementsPage:
    """Fixture for AddRemoveElementsPage object."""
    return AddRemoveElementsPage(page)


@pytest.fixture
def basic_auth_page(page: Page) -> BasicAuthPage:
    """Fixture for BasicAuthPage object."""
    return BasicAuthPage(page)


@pytest.fixture
def ab_testing_page(page: Page) -> ABTestingPage:
    """Fixture for ABTestingPage object."""
    return ABTestingPage(page)


# Broken Images page fixture
@pytest.fixture
def broken_images_page(page: Page) -> BrokenImagesPage:
    """Fixture for BrokenImagesPage object."""
    return BrokenImagesPage(page)


@pytest.fixture
def challenging_dom_page(page: Page) -> ChallengingDomPage:
    """Fixture for ChallengingDomPage object."""
    return ChallengingDomPage(page)


@pytest.fixture
def checkboxes_page(page: Page) -> CheckboxesPage:
    """Fixture for CheckboxesPage object."""
    return CheckboxesPage(page)


@pytest.fixture
def dropdown_page(page: Page) -> DropdownPage:
    """Fixture for DropdownPage object."""
    return DropdownPage(page)


@pytest.fixture
def context_menu_page(page: Page) -> ContextMenuPage:
    """Fixture for ContextMenuPage object."""
    return ContextMenuPage(page)


@pytest.fixture
def dynamic_controls_page(page: Page) -> DynamicControlsPage:
    """Fixture for DynamicControlsPage object."""
    return DynamicControlsPage(page)


@pytest.fixture
def hovers_page(page: Page) -> HoversPage:
    """Fixture for HoversPage object."""
    return HoversPage(page)


@pytest.fixture
def javascript_alerts_page(page: Page) -> JavaScriptAlertsPage:
    """Fixture for JavaScriptAlertsPage object."""
    return JavaScriptAlertsPage(page)


@pytest.fixture
def javascript_onload_error_page(page: Page) -> JavascriptOnloadErrorPage:
    """Fixture for JavascriptOnloadErrorPage object."""
    return JavascriptOnloadErrorPage(page)


@pytest.fixture
def disappearing_elements_page(page: Page) -> DisappearingElementsPage:
    """Fixture for DisappearingElementsPage object."""
    return DisappearingElementsPage(page)


@pytest.fixture
def key_presses_page(page: Page) -> KeyPressesPage:
    """Fixture for KeyPressesPage object."""
    return KeyPressesPage(page)


@pytest.fixture
def drag_and_drop_page(page: Page) -> DragAndDropPage:
    """Fixture for DragAndDropPage object."""
    return DragAndDropPage(page)


@pytest.fixture
def dynamic_loading_page(page: Page) -> DynamicLoadingPage:
    """Fixture for DynamicLoadingPage object."""
    return DynamicLoadingPage(page)


@pytest.fixture
def dynamic_content_page(page: Page) -> DynamicContentPage:
    """Fixture for DynamicContentPage object."""
    return DynamicContentPage(page)


@pytest.fixture
def stale_element_page(page: Page) -> StaleElementPage:
    """Fixture for StaleElementPage object."""
    return StaleElementPage(page)


@pytest.fixture
def entry_ad_page(page: Page) -> EntryAdPage:
    """Fixture for EntryAdPage object."""
    return EntryAdPage(page)


@pytest.fixture
def exit_intent_page(page: Page) -> ExitIntentPage:
    """Fixture for ExitIntentPage object."""
    return ExitIntentPage(page)


@pytest.fixture
def file_download_page(page: Page) -> FileDownloadPage:
    """Fixture for FileDownloadPage object."""
    return FileDownloadPage(page)


@pytest.fixture
def file_upload_page(page: Page) -> FileUploadPage:
    """Fixture for FileUploadPage object."""
    return FileUploadPage(page)


@pytest.fixture
def floating_menu_page(page: Page) -> FloatingMenuPage:
    """Fixture for FloatingMenuPage object."""
    return FloatingMenuPage(page)


@pytest.fixture
def geolocation_page(page: Page) -> GeolocationPage:
    """Fixture for GeolocationPage object."""
    return GeolocationPage(page)


@pytest.fixture
def horizontal_slider_page(page: Page) -> HorizontalSliderPage:
    """Fixture for HorizontalSliderPage object."""
    return HorizontalSliderPage(page)


@pytest.fixture
def large_deep_dom_page(page: Page) -> LargeDeepDomPage:
    """Fixture for LargeDeepDomPage object."""
    return LargeDeepDomPage(page)


@pytest.fixture
def iframe_page(page: Page) -> IFramePage:
    """Fixture for IFramePage object."""
    return IFramePage(page)


@pytest.fixture
def infinite_scroll_page(page: Page) -> InfiniteScrollPage:
    """Fixture for InfiniteScrollPage object."""
    return InfiniteScrollPage(page)


@pytest.fixture
def inputs_page(page: Page) -> InputsPage:
    """Fixture for InputsPage object."""
    return InputsPage(page)


@pytest.fixture
def multiple_windows_page(page: Page) -> MultipleWindowsPage:
    """Fixture for MultipleWindowsPage object."""
    return MultipleWindowsPage(page)


@pytest.fixture
def menus_page(page: Page) -> MenusPage:
    """Fixture for MenusPage object."""
    return MenusPage(page)


@pytest.fixture
def notification_messages_page(page: Page) -> NotificationMessagesPage:
    """Fixture for NotificationMessagesPage object."""
    return NotificationMessagesPage(page)


@pytest.fixture
def redirect_link_page(page: Page) -> RedirectLinkPage:
    """Fixture for RedirectLinkPage object."""
    return RedirectLinkPage(page)


@pytest.fixture
def secure_file_download_page(page: Page) -> SecureFileDownloadPage:
    """Fixture for SecureFileDownloadPage object."""
    return SecureFileDownloadPage(page)
