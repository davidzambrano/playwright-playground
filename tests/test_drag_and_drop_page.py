"""Tests for the Drag and Drop page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDragAndDropPage:
    """Tests for the Drag and Drop page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, drag_and_drop_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.drag_and_drop_page = drag_and_drop_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_drag_and_drop_page(self):
        """Fixture to navigate to the Drag and Drop page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_drag_and_drop_card()

    def test_page_heading_is_visible(self, navigate_to_drag_and_drop_page):
        """
        Test that the Drag and Drop heading is visible.
        """
        expect(self.drag_and_drop_page.get_page_heading()).to_be_visible()

    def test_draggable_item_in_column_a_initially(self, navigate_to_drag_and_drop_page):
        """
        Test that the draggable item is in column A initially.
        """
        expect(self.drag_and_drop_page.get_column_a()).to_contain_text("Drag me")

    def test_drag_item_to_column_b(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column A to column B works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_b())
        expect(self.drag_and_drop_page.get_column_b()).to_contain_text("Drag me")

    def test_verify_item_in_column_b_after_drop(self, navigate_to_drag_and_drop_page):
        """
        Test that after dropping the item in column B, it is a child of column B.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_b())
        expect(self.drag_and_drop_page.get_draggable_item()).to_be_visible()
        expect(self.drag_and_drop_page.get_column_b().locator("#draggable")).to_be_visible()

    def test_drag_item_to_column_c(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column A to column C works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_c())
        expect(self.drag_and_drop_page.get_column_c()).to_contain_text("Drag me")

    def test_drag_item_to_column_d(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column A to column D works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_d())
        expect(self.drag_and_drop_page.get_column_d()).to_contain_text("Drag me")

    def test_drag_item_back_to_column_a(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column B back to column A works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_b())
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_a())
        expect(self.drag_and_drop_page.get_column_a()).to_contain_text("Drag me")

    def test_drag_item_from_c_to_a(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column C back to column A works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_c())
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_a())
        expect(self.drag_and_drop_page.get_column_a()).to_contain_text("Drag me")

    def test_drag_item_from_d_to_a(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column D back to column A works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_d())
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_a())
        expect(self.drag_and_drop_page.get_column_a()).to_contain_text("Drag me")

    def test_drag_item_from_b_to_c(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column B to column C works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_b())
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_c())
        expect(self.drag_and_drop_page.get_column_c()).to_contain_text("Drag me")

    def test_drag_item_from_c_to_d(self, navigate_to_drag_and_drop_page):
        """
        Test that dragging the item from column C to column D works.
        """
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_c())
        self.drag_and_drop_page.drag_item_to_column(self.drag_and_drop_page.get_column_d())
        expect(self.drag_and_drop_page.get_column_d()).to_contain_text("Drag me")
