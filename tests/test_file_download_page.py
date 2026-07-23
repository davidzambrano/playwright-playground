"""Tests for the File Download page."""

import os
import tempfile

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestFileDownloadPage:
    """Tests for the File Download page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, file_download_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.file_download_page = file_download_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_file_download_page(self):
        """Fixture to navigate to the File Download page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_file_download_card()

    def test_page_heading_is_visible(self, navigate_to_file_download_page):
        """
        Test that the page heading is visible.
        """
        expect(self.file_download_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_file_download_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.file_download_page.get_instruction_text()).to_be_visible()

    def test_download_button_is_visible(self, navigate_to_file_download_page):
        """
        Test that the Download File button is visible.
        """
        expect(self.file_download_page.get_download_button()).to_be_visible()

    def test_download_file(self, navigate_to_file_download_page):
        """
        Test that clicking the Download File button downloads sample-file.txt.
        """
        with self.page.expect_download() as download_info:
            self.file_download_page.click_download_button()
        download = download_info.value
        assert download.suggested_filename == "sample-file.txt"

    def test_download_file_content(self, navigate_to_file_download_page):
        """
        Test that the downloaded file contains the expected text.
        """
        with self.page.expect_download() as download_info:
            self.file_download_page.click_download_button()
        download = download_info.value

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, download.suggested_filename)
            download.save_as(file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        assert "This is a sample file for download." in content
