from playwright.sync_api import Page
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class AddRemoveElementsPage(BasePage):
    """Page object for the Add/Remove Elements page."""
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.header_locator = "//span[.='Add/Remove Elements'] | //h1[.='Add/Remove Elements']"
        self.add_element_button_locator = "//button[.='Add Element']"
        self.delete_button_locator = "//div[contains(text(), 'Element ')]/parent::div/button"

    def get_header(self):
        """Get the page header element.

        Returns:
            Locator: The locator for the page header element.
        """
        return self.page.locator(self.header_locator)

    def get_add_element_button(self):
        """Get the Add Element button element.

        Returns:
            Locator: The locator for the Add Element button.
        """
        return self.page.locator(self.add_element_button_locator)


    def click_add_element_button(self):
        """Click the Add Element button.

        Returns:
            None
        """
        button = self.get_add_element_button()
        button.click()
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
        return self.page.locator(f"({self.delete_button_locator})[{index}]")


    def click_delete_button(self, index):
        """Click a delete button by its index (1-based).

        Args:
            index (int): The 1-based index of the delete button to click.

        Returns:
            None
        """
        button = self.get_delete_button(index)
        button.click()
        logger.info(f"Clicked Delete button {index}")

    def get_delete_buttons_count(self):
        """Get the count of delete buttons currently on the page.

        Returns:
            int: The number of delete buttons.
        """
        return self.page.locator(self.delete_button_locator).count()
