"""Tests for the Redirect Link page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestRedirectLinkPage:
    """Tests for the Redirect Link page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, redirect_link_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.redirect_link_page = redirect_link_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_redirect_link_page(self):
        """Fixture to navigate to the Redirect Link page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_redirect_link_card()

    def test_page_heading_is_visible(self, navigate_to_redirect_link_page):
        """
        Test that the Redirect Link heading is visible.
        """
        expect(self.redirect_link_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_redirect_link_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.redirect_link_page.get_instruction_text()).to_be_visible()

    def test_start_redirect_button_is_visible(self, navigate_to_redirect_link_page):
        """
        Test that the Start Redirect button is visible.
        """
        expect(self.redirect_link_page.get_start_redirect_button()).to_be_visible()

    def test_click_start_redirect_shows_countdown(self, navigate_to_redirect_link_page):
        """
        Test that clicking Start Redirect shows the countdown text.
        """
        self.redirect_link_page.click_start_redirect()
        expect(self.redirect_link_page.get_redirecting_text()).to_be_visible()

    def test_redirect_to_destination_page(self, navigate_to_redirect_link_page):
        """
        Test that clicking Start Redirect redirects to the destination page.
        """
        self.redirect_link_page.click_start_redirect()
        self.page.wait_for_url("**/link/redirect-destination", timeout=15000)
        expect(self.page.get_by_role("heading", name="Redirect Destination")).to_be_visible()
