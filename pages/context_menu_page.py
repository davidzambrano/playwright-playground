"""Page object for the Context Menu page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class ContextMenuPage(BasePage):
    """
    Page object for the Context Menu page.
    Provides locators and actions for custom context menu interactions.
    """

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Context Menu')]"
    HOTSPOT_AREA = "//p[contains(text(), 'Right-click me!')]"
    CONTEXT_MENU = "//ul"
    MENU_ITEM_SHARE = "//li[contains(text(), 'Share')]"
    SUB_MENU = "//ul[li[contains(text(), 'Email')]]"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_hotspot_area(self):
        """Get the hot-spot area element for right-clicking.

        Returns:
            Locator: The locator for the hot-spot area element.
        """
        logger.info("Getting hot-spot area element")
        return self.page.locator(self.HOTSPOT_AREA)

    def get_context_menu(self):
        """Get the custom context menu element.

        Returns:
            Locator: The locator for the context menu element.
        """
        logger.info("Getting context menu element")
        return self.page.locator(self.CONTEXT_MENU)

    def get_share_menu_item(self):
        """Get the Share menu item element.

        Returns:
            Locator: The locator for the Share menu item element.
        """
        logger.info("Getting Share menu item element")
        return self.page.locator(self.MENU_ITEM_SHARE)

    def get_sub_menu(self):
        """Get the sub-menu element.

        Returns:
            Locator: The locator for the sub-menu element.
        """
        logger.info("Getting sub-menu element")
        return self.page.locator(self.SUB_MENU)

    def right_click_hotspot(self):
        """Perform a right-click on the hot-spot area to trigger the context menu.

        Returns:
            None
        """
        logger.info("Right-clicking on hot-spot area")
        self.get_hotspot_area().click(button="right")

    def left_click_outside_menu(self):
        """Left-click outside the context menu to dismiss it.

        Returns:
            None
        """
        logger.info("Left-clicking outside context menu to dismiss it")
        self.get_page_heading().click()

    def hover_over_share_item(self):
        """Hover over the Share menu item to trigger the sub-menu.

        Returns:
            None
        """
        logger.info("Hovering over Share menu item")
        self.get_share_menu_item().hover()
