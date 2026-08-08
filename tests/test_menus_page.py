"""Tests for the Menus page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestMenusPage:
    """Tests for the Menus page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, menus_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.menus_page = menus_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_menus_page(self):
        """Fixture to navigate to the Menus page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_menus_card()

    def test_page_heading_is_visible(self, navigate_to_menus_page):
        """
        Test that the Menus heading is visible.
        """
        expect(self.menus_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_menus_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.menus_page.get_instruction_text()).to_be_visible()

    def test_enabled_trigger_is_visible(self, navigate_to_menus_page):
        """
        Test that the Enabled menu trigger is visible.
        """
        expect(self.menus_page.get_enabled_trigger()).to_be_visible()

    def test_disabled_trigger_is_disabled(self, navigate_to_menus_page):
        """
        Test that the Disabled menu trigger is disabled.
        """
        expect(self.menus_page.get_disabled_trigger()).to_be_disabled()

    def test_hover_shows_menu_items(self, navigate_to_menus_page):
        """
        Test that hovering over the Enabled trigger shows the menu items.
        """
        self.menus_page.hover_over_enabled_trigger()
        expect(self.menus_page.get_copy_menu_item()).to_be_visible()
        expect(self.menus_page.get_paste_menu_item()).to_be_visible()
        expect(self.menus_page.get_preferences_menu_item()).to_be_visible()

    def test_click_copy_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the Copy menu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.click_copy_menu_item()
        expect(self.menus_page.get_toast()).to_be_visible()

    def test_click_paste_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the Paste menu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.click_paste_menu_item()
        expect(self.menus_page.get_toast()).to_be_visible()

    def test_click_preferences_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the Preferences menu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.click_preferences_menu_item()
        expect(self.menus_page.get_toast()).to_be_visible()

    def test_submenu_shows_on_hover(self, navigate_to_menus_page):
        """
        Test that hovering over the Downloads submenu trigger shows submenu items.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.hover_over_submenu_trigger()
        expect(self.menus_page.get_pdf_submenu_item()).to_be_visible()
        expect(self.menus_page.get_csv_submenu_item()).to_be_visible()
        expect(self.menus_page.get_excel_submenu_item()).to_be_visible()

    def test_click_pdf_submenu_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the PDF submenu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.hover_over_submenu_trigger()
        self.menus_page.click_pdf_submenu_item()
        expect(self.menus_page.get_toast()).to_be_visible()

    def test_click_csv_submenu_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the CSV submenu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.hover_over_submenu_trigger()
        self.menus_page.click_csv_submenu_item()
        expect(self.menus_page.get_toast()).to_be_visible()

    def test_click_excel_submenu_shows_toast(self, navigate_to_menus_page):
        """
        Test that clicking the Excel submenu item shows a toast notification.
        """
        self.menus_page.hover_over_enabled_trigger()
        self.menus_page.hover_over_submenu_trigger()
        self.menus_page.click_excel_submenu_item()
        expect(self.menus_page.get_toast()).to_be_visible()
