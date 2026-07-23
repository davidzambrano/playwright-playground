"""Base page object for pages with modal dialogs."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class ModalPage(BasePage):
    """Base page class for pages that contain modal dialogs."""

    # Common modal locators (to be overridden by child classes if needed)
    MODAL = "[role='dialog']"
    MODAL_TITLE = "//h2"
    MODAL_BODY = "//*[contains(@class, 'modal-body') or contains(@class, 'modal')]"
    CLOSE_BUTTON = "//button[normalize-space()='Close' and not(contains(@class, 'absolute'))]"

    def get_modal(self):
        """Get the modal element.

        Returns:
            Locator: The locator for the modal element.
        """
        logger.info("Getting modal element")
        return self.page.locator(self.MODAL)

    def get_modal_title(self):
        """Get the modal title element.

        Returns:
            Locator: The locator for the modal title element.
        """
        logger.info("Getting modal title element")
        return self.page.locator(self.MODAL_TITLE)

    def get_modal_body(self):
        """Get the modal body element.

        Returns:
            Locator: The locator for the modal body element.
        """
        logger.info("Getting modal body element")
        return self.page.locator(self.MODAL_BODY)

    def get_close_button(self):
        """Get the Close button element.

        Returns:
            Locator: The locator for the Close button element.
        """
        logger.info("Getting Close button element")
        return self.page.locator(self.CLOSE_BUTTON)

    def click_close_button(self):
        """Click the Close button on the modal.

        Returns:
            None
        """
        logger.info("Clicking Close button on modal")
        self.get_close_button().click()

    def wait_for_modal(self, timeout: int = 10000):
        """Wait for the modal to become visible.

        Args:
            timeout (int): Maximum time to wait in milliseconds. Defaults to 10000.

        Returns:
            None
        """
        logger.info("Waiting for modal to appear")
        self.get_modal().wait_for(state="visible", timeout=timeout)
