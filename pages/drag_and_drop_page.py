"""Page object for the Drag and Drop page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DragAndDropPage(BasePage):
    """
    Page object for the Drag and Drop page.
    Provides locators and actions for drag and drop interactions.
    """

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Drag and Drop')]"
    DRAGGABLE_ITEM = "#draggable"
    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"
    COLUMN_C = "#column-c"
    COLUMN_D = "#column-d"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_draggable_item(self):
        """Get the draggable item element.

        Returns:
            Locator: The locator for the draggable item element.
        """
        logger.info("Getting draggable item element")
        return self.page.locator(self.DRAGGABLE_ITEM)

    def get_column_a(self):
        """Get column A drop zone element.

        Returns:
            Locator: The locator for column A drop zone element.
        """
        logger.info("Getting column A drop zone element")
        return self.page.locator(self.COLUMN_A)

    def get_column_b(self):
        """Get column B drop zone element.

        Returns:
            Locator: The locator for column B drop zone element.
        """
        logger.info("Getting column B drop zone element")
        return self.page.locator(self.COLUMN_B)

    def get_column_c(self):
        """Get column C drop zone element.

        Returns:
            Locator: The locator for column C drop zone element.
        """
        logger.info("Getting column C drop zone element")
        return self.page.locator(self.COLUMN_C)

    def get_column_d(self):
        """Get column D drop zone element.

        Returns:
            Locator: The locator for column D drop zone element.
        """
        logger.info("Getting column D drop zone element")
        return self.page.locator(self.COLUMN_D)

    def drag_item_to_column(self, column_locator):
        """Drag the draggable item to a specific column.

        Args:
            column_locator (Locator): The locator for the target column.

        Returns:
            None
        """
        logger.info("Dragging item to column")
        self.get_draggable_item().drag_to(column_locator)
