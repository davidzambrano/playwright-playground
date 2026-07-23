"""Tests for the Key Presses page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestKeyPressesPage:
    """Tests for the Key Presses page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, key_presses_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.key_presses_page = key_presses_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_key_presses_page(self):
        """Fixture to navigate to the Key Presses page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_key_presses_card()

    def test_page_heading_is_visible(self, navigate_to_key_presses_page):
        """
        Test that the Key Presses heading is visible.
        """
        expect(self.key_presses_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_key_presses_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.key_presses_page.get_instruction_text()).to_be_visible()

    def test_input_field_is_visible(self, navigate_to_key_presses_page):
        """
        Test that the input field is visible.
        """
        expect(self.key_presses_page.get_input_field()).to_be_visible()

    def test_send_standard_key(self, navigate_to_key_presses_page):
        """
        Test that pressing a standard key (A) displays the correct result.
        """
        self.key_presses_page.press_key_in_input("A")
        expect(self.key_presses_page.get_result_value()).to_have_text("A")

    def test_send_special_key(self, navigate_to_key_presses_page):
        """
        Test that pressing a special key (Enter) displays the correct result.
        """
        self.key_presses_page.press_key_in_input("Enter")
        expect(self.key_presses_page.get_result_value()).to_have_text("ENTER")
