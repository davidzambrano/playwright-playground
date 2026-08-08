"""Page object for the Entry Ad page."""

import logging
import re

from .modal_page import ModalPage

logger = logging.getLogger(__name__)


class EntryAdPage(ModalPage):
    """Page object for the Entry Ad page."""

    # Locators
    PAGE_HEADING = re.compile("Entry Ad")
    MODAL_TITLE = re.compile("THIS IS A MODAL WINDOW")
    MODAL_BODY = re.compile("It is a modal window that appears on page load")

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_modal_title(self):
        """Get the modal title element.

        Returns:
            Locator: The locator for the modal title element.
        """
        logger.info("Getting modal title element")
        return self.get_modal().get_by_text(self.MODAL_TITLE)

    def get_modal_body(self):
        """Get the modal body element.

        Returns:
            Locator: The locator for the modal body element.
        """
        logger.info("Getting modal body element")
        return self.get_modal().get_by_text(self.MODAL_BODY)
