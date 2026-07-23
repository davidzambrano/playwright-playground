"""Tests for the Floating Menu page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestFloatingMenuPage:
    """Tests for the Floating Menu page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, floating_menu_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.floating_menu_page = floating_menu_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_floating_menu_page(self):
        """Fixture to navigate to the Floating Menu page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_floating_menu_card()

    def test_page_heading_is_visible(self, navigate_to_floating_menu_page):
        """
        Test that the page heading is visible.
        """
        expect(self.floating_menu_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_floating_menu_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.floating_menu_page.get_instruction_text()).to_be_visible()

    def test_floating_menu_is_visible_on_load(self, navigate_to_floating_menu_page):
        """
        Test that the floating menu is visible when the page loads.
        """
        expect(self.floating_menu_page.get_floating_menu()).to_be_visible()
        assert self.floating_menu_page.is_menu_visible()

    def test_menu_hides_on_scroll_down(self, navigate_to_floating_menu_page):
        """
        Test that the floating menu hides when scrolling down.
        """
        self.floating_menu_page.scroll_down()
        assert self.floating_menu_page.is_menu_hidden()

    def test_menu_reappears_on_scroll_up(self, navigate_to_floating_menu_page):
        """
        Test that the floating menu reappears when scrolling back up.
        """
        self.floating_menu_page.scroll_down()
        assert self.floating_menu_page.is_menu_hidden()
        self.floating_menu_page.scroll_up()
        assert self.floating_menu_page.is_menu_visible()
