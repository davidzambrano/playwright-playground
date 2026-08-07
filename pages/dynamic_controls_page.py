"""Page object for the Dynamic Controls page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DynamicControlsPage(BasePage):
    """
    Page object for the Dynamic Controls page.
    Provides locators and actions for dynamic element addition/removal and enable/disable patterns.
    """

    # Locators
    PAGE_HEADING = re.compile("Dynamic Controls")
    CHECKBOX = "A checkbox"
    TOGGLE_CHECKBOX_BUTTON = re.compile("Checkbox")
    TEXT_INPUT = "This can be enabled or disabled"
    TOGGLE_INPUT_BUTTON = re.compile("Input")

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_checkbox(self):
        """Get the checkbox element.

        Returns:
            Locator: The locator for the checkbox element.
        """
        logger.info("Getting checkbox element")
        return self.page.get_by_role("checkbox", name=self.CHECKBOX)

    def get_toggle_checkbox_button(self):
        """Get the toggle checkbox button element (Remove/Add).

        Returns:
            Locator: The locator for the toggle checkbox button element.
        """
        logger.info("Getting toggle checkbox button element")
        return self.page.get_by_role("button", name=self.TOGGLE_CHECKBOX_BUTTON)

    def get_text_input(self):
        """Get the text input element.

        Returns:
            Locator: The locator for the text input element.
        """
        logger.info("Getting text input element")
        return self.page.get_by_placeholder(self.TEXT_INPUT)

    def get_toggle_input_button(self):
        """Get the toggle input button element (Enable/Disable).

        Returns:
            Locator: The locator for the toggle input button element.
        """
        logger.info("Getting toggle input button element")
        return self.page.get_by_role("button", name=self.TOGGLE_INPUT_BUTTON)

    def click_toggle_checkbox_button(self):
        """Click the toggle checkbox button to remove or add the checkbox.

        Returns:
            None
        """
        logger.info("Clicking toggle checkbox button")
        self.get_toggle_checkbox_button().click()

    def click_toggle_input_button(self):
        """Click the toggle input button to enable or disable the text input.

        Returns:
            None
        """
        logger.info("Clicking toggle input button")
        self.get_toggle_input_button().click()
