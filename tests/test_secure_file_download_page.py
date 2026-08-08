"""Tests for the Secure File Download page."""

import os
import tempfile

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestSecureFileDownloadPage:
    """Tests for the Secure File Download page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, secure_file_download_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.secure_file_download_page = secure_file_download_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_secure_file_download_page(self):
        """Fixture to navigate to the Secure File Download page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_secure_file_download_card()

    def test_page_heading_is_visible(self, navigate_to_secure_file_download_page):
        """
        Test that the Secure File Download heading is visible.
        """
        expect(self.secure_file_download_page.get_page_heading()).to_be_visible()

    def test_login_form_is_visible(self, navigate_to_secure_file_download_page):
        """
        Test that the login form elements are visible.
        """
        expect(self.secure_file_download_page.get_login_card_title()).to_be_visible()
        expect(self.secure_file_download_page.get_username_input()).to_be_visible()
        expect(self.secure_file_download_page.get_password_input()).to_be_visible()
        expect(self.secure_file_download_page.get_login_button()).to_be_visible()

    def test_successful_login_shows_secure_area(self, navigate_to_secure_file_download_page):
        """
        Test that logging in with correct credentials shows the secure area.
        """
        self.secure_file_download_page.login("admin", "admin")
        expect(self.secure_file_download_page.get_secure_area_heading()).to_be_visible()
        expect(self.secure_file_download_page.get_welcome_text()).to_be_visible()

    def test_download_sample_file(self, navigate_to_secure_file_download_page):
        """
        Test that downloading sample.txt works after login.
        """
        self.secure_file_download_page.login("admin", "admin")
        with self.page.expect_download() as download_info:
            self.secure_file_download_page.click_download("sample.txt")
        download = download_info.value
        assert download.suggested_filename == "sample.txt"

    def test_download_file_content(self, navigate_to_secure_file_download_page):
        """
        Test that the downloaded file contains the expected content.
        """
        self.secure_file_download_page.login("admin", "admin")
        with self.page.expect_download() as download_info:
            self.secure_file_download_page.click_download("sample.txt")
        download = download_info.value

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, download.suggested_filename)
            download.save_as(file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        assert "This is a sample text file." in content

    def test_logout_returns_to_login(self, navigate_to_secure_file_download_page):
        """
        Test that logging out returns to the login form.
        """
        self.secure_file_download_page.login("admin", "admin")
        expect(self.secure_file_download_page.get_secure_area_heading()).to_be_visible()
        self.secure_file_download_page.click_logout()
        expect(self.secure_file_download_page.get_login_card_title()).to_be_visible()
