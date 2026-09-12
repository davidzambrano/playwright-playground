"""Tests for the Sortable Data Tables page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestSortableDataTablesPage:
    """Tests for the Sortable Data Tables page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, sortable_data_tables_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.sortable_data_tables_page = sortable_data_tables_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_sortable_data_tables_page(self):
        """Fixture to navigate to the Sortable Data Tables page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_sortable_data_tables_card()

    @pytest.mark.smoke
    def test_page_heading_is_visible(self, navigate_to_sortable_data_tables_page):
        """Test that the Sortable Data Tables heading is visible."""
        expect(self.sortable_data_tables_page.get_page_heading()).to_be_visible()

    def test_example_headings_are_visible(self, navigate_to_sortable_data_tables_page):
        """Test that both example section headings are visible."""
        expect(self.sortable_data_tables_page.get_example_1_heading()).to_be_visible()
        expect(self.sortable_data_tables_page.get_example_2_heading()).to_be_visible()

    def test_both_tables_have_four_rows(self, navigate_to_sortable_data_tables_page):
        """Test that both tables render four data rows each."""
        for table_index in (0, 1):
            expect(self.sortable_data_tables_page.get_rows(table_index)).to_have_count(4)

    def test_header_buttons_are_visible(self, navigate_to_sortable_data_tables_page):
        """Test that all sortable header buttons are visible in both tables."""
        for table_index in (0, 1):
            for label in ["Last Name", "First Name", "Email", "Due", "Web Site"]:
                expect(
                    self.sortable_data_tables_page.get_header_button(label, table_index)
                ).to_be_visible()

    def test_default_sort_is_last_name_ascending(self, navigate_to_sortable_data_tables_page):
        """Test that tables load pre-sorted by Last Name ascending."""
        for table_index in (0, 1):
            last_names = self.sortable_data_tables_page.get_column_values("Last Name", table_index)
            assert last_names == ["Bach", "Conway", "Doe", "Smith"]

    def test_sort_by_first_name(self, navigate_to_sortable_data_tables_page):
        """Test that clicking First Name sorts alphabetically, Frank first."""
        self.sortable_data_tables_page.click_header_button("First Name")
        first_names = self.sortable_data_tables_page.get_column_values("First Name")
        assert first_names == ["Frank", "Jason", "John", "Tim"]
        expect(self.sortable_data_tables_page.get_rows().first).to_contain_text("Frank")

    def test_sort_toggle_reverses_order(self, navigate_to_sortable_data_tables_page):
        """Test that clicking the same header twice reverses the sort order."""
        page = self.sortable_data_tables_page
        page.click_header_button("First Name")
        ascending = page.get_column_values("First Name")
        page.click_header_button("First Name")
        descending = page.get_column_values("First Name")
        assert ascending == ["Frank", "Jason", "John", "Tim"]
        assert descending == list(reversed(ascending))

    def test_due_amount_for_jason_doe(self, navigate_to_sortable_data_tables_page):
        """Test that the Due amount for Jason Doe is $100.00."""
        row = self.sortable_data_tables_page.get_row_by_text("Jason")
        expect(row).to_contain_text("Doe")
        expect(row).to_contain_text("$100.00")
