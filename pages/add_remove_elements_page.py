"""Page object for the Add/Remove Elements page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class AddRemoveElementsPage(BasePage):
    """Page object for the Add/Remove Elements page."""

    # Locators
    HEADER_LOCATOR = "Add/Remove Elements"
    ADD_ELEMENT_BUTTON_LOCATOR = "Add Element"
    ELEMENTS_CONTAINER = "#elements"
    ELEMENT_TEXT = re.compile(r"Element \d+")

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        return self.page.get_by_role("heading", name=self.HEADER_LOCATOR)

    def get_add_element_button(self):
        """Get the Add Element button element.

        Returns:
            Locator: The locator for the Add Element button.
        """
        return self.page.get_by_role("button", name=self.ADD_ELEMENT_BUTTON_LOCATOR)

    def click_add_element_button(self):
        """Click the Add Element button.

        Returns:
            None
        """
        self.get_add_element_button().click()
        logger.info("Clicked Add Element button")

    def get_added_element(self, index):
        """Get an added element by its index (1-based).

        Args:
            index (int): The 1-based index of the added element.

        Returns:
            Locator: The locator for the added element.
        """
        return self.page.get_by_text(self.ELEMENT_TEXT).nth(index - 1)

    def get_delete_button(self, index):
        """Get a delete button by its index (1-based).

        Args:
            index (int): The 1-based index of the delete button.

        Returns:
            Locator: The locator for the delete button.
        """
        return self.page.locator(self.ELEMENTS_CONTAINER).get_by_role("button").nth(index - 1)

    def click_delete_button(self, index):
        """Click a delete button by its index (1-based).

        Args:
            index (int): The 1-based index of the delete button to click.

        Returns:
            None
        """
        self.get_delete_button(index).click()
        logger.info("Clicked Delete button %s", index)

    def get_delete_buttons(self):
        """Get all delete button elements.

        Returns:
            Locator: The locator for all delete buttons.
        """
        return self.page.locator(self.ELEMENTS_CONTAINER).get_by_role("button")

    def get_delete_buttons_count(self):
        """Get the count of delete buttons currently on the page.

        Returns:
            int: The number of delete buttons.
        """
        return self.get_delete_buttons().count()
