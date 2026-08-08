"""Page object for the Menus page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class MenusPage(BasePage):
    """Page object for the Menus page."""

    # pylint: disable=R0904
    # MenusPage has many menu items, each requiring getter and clicker methods
    # Following the project's Page Object Model pattern with clear separation of concerns

    # Locators
    PAGE_HEADING = re.compile("Menus")
    INSTRUCTION_TEXT = re.compile("menu system that opens on hover")
    ENABLED_TRIGGER = "Enabled"
    DISABLED_TRIGGER = "Disabled"
    MENU_ITEM_COPY = "Copy"
    MENU_ITEM_PASTE = "Paste"
    MENU_ITEM_PREFERENCES = "Preferences"
    MENU_ITEM_BACK_TO_MENU = "Back to Menu"
    SUBMENU_TRIGGER = "Downloads"
    SUBMENU_ITEM_PDF = "PDF"
    SUBMENU_ITEM_CSV = "CSV"
    SUBMENU_ITEM_EXCEL = "Excel"
    TOAST_TITLE = "Action Triggered"

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

    def get_enabled_trigger(self):
        """Get the Enabled menu trigger element.

        Returns:
            Locator: The locator for the Enabled menu trigger element.
        """
        logger.info("Getting Enabled menu trigger element")
        return self.page.get_by_role("menuitem", name=self.ENABLED_TRIGGER)

    def get_disabled_trigger(self):
        """Get the Disabled menu trigger element.

        Returns:
            Locator: The locator for the Disabled menu trigger element.
        """
        logger.info("Getting Disabled menu trigger element")
        return self.page.get_by_role("menuitem", name=self.DISABLED_TRIGGER)

    def get_menu_item(self, item_name):
        """Get a menu item element by name.

        Args:
            item_name (str): The name of the menu item.

        Returns:
            Locator: The locator for the menu item element.
        """
        logger.info("Getting menu item: %s", item_name)
        return self.page.get_by_role("menuitem", name=item_name, exact=True)

    def get_copy_menu_item(self):
        """Get the Copy menu item element.

        Returns:
            Locator: The locator for the Copy menu item element.
        """
        logger.info("Getting Copy menu item element")
        return self.get_menu_item(self.MENU_ITEM_COPY)

    def get_paste_menu_item(self):
        """Get the Paste menu item element.

        Returns:
            Locator: The locator for the Paste menu item element.
        """
        logger.info("Getting Paste menu item element")
        return self.get_menu_item(self.MENU_ITEM_PASTE)

    def get_preferences_menu_item(self):
        """Get the Preferences menu item element.

        Returns:
            Locator: The locator for the Preferences menu item element.
        """
        logger.info("Getting Preferences menu item element")
        return self.get_menu_item(self.MENU_ITEM_PREFERENCES)

    def get_back_to_menu_item(self):
        """Get the Back to Menu item element.

        Returns:
            Locator: The locator for the Back to Menu item element.
        """
        logger.info("Getting Back to Menu item element")
        return self.get_menu_item(self.MENU_ITEM_BACK_TO_MENU)

    def get_submenu_trigger(self):
        """Get the Downloads submenu trigger element.

        Returns:
            Locator: The locator for the Downloads submenu trigger element.
        """
        logger.info("Getting Downloads submenu trigger element")
        return self.get_menu_item(self.SUBMENU_TRIGGER)

    def get_submenu_item(self, item_name):
        """Get a submenu item element by name.

        Args:
            item_name (str): The name of the submenu item.

        Returns:
            Locator: The locator for the submenu item element.
        """
        logger.info("Getting submenu item: %s", item_name)
        return self.page.get_by_role("menuitem", name=item_name, exact=True)

    def get_pdf_submenu_item(self):
        """Get the PDF submenu item element.

        Returns:
            Locator: The locator for the PDF submenu item element.
        """
        logger.info("Getting PDF submenu item element")
        return self.get_submenu_item(self.SUBMENU_ITEM_PDF)

    def get_csv_submenu_item(self):
        """Get the CSV submenu item element.

        Returns:
            Locator: The locator for the CSV submenu item element.
        """
        logger.info("Getting CSV submenu item element")
        return self.get_submenu_item(self.SUBMENU_ITEM_CSV)

    def get_excel_submenu_item(self):
        """Get the Excel submenu item element.

        Returns:
            Locator: The locator for the Excel submenu item element.
        """
        logger.info("Getting Excel submenu item element")
        return self.get_submenu_item(self.SUBMENU_ITEM_EXCEL)

    def get_toast(self):
        """Get the toast notification element.

        Returns:
            Locator: The locator for the toast notification element.
        """
        logger.info("Getting toast notification element")
        return self.page.get_by_text(self.TOAST_TITLE)

    def hover_over_enabled_trigger(self):
        """Hover over the Enabled menu trigger to open the menu.

        Returns:
            None
        """
        logger.info("Hovering over Enabled menu trigger")
        self.get_enabled_trigger().hover()

    def click_copy_menu_item(self):
        """Click the Copy menu item.

        Returns:
            None
        """
        logger.info("Clicking Copy menu item")
        self.get_copy_menu_item().click()

    def click_paste_menu_item(self):
        """Click the Paste menu item.

        Returns:
            None
        """
        logger.info("Clicking Paste menu item")
        self.get_paste_menu_item().click()

    def click_preferences_menu_item(self):
        """Click the Preferences menu item.

        Returns:
            None
        """
        logger.info("Clicking Preferences menu item")
        self.get_preferences_menu_item().click()

    def click_back_to_menu_item(self):
        """Click the Back to Menu item.

        Returns:
            None
        """
        logger.info("Clicking Back to Menu item")
        self.get_back_to_menu_item().click()

    def hover_over_submenu_trigger(self):
        """Hover over the Downloads submenu trigger.

        Returns:
            None
        """
        logger.info("Hovering over Downloads submenu trigger")
        self.get_submenu_trigger().hover()

    def click_pdf_submenu_item(self):
        """Click the PDF submenu item.

        Returns:
            None
        """
        logger.info("Clicking PDF submenu item")
        self.get_pdf_submenu_item().click()

    def click_csv_submenu_item(self):
        """Click the CSV submenu item.

        Returns:
            None
        """
        logger.info("Clicking CSV submenu item")
        self.get_csv_submenu_item().click()

    def click_excel_submenu_item(self):
        """Click the Excel submenu item.

        Returns:
            None
        """
        logger.info("Clicking Excel submenu item")
        self.get_excel_submenu_item().click()
