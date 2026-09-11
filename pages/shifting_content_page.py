"""Page object for the Shifting Content page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class ShiftingContentPage(BasePage):
    """Page object for the Shifting Content page.

    Provides locators and actions for the three example sections
    (Menu Element, An image, List) that shift position on each page load.
    """

    # Locators
    PAGE_HEADING = re.compile(r"Shifting Content")
    INSTRUCTION_TEXT = re.compile(r"shifting a few pixels")
    EXAMPLE_1_HEADING = re.compile(r"Example 1: Menu Element")
    EXAMPLE_2_HEADING = re.compile(r"Example 2: An image")
    EXAMPLE_3_HEADING = re.compile(r"Example 3: List")

    # Menu buttons
    MENU_ITEM_HOME = "Home"
    MENU_ITEM_ABOUT = "About"
    MENU_ITEM_PORTFOLIO = "Portfolio"
    MENU_ITEM_CONTACT_US = "Contact Us"

    # Image
    SHIFTING_IMAGE_ALT = "A random shifting image"

    # List items in Example 3
    LIST_ITEM_LOCATOR = "ul li"

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

    def get_example_1_heading(self):
        """Get the Example 1 (Menu Element) heading element.

        Returns:
            Locator: The locator for the Example 1 heading element.
        """
        logger.info("Getting Example 1 heading element")
        return self.page.get_by_role("heading", name=self.EXAMPLE_1_HEADING)

    def get_example_2_heading(self):
        """Get the Example 2 (An image) heading element.

        Returns:
            Locator: The locator for the Example 2 heading element.
        """
        logger.info("Getting Example 2 heading element")
        return self.page.get_by_role("heading", name=self.EXAMPLE_2_HEADING)

    def get_example_3_heading(self):
        """Get the Example 3 (List) heading element.

        Returns:
            Locator: The locator for the Example 3 heading element.
        """
        logger.info("Getting Example 3 heading element")
        return self.page.get_by_role("heading", name=self.EXAMPLE_3_HEADING)

    def get_menu_button(self, label):
        """Get a menu button element by its label.

        Args:
            label (str): The text label of the menu button.

        Returns:
            Locator: The locator for the menu button element.
        """
        logger.info("Getting menu button: %s", label)
        return self.page.get_by_role("button", name=label, exact=True)

    def get_portfolio_menu_button(self):
        """Get the Portfolio menu button element.

        Returns:
            Locator: The locator for the Portfolio menu button element.
        """
        logger.info("Getting Portfolio menu button element")
        return self.get_menu_button(self.MENU_ITEM_PORTFOLIO)

    def click_portfolio_menu_button(self):
        """Click the Portfolio menu button.

        The menu element shifts a few pixels on each page load, so this
        method tests the ability to click a menu item regardless of its
        exact pixel position.

        Returns:
            None
        """
        logger.info("Clicking Portfolio menu button")
        self.get_portfolio_menu_button().click()

    def get_shifting_image(self):
        """Get the shifting image element.

        Located by its alt attribute, not by position, to test
        resilience to minor layout shifts.

        Returns:
            Locator: The locator for the shifting image element.
        """
        logger.info("Getting shifting image element")
        return self.page.get_by_role("img", name=self.SHIFTING_IMAGE_ALT)

    def get_list_items(self):
        """Get all list item elements in the Example 3 section.

        Returns:
            Locator: The locator for all list item elements.
        """
        logger.info("Getting list items")
        return self.page.locator(self.LIST_ITEM_LOCATOR)

    def get_list_item_count(self):
        """Get the count of list items.

        Returns:
            int: The number of list items currently on the page.
        """
        logger.info("Getting list item count")
        self.get_list_items().first.wait_for(state="visible")
        return self.get_list_items().count()
