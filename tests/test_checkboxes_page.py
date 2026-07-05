"""Tests for the Checkboxes page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestCheckboxesPage:
    """Tests for the Checkboxes page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, checkboxes_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.checkboxes_page = checkboxes_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_checkboxes_page(self):
        """Fixture to navigate to the Checkboxes page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_checkboxes_card()

    def test_page_heading_is_visible(self, navigate_to_checkboxes_page):
        """
        Test that the Basic Checkboxes heading is visible.
        """
        expect(self.checkboxes_page.get_heading()).to_be_visible()

    def test_default_checkbox_states(self, navigate_to_checkboxes_page):
        """
        Test that checkbox1 is unchecked by default and checkbox2 is checked by default.
        """
        expect(self.checkboxes_page.get_checkbox1()).not_to_be_checked()
        expect(self.checkboxes_page.get_checkbox2()).to_be_checked()

    def test_toggle_checkbox(self, navigate_to_checkboxes_page):
        """
        Test that a checkbox can be toggled from unchecked to checked and back.
        """
        checkbox1 = self.checkboxes_page.get_checkbox1()
        expect(checkbox1).not_to_be_checked()
        checkbox1.check()
        expect(checkbox1).to_be_checked()
        checkbox1.uncheck()
        expect(checkbox1).not_to_be_checked()

    def test_disabled_checkboxes_cannot_be_changed(self, navigate_to_checkboxes_page):
        """
        Test that disabled checkboxes cannot be changed.
        """
        disabled_unchecked = self.checkboxes_page.get_disabled_unchecked()
        disabled_checked = self.checkboxes_page.get_disabled_checked()
        expect(disabled_unchecked).to_be_disabled()
        expect(disabled_unchecked).not_to_be_checked()
        expect(disabled_checked).to_be_disabled()
        expect(disabled_checked).to_be_checked()

    def test_terms_checkbox_can_be_checked(self, navigate_to_checkboxes_page):
        """
        Test that the terms checkbox can be checked.
        """
        terms_checkbox = self.checkboxes_page.get_terms_checkbox()
        expect(terms_checkbox).not_to_be_checked()
        terms_checkbox.check()
        expect(terms_checkbox).to_be_checked()

    def test_select_all_checks_all_items(self, navigate_to_checkboxes_page):
        """
        Test that clicking Select All checks all fruit checkboxes.
        """
        select_all = self.checkboxes_page.get_select_all()
        item1 = self.checkboxes_page.get_item1()
        item2 = self.checkboxes_page.get_item2()
        item3 = self.checkboxes_page.get_item3()

        expect(item1).not_to_be_checked()
        expect(item2).not_to_be_checked()
        expect(item3).not_to_be_checked()

        select_all.check()

        expect(item1).to_be_checked()
        expect(item2).to_be_checked()
        expect(item3).to_be_checked()

    def test_unchecking_item_unchecks_select_all(self, navigate_to_checkboxes_page):
        """
        Test that unchecking an individual item unchecks Select All.
        """
        select_all = self.checkboxes_page.get_select_all()
        item1 = self.checkboxes_page.get_item1()

        select_all.check()
        expect(select_all).to_be_checked()

        item1.uncheck()
        expect(select_all).not_to_be_checked()

    def test_checking_all_items_checks_select_all(self, navigate_to_checkboxes_page):
        """
        Test that checking all items individually checks Select All.
        """
        select_all = self.checkboxes_page.get_select_all()
        item1 = self.checkboxes_page.get_item1()
        item2 = self.checkboxes_page.get_item2()
        item3 = self.checkboxes_page.get_item3()

        item1.check()
        item2.check()
        item3.check()

        expect(select_all).to_be_checked()
