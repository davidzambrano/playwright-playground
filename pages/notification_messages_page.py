"""Page object for the Notification Messages page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class NotificationMessagesPage(BasePage):
    """Page object for the Notification Messages page."""

    # Locators
    PAGE_HEADING = re.compile("Notification Messages")
    INSTRUCTION_TEXT = re.compile("message displayed is a notification message")
    CLICK_HERE_LINK = "Click here to load a new message."
    NOTIFICATION_ALERT = "[role='alert']:not([id='__next-route-announcer__'])"
    POSSIBLE_MESSAGES = [
        "Action successful.",
        "Action unsuccessful, please try again.",
        "Action completed.",
        "Something went wrong.",
    ]

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
        """Get the Click here to load a new message link element.

        Returns:
            Locator: The locator for the Click here link element.
        """
        logger.info("Getting Click here link element")
        return self.page.get_by_role("button", name=self.CLICK_HERE_LINK)

    def get_notification_alert(self):
        """Get the notification alert element.

        Returns:
            Locator: The locator for the notification alert element.
        """
        logger.info("Getting notification alert element")
        return self.page.locator(self.NOTIFICATION_ALERT)

    def get_notification_message(self):
        """Get the notification message text element.

        Returns:
            Locator: The locator for the notification message text element.
        """
        logger.info("Getting notification message text element")
        return self.get_notification_alert().locator("div")

    def get_close_button(self):
        """Get the notification close button element.

        Returns:
            Locator: The locator for the notification close button element.
        """
        logger.info("Getting notification close button element")
        return self.get_notification_alert().get_by_role("button")

    def click_click_here(self):
        """Click the Click here link to load a new message.

        Returns:
            None
        """
        logger.info("Clicking Click here link")
        self.get_click_here_link().click()

    def click_close_button(self):
        """Click the close button on the notification.

        Returns:
            None
        """
        logger.info("Clicking notification close button")
        self.get_close_button().click()
