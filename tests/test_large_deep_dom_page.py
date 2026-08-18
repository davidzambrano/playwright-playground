"""Tests for the Large & Deep DOM page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestLargeDeepDomPage:
    """Tests for the Large & Deep DOM page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, large_deep_dom_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.large_deep_dom_page = large_deep_dom_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_large_deep_dom_page(self):
        """Fixture to navigate to the Large & Deep DOM page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_large_deep_dom_card()

    def test_page_heading_is_visible(self, navigate_to_large_deep_dom_page):
        """Test that the page heading is visible."""
        expect(self.large_deep_dom_page.get_page_heading()).to_be_visible()

    def test_deeply_nested_dom_is_visible(self, navigate_to_large_deep_dom_page):
        """Test that the deeply nested DOM sections are visible."""
        expect(self.large_deep_dom_page.get_no_siblings_container()).to_be_visible()
        expect(self.large_deep_dom_page.get_deepest_level()).to_be_visible()
        expect(self.large_deep_dom_page.get_nested_siblings_container()).to_be_visible()
        expect(self.large_deep_dom_page.get_nested_sibling("1.1.1.1")).to_be_visible()

    def test_table_cell_is_accessible_by_id(self, navigate_to_large_deep_dom_page):
        """Test that a large table cell can be targeted by its id."""
        expect(self.large_deep_dom_page.get_table_cell(25, 25)).to_have_text("25.25")
