"""Page object for the Entry Ad page."""

import logging

from .modal_page import ModalPage

logger = logging.getLogger(__name__)


class EntryAdPage(ModalPage):
    """Page object for the Entry Ad page."""

    # Locators
    PAGE_HEADING = "//h1"
    MODAL_TITLE = "//h2[contains(text(), 'THIS IS A MODAL WINDOW')]"
    MODAL_BODY = "//*[contains(text(), 'It is a modal window that appears on page load')]"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)
