"""Tests for the Dynamic Content page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDynamicContentPage:
    """Tests for the Dynamic Content page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, dynamic_content_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.dynamic_content_page = dynamic_content_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_dynamic_content_page(self):
        """Fixture to navigate to the Dynamic Content page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_dynamic_content_card()

    def test_page_heading_is_visible(self, navigate_to_dynamic_content_page):
        """
        Test that the Dynamic Content heading is visible.
        """
        expect(self.dynamic_content_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_dynamic_content_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.dynamic_content_page.get_instruction_text()).to_be_visible()

    def test_randomize_button_is_visible(self, navigate_to_dynamic_content_page):
        """
        Test that the Randomize Content button is visible.
        """
        expect(self.dynamic_content_page.get_randomize_button()).to_be_visible()

    def test_content_items_are_visible(self, navigate_to_dynamic_content_page):
        """
        Test that content items are visible on the page.
        """
        expect(self.dynamic_content_page.get_content_items()).to_have_count(3)

    def test_content_changes_on_randomize(self, navigate_to_dynamic_content_page):
        """
        Test that clicking Randomize Content changes the displayed content.
        """
        initial_texts = self.dynamic_content_page.get_content_texts()
        self.dynamic_content_page.click_randomize_button()
        new_texts = self.dynamic_content_page.get_content_texts()
        assert initial_texts != new_texts, "Content should change after clicking Randomize"

    def test_images_change_on_randomize(self, navigate_to_dynamic_content_page):
        """
        Test that clicking Randomize Content changes the displayed images.
        """
        initial_images = self.dynamic_content_page.get_image_sources()
        self.dynamic_content_page.click_randomize_button()
        new_images = self.dynamic_content_page.get_image_sources()
        assert initial_images != new_images, "Images should change after clicking Randomize"

    def test_content_changes_on_refresh(self, navigate_to_dynamic_content_page):
        """
        Test that refreshing the page changes the displayed content.
        """
        initial_texts = self.dynamic_content_page.get_content_texts()
        self.page.reload()
        self.dynamic_content_page.get_content_items().first.wait_for(state="visible")
        new_texts = self.dynamic_content_page.get_content_texts()
        assert initial_texts != new_texts, "Content should change after page refresh"
