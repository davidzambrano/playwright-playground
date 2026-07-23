"""Tests for the Stale Element page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestStaleElementPage:
    """Tests for the Stale Element page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, stale_element_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.stale_element_page = stale_element_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_stale_element_page(self):
        """Fixture to navigate to the Stale Element page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_stale_element_card()

    def test_page_heading_is_visible(self, navigate_to_stale_element_page):
        """
        Test that the Stale Element Monster heading is visible.
        """
        expect(self.stale_element_page.get_page_heading()).to_be_visible()

    def test_stale_button_is_visible(self, navigate_to_stale_element_page):
        """
        Test that the stale button is visible on the page.
        """
        expect(self.stale_element_page.get_stale_button()).to_be_visible()

    def test_click_stale_button_shows_success_message(self, navigate_to_stale_element_page):
        """
        Test that clicking the stale button shows the success message.

        Playwright auto-retries actions on stale element references,
        so it should succeed despite the 150ms re-render interval.
        """
        self.stale_element_page.click_stale_button()
        expect(self.stale_element_page.get_success_message()).to_be_visible()

    def test_click_stale_button_shows_success_description(self, navigate_to_stale_element_page):
        """
        Test that clicking the stale button shows the success description.
        """
        self.stale_element_page.click_stale_button()
        expect(self.stale_element_page.get_success_message()).to_be_visible()
        expect(self.stale_element_page.get_success_description()).to_be_visible()

    def test_success_message_has_correct_text(self, navigate_to_stale_element_page):
        """
        Test that the success message displays the expected text.
        """
        self.stale_element_page.click_stale_button()
        expect(self.stale_element_page.get_success_message()).to_contain_text(
            "You managed to click the button"
        )

    def test_stale_button_label_is_correct(self, navigate_to_stale_element_page):
        """
        Test that the stale button has the expected label text.
        """
        expect(self.stale_element_page.get_stale_button()).to_have_text("Click Me, If You Can!")
