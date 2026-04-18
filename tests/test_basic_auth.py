"""Tests for the Basic Auth page."""

import pytest
from playwright.sync_api import expect


class TestBasicAuthPage:
    """Tests for the Basic Auth page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, home_page, page, basic_auth_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.home_page = home_page
        self.basic_auth_page = basic_auth_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_basic_auth_page(self):
        """Fixture to navigate to the Basic Auth page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_basic_auth_card()

    def test_basic_auth_page_loads(self, navigate_to_basic_auth_page):
        """Test that the Basic Auth page loads."""
        expect(self.basic_auth_page.get_header()).to_have_text("Basic Auth")
