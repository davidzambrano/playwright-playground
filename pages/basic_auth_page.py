"""Page object for the Basic Auth page."""

import logging

from playwright.sync_api import Page

from .base_page import BasePage

logger = logging.getLogger(__name__)


class BasicAuthPage(BasePage):
    """Page object for the Basic Auth page."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.header_locator = "//span[.='Add/Remove Elements'] | //h1[.='Basic Auth']"

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        logger.debug("Getting page header element with locator: %s", self.header_locator)
        return self.page.locator(self.header_locator)
