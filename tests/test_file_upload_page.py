"""Tests for the File Upload page."""

import pytest
from playwright.sync_api import expect

from pages.file_upload_page import FileUploadPage


@pytest.mark.ui
@pytest.mark.regression
class TestFileUploadPage:
    """Tests for the File Upload page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, file_upload_page, home_page, base_url, page):
        """Set up page objects and base URL as class attributes."""
        self.file_upload_page = file_upload_page
        self.home_page = home_page
        self.base_url = base_url
        self.page = page

    @pytest.fixture
    def navigate_to_file_upload_page(self):
        """Fixture to navigate to the File Upload page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_file_upload_card()

    def test_page_heading_is_visible(self, navigate_to_file_upload_page):
        """
        Test that the page heading is visible.
        """
        expect(self.file_upload_page.get_page_heading()).to_be_visible()

    def test_uploader_heading_is_visible(self, navigate_to_file_upload_page):
        """
        Test that the File Uploader heading is visible.
        """
        expect(self.file_upload_page.get_uploader_heading()).to_be_visible()

    def test_file_input_is_present(self, navigate_to_file_upload_page):
        """
        Test that the file input element is present in the DOM.
        File inputs are typically hidden but should be attached.
        """
        expect(self.file_upload_page.get_file_input()).to_be_attached()

    def test_upload_button_is_visible(self, navigate_to_file_upload_page):
        """
        Test that the Upload button is visible.
        """
        expect(self.file_upload_page.get_upload_button()).to_be_visible()

    def test_upload_file(self, navigate_to_file_upload_page):
        """
        Test that uploading a file displays the uploaded section with the correct file name.
        """
        file_path = FileUploadPage.create_test_file("Upload test content.")
        self.file_upload_page.upload_file(file_path)
        self.file_upload_page.click_upload_button()
        expect(self.page.locator("//h3[contains(text(), 'File Uploaded')]")).to_be_visible()
        expect(self.page.locator("//p[text()='test-upload.txt']")).to_be_visible()
