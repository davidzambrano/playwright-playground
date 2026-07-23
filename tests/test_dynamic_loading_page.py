"""Tests for the Dynamic Loading page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDynamicLoadingPage:
    """Tests for the Dynamic Loading page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, dynamic_loading_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.dynamic_loading_page = dynamic_loading_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_dynamic_loading_page(self):
        """Fixture to navigate to the Dynamic Loading page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_dynamic_loading_card()

    def test_page_heading_is_visible(self, navigate_to_dynamic_loading_page):
        """
        Test that the Dynamic Loading heading is visible.
        """
        expect(self.dynamic_loading_page.get_page_heading()).to_be_visible()

    def test_example1_content_is_hidden_initially(self, navigate_to_dynamic_loading_page):
        """
        Test that the Example 1 content is hidden before clicking Start.
        """
        expect(self.dynamic_loading_page.get_example1_content()).not_to_be_visible()

    def test_example1_content_becomes_visible_after_start(self, navigate_to_dynamic_loading_page):
        """
        Test that clicking Start in Example 1 reveals the hidden content.
        """
        self.dynamic_loading_page.click_example1_start_button()
        self.dynamic_loading_page.wait_for_example1_content_visible()
        expect(self.dynamic_loading_page.get_example1_content()).to_be_visible()

    def test_example1_content_text_is_correct(self, navigate_to_dynamic_loading_page):
        """
        Test that the Example 1 content displays the expected text.
        """
        self.dynamic_loading_page.click_example1_start_button()
        self.dynamic_loading_page.wait_for_example1_content_visible()
        expect(self.dynamic_loading_page.get_example1_content()).to_have_text(
            "This content was hidden but is now visible."
        )

    def test_example2_content_not_present_initially(self, navigate_to_dynamic_loading_page):
        """
        Test that the Example 2 finish content is not present before clicking Start.
        """
        expect(self.dynamic_loading_page.get_example2_finish_content()).not_to_be_visible()

    def test_example2_content_appears_after_start(self, navigate_to_dynamic_loading_page):
        """
        Test that clicking Start in Example 2 loads the content after the async request.
        """
        self.dynamic_loading_page.click_example2_start_button()
        self.dynamic_loading_page.wait_for_example2_content_loaded()
        expect(self.dynamic_loading_page.get_example2_finish_content()).to_be_visible()

    def test_example2_content_text_is_hello_world(self, navigate_to_dynamic_loading_page):
        """
        Test that the Example 2 finish content displays "Hello World!".
        """
        self.dynamic_loading_page.click_example2_start_button()
        self.dynamic_loading_page.wait_for_example2_content_loaded()
        expect(self.dynamic_loading_page.get_example2_finish_content()).to_have_text("Hello World!")
