"""Tests for the Context Menu page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestContextMenuPage:
    """Tests for the Context Menu page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, context_menu_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.context_menu_page = context_menu_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_context_menu_page(self):
        """Fixture to navigate to the Context Menu page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_context_menu_card()

    def test_page_heading_is_visible(self, navigate_to_context_menu_page):
        """
        Test that the Context Menu heading is visible.
        """
        expect(self.context_menu_page.get_page_heading()).to_be_visible()

    def test_hotspot_area_is_visible(self, navigate_to_context_menu_page):
        """
        Test that the hot-spot area is visible.
        """
        expect(self.context_menu_page.get_hotspot_area()).to_be_visible()

    def test_right_click_triggers_context_menu(self, navigate_to_context_menu_page):
        """
        Test that right-clicking the hot-spot area triggers the custom context menu.
        """
        self.context_menu_page.right_click_hotspot()
        expect(self.context_menu_page.get_context_menu()).to_be_visible()

    def test_left_click_dismisses_context_menu(self, navigate_to_context_menu_page):
        """
        Test that left-clicking outside the menu dismisses the context menu.
        """
        self.context_menu_page.right_click_hotspot()
        expect(self.context_menu_page.get_context_menu()).to_be_visible()
        self.context_menu_page.left_click_outside_menu()
        expect(self.context_menu_page.get_context_menu()).not_to_be_visible()

    def test_hover_share_item_triggers_sub_menu(self, navigate_to_context_menu_page):
        """
        Test that hovering over the Share menu item triggers the sub-menu.
        """
        self.context_menu_page.right_click_hotspot()
        expect(self.context_menu_page.get_context_menu()).to_be_visible()
        self.context_menu_page.hover_over_share_item()
        expect(self.context_menu_page.get_sub_menu()).to_be_visible()
