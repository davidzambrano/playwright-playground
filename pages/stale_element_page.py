"""Page object for the Stale Element page."""

import logging

from .modal_page import ModalPage

logger = logging.getLogger(__name__)


class StaleElementPage(ModalPage):
    """
    Page object for the Stale Element page.
    Provides locators and actions for testing stale element handling.
    """

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Stale Element')]"
    STALE_BUTTON = "//button[@id='stale-button']"
    SUCCESS_MESSAGE = "//p[contains(text(), 'You managed to click the button')]"
    SUCCESS_DESCRIPTION = (
        "//p[contains(text(), 'You defeated the StaleElementReferenceException monster')]"
    )

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_stale_button(self):
        """Get the stale button element.

        Returns:
            Locator: The locator for the stale button element.
        """
        logger.info("Getting stale button element")
        return self.page.locator(self.STALE_BUTTON)

    def click_stale_button(self):
        """Click the stale button, retrying if it becomes stale.

        Playwright auto-retries on stale element references, so this
        should succeed as long as the button is clicked before the
        150ms re-render interval.

        Returns:
            None
        """
        logger.info("Clicking stale button")
        self.get_stale_button().click()

    def get_success_message(self):
        """Get the success message element.

        Returns:
            Locator: The locator for the success message element.
        """
        logger.info("Getting success message element")
        return self.page.locator(self.SUCCESS_MESSAGE)

    def get_success_description(self):
        """Get the success description element.

        Returns:
            Locator: The locator for the success description element.
        """
        logger.info("Getting success description element")
        return self.page.locator(self.SUCCESS_DESCRIPTION)

    def is_success_message_visible(self):
        """Check if the success message is visible.

        Returns:
            bool: True if the success message is visible, False otherwise.
        """
        logger.info("Checking if success message is visible")
        return self.get_success_message().is_visible()
