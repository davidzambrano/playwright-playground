"""Page object for the File Download page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class FileDownloadPage(BasePage):
    """Page object for the File Download page."""

    # Locators
    PAGE_HEADING = re.compile("File Download")
    INSTRUCTION_TEXT = re.compile("Click the button to download")
    DOWNLOAD_BUTTON = "Download File"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_instruction_text(self):
        """Get the instruction text element.

        Returns:
            Locator: The locator for the instruction text element.
        """
        logger.info("Getting instruction text element")
        return self.page.get_by_text(self.INSTRUCTION_TEXT)

    def get_download_button(self):
        """Get the Download File button element.

        Returns:
            Locator: The locator for the Download File button element.
        """
        logger.info("Getting Download File button element")
        return self.page.get_by_role("button", name=self.DOWNLOAD_BUTTON)

    def click_download_button(self):
        """Click the Download File button.

        Returns:
            None
        """
        logger.info("Clicking Download File button")
        self.get_download_button().click()
