"""Page object for the Basic Auth page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class BasicAuthPage(BasePage):
    """Page object for the Basic Auth page."""

    # Locators
    HEADER_LOCATOR = "Basic Auth"

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        logger.debug("Getting page header element")
        return self.page.get_by_role("heading", name=self.HEADER_LOCATOR)
