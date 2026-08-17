"""Page object for the JavaScript onload event error page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class JavascriptOnloadErrorPage(BasePage):
    """Page object for the JavaScript onload event error page."""

    # Locators
    PAGE_HEADING = re.compile("JavaScript onload event error")
    INSTRUCTION_TEXT = re.compile("This page has a JavaScript error in the onload event")
    CONSOLE_HINT_TEXT = re.compile("Check your browser's developer console")

    def __init__(self, page):
        """Initialize the page object and capture console errors.

        Args:
            page (Page): The page object.
        """
        super().__init__(page)
        self.console_errors = []
        self.page.on("console", self._capture_console_error)

    def _capture_console_error(self, message):
        """Capture a console error message for later assertions.

        Args:
            message (ConsoleMessage): The console message object.
        """
        if message.type == "error":
            self.console_errors.append(message.text)
            logger.info("Captured console error: %s", message.text)

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

    def get_console_hint_text(self):
        """Get the console hint text element.

        Returns:
            Locator: The locator for the console hint text element.
        """
        logger.info("Getting console hint text element")
        return self.page.get_by_text(self.CONSOLE_HINT_TEXT)

    def get_console_errors(self):
        """Get the list of captured console errors.

        Returns:
            list: A list of console error messages captured during the page load.
        """
        logger.info("Getting captured console errors")
        return self.console_errors

    def has_console_errors(self) -> bool:
        """Check if any console errors were captured.

        Returns:
            bool: True if console errors were captured, False otherwise.
        """
        has_errors = len(self.console_errors) > 0
        logger.info("Console errors captured: %s", has_errors)
        return has_errors
