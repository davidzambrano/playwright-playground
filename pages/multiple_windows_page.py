"""Page object for the Multiple Windows page."""

import logging
import re

from playwright.sync_api import Page

from .base_page import BasePage

logger = logging.getLogger(__name__)


class MultipleWindowsPage(BasePage):
    """Page object for the Multiple Windows page."""

    # Locators
    PAGE_HEADING = re.compile("Multiple Windows")
    INSTRUCTION_TEXT = re.compile("This is a page for the Multiple Windows example")
    CLICK_HERE_LINK = "Click Here"

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

    def get_click_here_link(self):
        """Get the Click Here link element.

        Returns:
            Locator: The locator for the Click Here link element.
        """
        logger.info("Getting Click Here link element")
        return self.page.get_by_text(self.CLICK_HERE_LINK, exact=True)

    def click_click_here(self) -> Page:
        """Click the Click Here link and return the new window page.

        Returns:
            Page: The new window page opened in a separate tab.
        """
        logger.info("Clicking Click Here link to open a new window")
        with self.page.expect_popup() as popup_info:
            self.get_click_here_link().click()
        new_page = popup_info.value
        new_page.wait_for_load_state("load")
        logger.info("New window opened")
        return new_page
