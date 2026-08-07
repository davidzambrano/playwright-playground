"""Page object for the Key Presses page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class KeyPressesPage(BasePage):
    """
    Page object for the Key Presses page.
    Provides locators and actions for keyboard interaction testing.
    """

    # Locators
    PAGE_HEADING = re.compile("Key Presses")
    INSTRUCTION_TEXT = re.compile("Key presses are often used")
    INPUT_FIELD = "#key-input"
    RESULT_TEXT = re.compile("You entered:")
    RESULT_VALUE = "span.text-primary"

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

    def get_input_field(self):
        """Get the input field element.

        Returns:
            Locator: The locator for the input field element.
        """
        logger.info("Getting input field element")
        return self.page.locator(self.INPUT_FIELD)

    def get_result_text(self):
        """Get the result text element.

        Returns:
            Locator: The locator for the result text element.
        """
        logger.info("Getting result text element")
        return self.page.get_by_text(self.RESULT_TEXT)

    def get_result_value(self):
        """Get the result value element.

        Returns:
            Locator: The locator for the result value element.
        """
        logger.info("Getting result value element")
        return self.page.locator(self.RESULT_VALUE)

    def press_key_in_input(self, key):
        """Press a key in the input field.

        Args:
            key (str): The key to press (e.g., 'A', 'Enter', 'Space').

        Returns:
            None
        """
        logger.info("Pressing key '%s' in input field", key)
        self.get_input_field().press(key)

    def type_in_input(self, text):
        """Type text in the input field.

        Args:
            text (str): The text to type.

        Returns:
            None
        """
        logger.info("Typing '%s' in input field", text)
        self.get_input_field().type(text)
