"""Page object for the File Upload page."""

import logging
import os
import tempfile

from .base_page import BasePage

logger = logging.getLogger(__name__)


class FileUploadPage(BasePage):
    """Page object for the File Upload page."""

    # Locators
    PAGE_HEADING = "//h1"
    UPLOADER_HEADING = "//h2[contains(text(), 'File Uploader')]"
    FILE_INPUT = "#file-upload"
    UPLOAD_BUTTON = "//button[normalize-space()='Upload']"
    UPLOADED_SECTION = "//div[.//h3[contains(text(), 'File Uploaded')]]"
    UPLOADED_FILE_NAME = "//div[.//h3[contains(text(), 'File Uploaded')]]//p"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_uploader_heading(self):
        """Get the uploader heading element.

        Returns:
            Locator: The locator for the uploader heading element.
        """
        logger.info("Getting uploader heading element")
        return self.page.locator(self.UPLOADER_HEADING)

    def get_file_input(self):
        """Get the file input element.

        Returns:
            Locator: The locator for the file input element.
        """
        logger.info("Getting file input element")
        return self.page.locator(self.FILE_INPUT)

    def get_upload_button(self):
        """Get the Upload button element.

        Returns:
            Locator: The locator for the Upload button element.
        """
        logger.info("Getting Upload button element")
        return self.page.locator(self.UPLOAD_BUTTON)

    def get_uploaded_section(self):
        """Get the uploaded file section element.

        Returns:
            Locator: The locator for the uploaded file section element.
        """
        logger.info("Getting uploaded section element")
        return self.page.locator(self.UPLOADED_SECTION)

    def get_uploaded_file_name(self):
        """Get the uploaded file name element.

        Returns:
            Locator: The locator for the uploaded file name element.
        """
        logger.info("Getting uploaded file name element")
        return self.page.locator(self.UPLOADED_FILE_NAME)

    def upload_file(self, file_path: str):
        """Set the file input to the given file path.

        Args:
            file_path (str): The path to the file to upload.

        Returns:
            None
        """
        logger.info("Setting file input to: %s", file_path)
        self.get_file_input().set_input_files(file_path)

    def click_upload_button(self):
        """Click the Upload button.

        Returns:
            None
        """
        logger.info("Clicking Upload button")
        self.get_upload_button().click()

    @staticmethod
    def create_test_file(content: str = "This is a test file for upload.") -> str:
        """Create a temporary test file and return its path.

        Args:
            content (str): The text content to write to the file.

        Returns:
            str: The path to the created temporary file.
        """
        tmp_dir = tempfile.gettempdir()
        file_path = os.path.join(tmp_dir, "test-upload.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info("Created test file at: %s", file_path)
        return file_path
