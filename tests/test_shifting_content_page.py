"""Tests for the Shifting Content page."""

import allure
import pytest
from playwright.sync_api import expect


@allure.epic("Shifting Content Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestShiftingContentPage:
    """Tests for the Shifting Content page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, shifting_content_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.shifting_content_page = shifting_content_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_shifting_content_page(self):
        """Fixture to navigate to the Shifting Content page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_shifting_content_card()

    @allure.story("Shifting Content behaviour")
    @allure.title("The Shifting Content heading is visible.'''")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_page_heading_is_visible(self, navigate_to_shifting_content_page):
        """Test that the Shifting Content heading is visible."""
        expect(self.shifting_content_page.get_page_heading()).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("The instruction text is visible.'''")
    @allure.severity(allure.severity_level.MINOR)
    def test_instruction_text_is_visible(self, navigate_to_shifting_content_page):
        """Test that the instruction text is visible."""
        expect(self.shifting_content_page.get_instruction_text()).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("All three example section headings are visible.'''")
    @allure.severity(allure.severity_level.NORMAL)
    def test_example_headings_are_visible(self, navigate_to_shifting_content_page):
        """Test that all three example section headings are visible."""
        expect(self.shifting_content_page.get_example_1_heading()).to_be_visible()
        expect(self.shifting_content_page.get_example_2_heading()).to_be_visible()
        expect(self.shifting_content_page.get_example_3_heading()).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("All menu buttons in Example 1 are visible.'''")
    @allure.severity(allure.severity_level.NORMAL)
    def test_menu_buttons_are_visible(self, navigate_to_shifting_content_page):
        """Test that all menu buttons in Example 1 are visible."""
        for label in ["Home", "About", "Portfolio", "Contact Us"]:
            expect(self.shifting_content_page.get_menu_button(label)).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("The shifting image is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_shifting_image_is_visible(self, navigate_to_shifting_content_page):
        """Test that the shifting image is visible.

        The image is located by its alt attribute, not by position,
        to test resilience to minor layout shifts.
        """
        expect(self.shifting_content_page.get_shifting_image()).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("Clicking the Portfolio menu item works regardless of position")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_portfolio_menu_item(self, navigate_to_shifting_content_page):
        """Test that clicking the Portfolio menu item works regardless of position.

        The menu element shifts a few pixels on each page load, so this test
        verifies that the menu item can be clicked without relying on its
        exact pixel position.
        """
        self.shifting_content_page.click_portfolio_menu_button()
        expect(self.shifting_content_page.get_portfolio_menu_button()).to_be_visible()

    @allure.story("Shifting Content behaviour")
    @allure.title("The Example 3 list contains five items.'''")
    @allure.severity(allure.severity_level.NORMAL)
    def test_list_has_five_items(self, navigate_to_shifting_content_page):
        """Test that the Example 3 list contains five items."""
        expect(self.shifting_content_page.get_list_items()).to_have_count(5)

    @allure.story("Shifting Content behaviour")
    @allure.title("Get_list_item_count returns the correct count.'''")
    @allure.severity(allure.severity_level.NORMAL)
    def test_list_item_count_method(self, navigate_to_shifting_content_page):
        """Test that get_list_item_count returns the correct count."""
        assert self.shifting_content_page.get_list_item_count() == 5
