"""Tests for the Multiple Windows page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestMultipleWindowsPage:
    """Tests for the Multiple Windows page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, multiple_windows_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.multiple_windows_page = multiple_windows_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_multiple_windows_page(self):
        """Fixture to navigate to the Multiple Windows page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_multiple_windows_card()

    def test_page_heading_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the page heading is visible.
        """
        expect(self.multiple_windows_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.multiple_windows_page.get_instruction_text()).to_be_visible()

    def test_click_here_link_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the Click Here link is visible.
        """
        expect(self.multiple_windows_page.get_click_here_link()).to_be_visible()

    def test_click_here_opens_new_window(self, navigate_to_multiple_windows_page):
        """
        Test that clicking Click Here opens a new window.
        """
        new_page = self.multiple_windows_page.click_click_here()
        expect(new_page.locator("//h1")).to_have_text("New Window")
        new_page.close()

    def test_new_window_heading_is_correct(self, navigate_to_multiple_windows_page):
        """
        Test that the new window heading is 'New Window'.
        """
        new_page = self.multiple_windows_page.click_click_here()
        heading = new_page.locator("//h1")
        expect(heading).to_have_text("New Window")

    def test_new_window_content_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the new window content section is visible.
        """
        new_page = self.multiple_windows_page.click_click_here()
        content = new_page.locator("//h2[text()='New Window Content']")
        expect(content).to_be_visible()
        new_page.close()

    def test_original_page_still_active_after_closing_new_window(
        self, navigate_to_multiple_windows_page
    ):
        """
        Test that the original page remains active after closing the new window.
        """
        new_page = self.multiple_windows_page.click_click_here()
        new_page.close()
        expect(self.multiple_windows_page.get_page_heading()).to_have_text("Multiple Windows")

    def test_new_window_url_is_correct(self, navigate_to_multiple_windows_page):
        """
        Test that the new window navigates to the correct URL.
        """
        new_page = self.multiple_windows_page.click_click_here()
        assert "/link/new-window" in new_page.url
        new_page.close()

    def test_new_window_description_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the new window description text is visible.
        """
        new_page = self.multiple_windows_page.click_click_here()
        description = new_page.locator(
            "//p[contains(., 'This is a page that opened in a new window')]"
        )
        expect(description).to_be_visible()
        new_page.close()

    def test_new_window_back_to_home_link_is_visible(self, navigate_to_multiple_windows_page):
        """
        Test that the Back to Home link is visible in the new window.
        """
        new_page = self.multiple_windows_page.click_click_here()
        back_link = new_page.locator("//a[contains(text(), 'Back to Home')]")
        expect(back_link).to_be_visible()
        new_page.close()

    def test_original_page_url_unchanged_after_opening_new_window(
        self, navigate_to_multiple_windows_page
    ):
        """
        Test that the original page URL remains unchanged after opening a new window.
        """
        self.multiple_windows_page.click_click_here()
        assert "/link/multiple-windows" in self.multiple_windows_page.page.url

    def test_multiple_new_windows_can_be_opened(self, navigate_to_multiple_windows_page):
        """
        Test that multiple new windows can be opened simultaneously.
        """
        first_new_page = self.multiple_windows_page.click_click_here()
        second_new_page = self.multiple_windows_page.click_click_here()
        expect(first_new_page.locator("//h1")).to_have_text("New Window")
        expect(second_new_page.locator("//h1")).to_have_text("New Window")
        first_new_page.close()
        second_new_page.close()
