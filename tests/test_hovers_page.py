"""Tests for the Hovers page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestHoversPage:
    """Tests for the Hovers page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, hovers_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.hovers_page = hovers_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_hovers_page(self):
        """Fixture to navigate to the Hovers page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_hovers_card()

    def test_page_heading_is_visible(self, navigate_to_hovers_page):
        """
        Test that the Hovers heading is visible.
        """
        expect(self.hovers_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_hovers_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.hovers_page.get_instruction_text()).to_be_visible()

    def test_user_1_caption_visible_on_hover(self, navigate_to_hovers_page):
        """
        Test that hovering over User 1 image shows the caption.
        """
        self.hovers_page.hover_over_user_1()
        expect(self.hovers_page.get_user_1_caption()).to_be_visible()

    def test_user_2_caption_visible_on_hover(self, navigate_to_hovers_page):
        """
        Test that hovering over User 2 image shows the caption.
        """
        self.hovers_page.hover_over_user_2()
        expect(self.hovers_page.get_user_2_caption()).to_be_visible()

    def test_user_3_caption_visible_on_hover(self, navigate_to_hovers_page):
        """
        Test that hovering over User 3 image shows the caption.
        """
        self.hovers_page.hover_over_user_3()
        expect(self.hovers_page.get_user_3_caption()).to_be_visible()
