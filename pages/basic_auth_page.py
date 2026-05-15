"""Page object for the Basic Auth page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class BasicAuthPage(BasePage):
    """Page object for the Basic Auth page."""

    # Locators
    HEADER_LOCATOR = "//h1[.='Basic Auth']"

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        logger.debug("Getting page header element with locator: %s", self.HEADER_LOCATOR)
        return self.page.locator(self.HEADER_LOCATOR)
