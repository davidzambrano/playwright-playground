"""Page object for the Challenging DOM page."""

import logging

from playwright.sync_api import expect

from .base_page import BasePage

logger = logging.getLogger(__name__)


class ChallengingDomPage(BasePage):
    """
    Page object for the Challenging DOM page.
    Provides locators and actions for buttons, canvas, and table.
    """

    # Locators
    DESCRIPTION_LOCATOR = (
        "//p[contains(@class, 'text-muted-foreground') and "
        "contains(text(), 'random text and colors')]"
    )
    BUTTONS_LOCATOR = "//button[contains(@class, 'w-48')]"
    CANVAS_LOCATOR = "//canvas"
    TABLE_LOCATOR = "//table"
    TABLE_ROW_LOCATOR = "//table//tbody//tr"

    def get_description(self):
        """Get the page description element."""
        logger.info("Getting Challenging DOM page description element")
        return self.page.locator(self.DESCRIPTION_LOCATOR)

    def get_buttons(self):
        """Get all random buttons."""
        logger.info("Getting all random buttons")
        return self.page.locator(self.BUTTONS_LOCATOR)

    def get_canvas(self):
        """Get the canvas element displaying the answer."""
        logger.info("Getting canvas element")
        return self.page.locator(self.CANVAS_LOCATOR)

    def get_table(self):
        """Get the table element."""
        logger.info("Getting table element")
        return self.page.locator(self.TABLE_LOCATOR)

    def get_table_rows(self):
        """Get all table row elements."""
        logger.info("Getting all table row elements")
        return self.page.locator(self.TABLE_ROW_LOCATOR)

    def delete_table_row(self, row_index: int):
        """
        Clicks the delete button for a given row index (0-based).
        Relies on test assertions to verify row count changes.
        """
        logger.info("Clicking delete button for row at index %s", row_index)
        row_to_delete = self.get_table_rows().nth(row_index)
        delete_btn = row_to_delete.get_by_role("button", name="Delete")
        expect(delete_btn).to_be_visible()
        delete_btn.click()
