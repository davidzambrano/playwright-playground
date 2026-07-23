"""Tests for the Entry Ad page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestEntryAdPage:
    """Tests for the Entry Ad page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, entry_ad_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.entry_ad_page = entry_ad_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_entry_ad_page(self):
        """Fixture to navigate to the Entry Ad page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_entry_ad_card()

    def test_page_heading_is_visible(self, navigate_to_entry_ad_page):
        """
        Test that the page heading is visible.
        """
        expect(self.entry_ad_page.get_page_heading()).to_be_visible()

    def test_modal_appears_on_page_load(self, navigate_to_entry_ad_page):
        """
        Test that the modal window appears after navigating to the page.
        """
        self.entry_ad_page.wait_for_modal()
        expect(self.entry_ad_page.get_modal()).to_be_visible()

    def test_modal_has_title(self, navigate_to_entry_ad_page):
        """
        Test that the modal has a title.
        """
        self.entry_ad_page.wait_for_modal()
        expect(self.entry_ad_page.get_modal_title()).to_be_visible()

    def test_modal_has_body_text(self, navigate_to_entry_ad_page):
        """
        Test that the modal has body text.
        """
        self.entry_ad_page.wait_for_modal()
        expect(self.entry_ad_page.get_modal_body()).to_be_visible()

    def test_close_modal(self, navigate_to_entry_ad_page):
        """
        Test that clicking the Close button dismisses the modal.
        """
        self.entry_ad_page.wait_for_modal()
        self.entry_ad_page.click_close_button()
        expect(self.entry_ad_page.get_modal()).not_to_be_visible()
