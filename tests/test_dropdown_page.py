"""Tests for the Dropdown page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDropdownPage:
    """Tests for the Dropdown page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, dropdown_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.dropdown_page = dropdown_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_dropdown_page(self):
        """Fixture to navigate to the Dropdown page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_dropdown_card()

    def test_headings_are_visible(self, navigate_to_dropdown_page):
        """
        Test that both Simple Dropdown and Searchable Combobox headings are visible.
        """
        expect(self.dropdown_page.get_simple_dropdown_heading()).to_be_visible()
        expect(self.dropdown_page.get_searchable_combobox_heading()).to_be_visible()

    def test_simple_dropdown_select_apple(self, navigate_to_dropdown_page):
        """
        Test that selecting Apple from the simple dropdown updates the confirmation text.
        """
        self.dropdown_page.select_simple_dropdown_option("apple")
        expect(self.dropdown_page.get_selection_text()).to_contain_text("apple")

    def test_simple_dropdown_select_banana(self, navigate_to_dropdown_page):
        """
        Test that selecting Banana from the simple dropdown updates the confirmation text.
        """
        self.dropdown_page.select_simple_dropdown_option("banana")
        expect(self.dropdown_page.get_selection_text()).to_contain_text("banana")

    def test_simple_dropdown_select_vegetable(self, navigate_to_dropdown_page):
        """
        Test that selecting a vegetable from the simple dropdown updates the confirmation text.
        """
        self.dropdown_page.select_simple_dropdown_option("carrot")
        expect(self.dropdown_page.get_selection_text()).to_contain_text("carrot")

    def test_combobox_search_and_select_nextjs(self, navigate_to_dropdown_page):
        """
        Test that searching for Next.js in the combobox and selecting it updates the button text.
        """
        self.dropdown_page.select_combobox_option("Next.js")
        expect(self.dropdown_page.get_combobox_trigger()).to_contain_text("Next.js")

    def test_combobox_search_and_select_react(self, navigate_to_dropdown_page):
        """
        Test that searching for React in the combobox and selecting it updates the button text.
        """
        self.dropdown_page.select_combobox_option("React")
        expect(self.dropdown_page.get_combobox_trigger()).to_contain_text("React")

    def test_combobox_search_filters_options(self, navigate_to_dropdown_page):
        """
        Test that typing in the combobox search filters the available options.
        """
        self.dropdown_page.get_combobox_trigger().click()
        self.dropdown_page.search_combobox("next")
        expect(self.dropdown_page.get_combobox_option("Next.js")).to_be_visible()
        expect(self.dropdown_page.get_combobox_option("React")).not_to_be_visible()

    def test_combobox_search_no_results(self, navigate_to_dropdown_page):
        """
        Test that searching for a non-existent framework shows no results message.
        """
        self.dropdown_page.get_combobox_trigger().click()
        self.dropdown_page.search_combobox("nonexistent")
        expect(self.dropdown_page.get_no_results_text()).to_be_visible()
