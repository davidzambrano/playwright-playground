"""Page object for the Redirect Link page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class RedirectLinkPage(BasePage):
    """Page object for the Redirect Link page."""

    # Locators
    PAGE_HEADING = re.compile("Redirect Link")
    INSTRUCTION_TEXT = re.compile("redirected to a new page after a short delay")
    START_REDIRECT_BUTTON = "Start Redirect"
    REDIRECTING_TEXT = re.compile("Redirecting in")

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

    def get_start_redirect_button(self):
        """Get the Start Redirect button element.

        Returns:
            Locator: The locator for the Start Redirect button element.
        """
        logger.info("Getting Start Redirect button element")
        return self.page.get_by_role("button", name=self.START_REDIRECT_BUTTON)

    def get_redirecting_text(self):
        """Get the redirecting countdown text element.

        Returns:
            Locator: The locator for the redirecting countdown text element.
        """
        logger.info("Getting redirecting countdown text element")
        return self.page.get_by_text(self.REDIRECTING_TEXT)

    def click_start_redirect(self):
        """Click the Start Redirect button.

        Returns:
            None
        """
        logger.info("Clicking Start Redirect button")
        self.get_start_redirect_button().click()
