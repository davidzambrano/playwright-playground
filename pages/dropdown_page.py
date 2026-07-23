"""Page object for the Dropdown page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DropdownPage(BasePage):
    """
    Page object for the Dropdown page.
    Provides locators and actions for dropdown and combobox interactions.
    """

    # Locators
    SIMPLE_DROPDOWN_HEADING = "//h3[contains(text(), 'Simple Dropdown')]"
    SEARCHABLE_COMBOBOX_HEADING = "//h3[contains(text(), 'Searchable Combobox')]"
    SIMPLE_DROPDOWN_TRIGGER = "//button[@role='combobox' and contains(., 'Select a fruit')]"
    SIMPLE_DROPDOWN_VALUE = "//span[contains(@class, 'SelectValue')]"
    SELECTION_TEXT = "//p[contains(text(), 'You selected:')]"
    COMBOBOX_INPUT = "//input[@placeholder='Search framework...']"
    NO_RESULTS_TEXT = "//p[contains(text(), 'No framework found')]"

    def get_simple_dropdown_heading(self):
        """Get the Simple Dropdown heading element."""
        logger.info("Getting Simple Dropdown heading element")
        return self.page.locator(self.SIMPLE_DROPDOWN_HEADING)

    def get_searchable_combobox_heading(self):
        """Get the Searchable Combobox heading element."""
        logger.info("Getting Searchable Combobox heading element")
        return self.page.locator(self.SEARCHABLE_COMBOBOX_HEADING)

    def get_simple_dropdown_trigger(self):
        """Get the simple dropdown trigger button."""
        logger.info("Getting simple dropdown trigger element")
        return self.page.locator(self.SIMPLE_DROPDOWN_TRIGGER)

    def click_simple_dropdown_trigger(self):
        """Click the simple dropdown trigger to open it."""
        trigger = self.get_simple_dropdown_trigger()
        trigger.scroll_into_view_if_needed()
        logger.info("Clicking simple dropdown trigger")
        trigger.click()

    def get_simple_dropdown_option(self, value):
        """Get a specific option from the simple dropdown.

        Args:
            value (str): The value attribute of the option.

        Returns:
            Locator: The locator for the option element.
        """
        logger.info("Getting simple dropdown option with value: %s", value)
        # Capitalize first letter to match the actual option text (Apple, Banana, etc.)
        display_value = value.capitalize()
        return self.page.get_by_role("option", name=display_value, exact=True)

    def get_selection_text(self):
        """Get the selection confirmation text element."""
        logger.info("Getting selection text element")
        return self.page.locator(self.SELECTION_TEXT)

    def get_combobox_trigger(self):
        """Get the searchable combobox trigger button."""
        logger.info("Getting combobox trigger element")
        # There are two combobox buttons: fruit selector (1st index 0)
        # and framework selector (2nd index 1). Get the second one.
        return self.page.locator("//button[@role='combobox']").nth(1)

    def click_combobox_trigger(self):
        """Click the combobox trigger to open it."""
        trigger = self.get_combobox_trigger()
        trigger.scroll_into_view_if_needed()
        logger.info("Clicking combobox trigger")
        trigger.click()

    def get_combobox_input(self):
        """Get the combobox search input field."""
        logger.info("Getting combobox input element")
        return self.page.locator(self.COMBOBOX_INPUT)

    def get_combobox_option(self, label):
        """Get a specific option from the searchable combobox.

        Args:
            label (str): The label text of the option.

        Returns:
            Locator: The locator for the option button element.
        """
        logger.info("Getting combobox option with label: %s", label)
        # Options are rendered as buttons with class="font-normal"
        return self.page.locator(
            f"//button[contains(@class, 'font-normal') and contains(., '{label}')]"
        )

    def get_no_results_text(self):
        """Get the no results text element."""
        logger.info("Getting no results text element")
        return self.page.locator(self.NO_RESULTS_TEXT)

    def select_simple_dropdown_option(self, value):
        """Select an option from the simple dropdown.

        Args:
            value (str): The value attribute of the option to select.

        Returns:
            None
        """
        logger.info("Selecting option from simple dropdown: %s", value)
        self.click_simple_dropdown_trigger()
        option = self.get_simple_dropdown_option(value)
        logger.info("Waiting for option to be visible")
        option.wait_for(state="visible")
        logger.info("Clicking dropdown option: %s", value)
        option.click()

    def select_combobox_option(self, label):
        """Select an option from the searchable combobox.

        Args:
            label (str): The label text of the option to select.

        Returns:
            None
        """
        logger.info("Selecting option from combobox: %s", label)
        self.click_combobox_trigger()
        option = self.get_combobox_option(label)
        option.wait_for(state="visible")
        option.click()

    def search_combobox(self, search_term):
        """Type a search term in the combobox input.

        Args:
            search_term (str): The search term to type.

        Returns:
            None
        """
        logger.info("Searching combobox with term: %s", search_term)
        self.get_combobox_input().fill(search_term)
