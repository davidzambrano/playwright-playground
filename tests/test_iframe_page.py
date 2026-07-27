"""Tests for the iFrame page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestIFramePage:
    """Tests for the iFrame page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, iframe_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.iframe_page = iframe_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_iframe_page(self):
        """Fixture to navigate to the iFrame page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_iframe_card()

    def test_page_heading_is_visible(self, navigate_to_iframe_page):
        """
        Test that the iFrame page heading is visible.
        """
        expect(self.iframe_page.get_page_heading()).to_be_visible()

    def test_iframe_is_present(self, navigate_to_iframe_page):
        """
        Test that the iFrame element is present on the page.
        """
        expect(self.iframe_page.get_iframe_element()).to_be_attached()

    def test_switch_to_iframe_and_get_text(self, navigate_to_iframe_page):
        """
        Test switching to iFrame and retrieving text content.
        """
        # Get initial text from iFrame
        initial_text = self.iframe_page.get_iframe_text()
        # Verify iFrame has content (expect() works with locators, not strings)
        assert initial_text, "iFrame text should not be empty"

    def test_clear_and_type_in_iframe(self, navigate_to_iframe_page):
        """
        Test clearing iFrame content and typing new text.
        """
        # Clear the iFrame content
        self.iframe_page.clear_iframe_content()

        # Type new text
        test_text = "Hello, Playwright!"
        self.iframe_page.type_in_iframe(test_text)

        # Verify the text was entered
        actual_text = self.iframe_page.get_iframe_text()
        assert (
            test_text in actual_text
        ), f"Expected '{test_text}' to be in iFrame, got: {actual_text}"

    def test_parent_page_content_accessible(self, navigate_to_iframe_page):
        """
        Test that parent page content is still accessible while working with iFrame.
        """
        # Verify Back to Home link is visible (element outside iFrame)
        expect(self.iframe_page.get_back_to_home_link()).to_be_visible()

    def test_type_text_without_clearing(self, navigate_to_iframe_page):
        """
        Test typing text into iFrame without clearing first (appends to existing content).
        """
        # Type additional text without clearing
        additional_text = " Additional text"
        self.iframe_page.type_in_iframe(additional_text)

        # Verify the text was appended
        actual_text = self.iframe_page.get_iframe_text()
        assert (
            additional_text.strip() in actual_text
        ), f"Expected '{additional_text.strip()}' to be in iFrame"
