"""Tests for the Inputs page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestInputsPage:
    """Tests for the Inputs page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, inputs_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.inputs_page = inputs_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_inputs_page(self):
        """Fixture to navigate to the Inputs page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_inputs_card()

    def test_page_heading_is_visible(self, navigate_to_inputs_page):
        """
        Test that the Inputs page heading is visible.
        """
        expect(self.inputs_page.get_page_heading()).to_be_visible()

    def test_all_input_fields_are_visible(self, navigate_to_inputs_page):
        """
        Test that all input fields are visible on the page.
        """
        expect(self.inputs_page.get_name_input()).to_be_visible()
        expect(self.inputs_page.get_email_input()).to_be_visible()
        expect(self.inputs_page.get_password_input()).to_be_visible()
        expect(self.inputs_page.get_number_input()).to_be_visible()
        expect(self.inputs_page.get_website_input()).to_be_visible()

    def test_valid_form_submission(self, navigate_to_inputs_page):
        """
        Test valid form submission.
        """
        # Fill form with valid data
        self.inputs_page.submit_form(
            name="John Doe",
            email="john@example.com",
            password="password123",
            number="42",
            website="https://example.com",
        )

        # Verify success toast appears
        expect(self.inputs_page.get_toast_title()).to_be_visible()

    def test_invalid_email_shows_error(self, navigate_to_inputs_page):
        """
        Test invalid email format shows validation error.
        """
        # Fill form with invalid email
        self.inputs_page.fill_name("John Doe")
        self.inputs_page.fill_email("invalid-email")
        self.inputs_page.fill_password("password123")
        self.inputs_page.fill_number("42")
        self.inputs_page.fill_website("https://example.com")
        self.inputs_page.click_submit()

        # Verify form submission failed (toast should not appear)
        expect(self.inputs_page.get_toast_title()).not_to_be_visible()

    def test_required_field_empty_shows_error(self, navigate_to_inputs_page):
        """
        Test empty required field shows validation error.
        """
        # Submit form with empty name (required field)
        self.inputs_page.fill_email("john@example.com")
        self.inputs_page.fill_password("password123")
        self.inputs_page.fill_number("42")
        self.inputs_page.fill_website("https://example.com")
        self.inputs_page.click_submit()

        # Verify validation error appears (toast should not appear)
        expect(self.inputs_page.get_toast_title()).not_to_be_visible()
