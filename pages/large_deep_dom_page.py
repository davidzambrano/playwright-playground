"""Page object for the Large & Deep DOM page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class LargeDeepDomPage(BasePage):
    """Page object for the Large & Deep DOM page."""

    PAGE_HEADING = re.compile(r"Large & Deep DOM")
    NO_SIBLINGS_CONTAINER = "#no-siblings"
    NESTED_SIBLINGS_CONTAINER = "#siblings"
    DEEPEST_LEVEL = '[id="level-50"]'

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_no_siblings_container(self):
        """Get the no-siblings container element.

        Returns:
            Locator: The locator for the no-siblings container element.
        """
        logger.info("Getting no-siblings container element")
        return self.page.locator(self.NO_SIBLINGS_CONTAINER)

    def get_deepest_level(self):
        """Get the deepest nested level element.

        Returns:
            Locator: The locator for the deepest nested element.
        """
        logger.info("Getting deepest nested level element")
        return self.page.locator(self.DEEPEST_LEVEL)

    def get_nested_siblings_container(self):
        """Get the nested siblings container element.

        Returns:
            Locator: The locator for the nested siblings container element.
        """
        logger.info("Getting nested siblings container element")
        return self.page.locator(self.NESTED_SIBLINGS_CONTAINER)

    def get_nested_sibling(self, key: str):
        """Get a nested sibling element by its key.

        Args:
            key (str): The nested sibling key, such as "1.1.1.1".

        Returns:
            Locator: The locator for the nested sibling element.
        """
        logger.info("Getting nested sibling element: %s", key)
        return self.page.locator(f'[id="sibling-{key}"]')

    def get_table_cell(self, row: int, column: int):
        """Get a table cell by row and column.

        Args:
            row (int): The row number.
            column (int): The column number.

        Returns:
            Locator: The locator for the table cell.
        """
        logger.info("Getting table cell: %s.%s", row, column)
        return self.page.locator(f'[id="{row}.{column}"]')
