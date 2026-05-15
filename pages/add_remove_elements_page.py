"""Page object for the Add/Remove Elements page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class AddRemoveElementsPage(BasePage):
    """Page object for the Add/Remove Elements page."""

    # Locators
    HEADER_LOCATOR = "//span[.='Add/Remove Elements'] | //h1[.='Add/Remove Elements']"
    ADD_ELEMENT_BUTTON_LOCATOR = "//button[.='Add Element']"
    DELETE_BUTTON_LOCATOR = "//div[contains(text(), 'Element ')]/parent::div/button"

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        return self.page.locator(self.HEADER_LOCATOR)

    def get_add_element_button(self):
        """Get the Add Element button element.

        Returns:
            Locator: The locator for the Add Element button.
        """
        return self.page.locator(self.ADD_ELEMENT_BUTTON_LOCATOR)

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
        return self.page.locator(f"(//div[contains(text(), 'Element ')])[{index}]")

    def get_delete_button(self, index):
        """Get a delete button by its index (1-based).

        Args:
            index (int): The 1-based index of the delete button.

        Returns:
            Locator: The locator for the delete button.
        """
        return self.page.locator(f"({self.DELETE_BUTTON_LOCATOR})[{index}]")

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
        return self.page.locator(self.DELETE_BUTTON_LOCATOR)

    def get_delete_buttons_count(self):
        """Get the count of delete buttons currently on the page.

        Returns:
            int: The number of delete buttons.
        """
        return self.page.locator(self.DELETE_BUTTON_LOCATOR).count()
