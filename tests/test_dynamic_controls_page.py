"""Tests for the Dynamic Controls page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDynamicControlsPage:
    """Tests for the Dynamic Controls page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, dynamic_controls_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.dynamic_controls_page = dynamic_controls_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_dynamic_controls_page(self):
        """Fixture to navigate to the Dynamic Controls page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_dynamic_controls_card()

    def test_page_heading_is_visible(self, navigate_to_dynamic_controls_page):
        """
        Test that the Dynamic Controls heading is visible.
        """
        expect(self.dynamic_controls_page.get_page_heading()).to_be_visible()

    def test_checkbox_is_visible_initially(self, navigate_to_dynamic_controls_page):
        """
        Test that the checkbox is visible on page load.
        """
        expect(self.dynamic_controls_page.get_checkbox()).to_be_visible()

    def test_remove_checkbox(self, navigate_to_dynamic_controls_page):
        """
        Test that clicking Remove removes the checkbox from the DOM.
        """
        self.dynamic_controls_page.click_toggle_checkbox_button()
        expect(self.dynamic_controls_page.get_checkbox()).not_to_be_visible()

    def test_add_checkbox(self, navigate_to_dynamic_controls_page):
        """
        Test that clicking Add brings the checkbox back.
        """
        self.dynamic_controls_page.click_toggle_checkbox_button()
        expect(self.dynamic_controls_page.get_checkbox()).not_to_be_visible()
        self.dynamic_controls_page.click_toggle_checkbox_button()
        expect(self.dynamic_controls_page.get_checkbox()).to_be_visible()

    def test_text_input_is_disabled_initially(self, navigate_to_dynamic_controls_page):
        """
        Test that the text input is disabled by default.
        """
        expect(self.dynamic_controls_page.get_text_input()).to_be_disabled()

    def test_enable_text_input(self, navigate_to_dynamic_controls_page):
        """
        Test that clicking Enable enables the text input.
        """
        self.dynamic_controls_page.click_toggle_input_button()
        expect(self.dynamic_controls_page.get_text_input()).to_be_enabled()

    def test_disable_text_input(self, navigate_to_dynamic_controls_page):
        """
        Test that clicking Disable disables the text input.
        """
        self.dynamic_controls_page.click_toggle_input_button()
        expect(self.dynamic_controls_page.get_text_input()).to_be_enabled()
        self.dynamic_controls_page.click_toggle_input_button()
        expect(self.dynamic_controls_page.get_text_input()).to_be_disabled()
