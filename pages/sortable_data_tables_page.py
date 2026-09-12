"""Page object for the Sortable Data Tables page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class SortableDataTablesPage(BasePage):
    """Page object for the Sortable Data Tables page.

    The page renders two identical tables (Example 1 without id/class
    attributes, Example 2 with them). Each table has sortable column
    headers (Last Name, First Name, Email, Due, Website) rendered as
    buttons showing an indicator for the active sort column.
    """

    # Locators
    PAGE_HEADING = re.compile(r"Sortable Data Tables")
    INSTRUCTION_TEXT = re.compile(r"sortable -- sometimes with actions")
    EXAMPLE_1_HEADING = re.compile(r"Example 1")
    EXAMPLE_2_HEADING = re.compile(r"Example 2")

    # Both tables on the page, in DOM order (Example 1, then Example 2)
    TABLES_LOCATOR = "table"
    TABLE_ROW_LOCATOR = "tbody tr"

    # Header button label -> 1-based column index within a table row
    COLUMN_INDEX = {
        "Last Name": 1,
        "First Name": 2,
        "Email": 3,
        "Due": 4,
        "Web Site": 5,
    }

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
        """Get the Example 1 heading element.

        Returns:
            Locator: The locator for the Example 1 heading element.
        """
        logger.info("Getting Example 1 heading element")
        return self.page.get_by_role("heading", name=self.EXAMPLE_1_HEADING)

    def get_example_2_heading(self):
        """Get the Example 2 heading element.

        Returns:
            Locator: The locator for the Example 2 heading element.
        """
        logger.info("Getting Example 2 heading element")
        return self.page.get_by_role("heading", name=self.EXAMPLE_2_HEADING)

    def get_tables(self):
        """Get both data tables in DOM order (Example 1, then Example 2).

        Returns:
            Locator: The locator matching both table elements.
        """
        logger.info("Getting both data tables")
        return self.page.locator(self.TABLES_LOCATOR)

    def get_table(self, table_index: int = 0):
        """Get a single data table by index (0 for Example 1, 1 for Example 2).

        Args:
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            Locator: The locator for the requested table element.
        """
        logger.info("Getting data table at index %s", table_index)
        return self.get_tables().nth(table_index)

    def get_header_button(self, label: str, table_index: int = 0):
        """Get a sortable column header button within a table.

        Args:
            label (str): The header label (e.g. "First Name").
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            Locator: The locator for the header button element.
        """
        logger.info("Getting '%s' header button in table %s", label, table_index)
        table = self.get_table(table_index)
        return table.get_by_role("button", name=re.compile(label))

    def click_header_button(self, label: str, table_index: int = 0):
        """Click a sortable column header button within a table.

        Args:
            label (str): The header label (e.g. "First Name").
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            None

        """
        logger.info("Clicking '%s' header button in table %s", label, table_index)
        self.get_header_button(label, table_index).click()

    def get_rows(self, table_index: int = 0):
        """Get all data rows of a table.

        Args:
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            Locator: The locator matching the table row elements.
        """
        logger.info("Getting rows of table %s", table_index)
        return self.get_table(table_index).locator(self.TABLE_ROW_LOCATOR)

    def get_column_cells(self, label: str, table_index: int = 0):
        """Get all data cells of a column within a table.

        Args:
            label (str): The header label identifying the column.
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            Locator: The locator matching the column cell elements.
        """
        column = self.COLUMN_INDEX[label]
        logger.info("Getting '%s' column cells in table %s", label, table_index)
        return self.get_rows(table_index).locator(f"td:nth-child({column})")

    def get_column_values(self, label: str, table_index: int = 0) -> list:
        """Get the text values of a column within a table.

        Args:
            label (str): The header label identifying the column.
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            list: The text content of each cell in the column.
        """
        logger.info("Getting '%s' column values in table %s", label, table_index)
        self.get_rows(table_index).first.wait_for(state="visible")
        return self.get_column_cells(label, table_index).all_text_contents()

    def get_row_by_text(self, row_text: str, table_index: int = 0):
        """Get the row containing the given text within a table.

        Args:
            row_text (str): Text identifying the row (e.g. "Jason").
            table_index (int): 0 for Example 1, 1 for Example 2.

        Returns:
            Locator: The locator for the matching row element.
        """
        logger.info("Getting row containing '%s' in table %s", row_text, table_index)
        return self.get_rows(table_index).filter(has_text=row_text)
