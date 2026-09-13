"""Tests for the Challenging DOM page."""

import allure
import pytest
from playwright.sync_api import expect


@allure.epic("Challenging DOM Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestChallengingDomPage:
    """Tests for the Challenging DOM page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, challenging_dom_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.challenging_dom_page = challenging_dom_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_challenging_dom_page(self):
        """Fixture to navigate to the Challenging DOM page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_challenging_dom_card()

    @allure.story("Challenging DOM behaviour")
    @allure.title("Description and canvas are visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_description_and_canvas_are_visible(self, navigate_to_challenging_dom_page):
        """
        Test that the page description and canvas elements are visible.
        """
        expect(self.challenging_dom_page.get_description()).to_be_visible()
        expect(self.challenging_dom_page.get_canvas()).to_be_visible()

    @allure.story("Challenging DOM behaviour")
    @allure.title("Buttons are present and interactable")
    @allure.severity(allure.severity_level.NORMAL)
    def test_buttons_are_present_and_interactable(self, navigate_to_challenging_dom_page):
        """
        Test that the three challenge buttons are present, visible, and clickable.
        """
        buttons = self.challenging_dom_page.get_buttons()
        expect(buttons).to_have_count(3)
        for btn in buttons.all():
            expect(btn).to_be_visible()
            btn.click()

    @allure.story("Challenging DOM behaviour")
    @allure.title("Table structure and row deletion")
    @allure.severity(allure.severity_level.NORMAL)
    def test_table_structure_and_row_deletion(self, navigate_to_challenging_dom_page):
        """
        Test that the table is visible, has initial rows, and that individual row deletions work.
        """
        table = self.challenging_dom_page.get_table()
        expect(table).to_be_visible()
        rows = self.challenging_dom_page.get_table_rows()
        # Assert initial count and auto-wait for rows to be present
        expect(rows).to_have_count(10)

        # Delete first row and verify count
        self.challenging_dom_page.delete_table_row(0)
        expect(self.challenging_dom_page.get_table_rows()).to_have_count(9)

        # Delete another row and verify count
        self.challenging_dom_page.delete_table_row(0)
        expect(self.challenging_dom_page.get_table_rows()).to_have_count(8)

    @allure.story("Challenging DOM behaviour")
    @allure.title("Delete all rows")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_all_rows(self, navigate_to_challenging_dom_page):
        """
        Test that all rows can be deleted from the table one by one.
        """
        # Explicitly wait for the initial 10 rows to be present
        expect(self.challenging_dom_page.get_table_rows()).to_have_count(10)

        # Delete all rows one by one
        while self.challenging_dom_page.get_table_rows().count() > 0:
            self.challenging_dom_page.delete_table_row(0)
        expect(self.challenging_dom_page.get_table_rows()).to_have_count(0)
