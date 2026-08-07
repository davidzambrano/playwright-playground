"""Page object for the Checkboxes page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class CheckboxesPage(BasePage):
    """
    Page object for the Checkboxes page.
    Provides locators and actions for various checkbox interactions.
    """

    # Locators
    HEADING_LOCATOR = re.compile("Basic Checkboxes")
    CHECKBOX1_LOCATOR = "Unchecked by default"
    CHECKBOX2_LOCATOR = "Checked by default"
    DISABLED_UNCHECKED_LOCATOR = "Disabled and Unchecked"
    DISABLED_CHECKED_LOCATOR = "Disabled and Checked"
    TERMS_CHECKBOX_LOCATOR = "Accept terms and conditions"
    SELECT_ALL_LOCATOR = "Select All"
    ITEM1_LOCATOR = "Apples"
    ITEM2_LOCATOR = "Bananas"
    ITEM3_LOCATOR = "Oranges"

    def get_heading(self):
        """Get the Basic Checkboxes heading element."""
        logger.info("Getting Basic Checkboxes heading element")
        return self.page.get_by_role("heading", name=self.HEADING_LOCATOR)

    def get_checkbox1(self):
        """Get the first basic checkbox (unchecked by default)."""
        logger.info("Getting checkbox1 element")
        return self.page.locator("#checkbox1")

    def get_checkbox2(self):
        """Get the second basic checkbox (checked by default)."""
        logger.info("Getting checkbox2 element")
        return self.page.locator("#checkbox2")

    def get_disabled_unchecked(self):
        """Get the disabled unchecked checkbox."""
        logger.info("Getting disabled unchecked checkbox element")
        return self.page.get_by_role("checkbox", name=self.DISABLED_UNCHECKED_LOCATOR)

    def get_disabled_checked(self):
        """Get the disabled checked checkbox."""
        logger.info("Getting disabled checked checkbox element")
        return self.page.get_by_role("checkbox", name=self.DISABLED_CHECKED_LOCATOR)

    def get_terms_checkbox(self):
        """Get the terms and conditions checkbox."""
        logger.info("Getting terms checkbox element")
        return self.page.get_by_role("checkbox", name=self.TERMS_CHECKBOX_LOCATOR)

    def get_select_all(self):
        """Get the select all checkbox in controlled group."""
        logger.info("Getting select all checkbox element")
        return self.page.get_by_role("checkbox", name=self.SELECT_ALL_LOCATOR)

    def get_item1(self):
        """Get the Apples checkbox in controlled group."""
        logger.info("Getting item1 (Apples) checkbox element")
        return self.page.get_by_role("checkbox", name=self.ITEM1_LOCATOR)

    def get_item2(self):
        """Get the Bananas checkbox in controlled group."""
        logger.info("Getting item2 (Bananas) checkbox element")
        return self.page.get_by_role("checkbox", name=self.ITEM2_LOCATOR)

    def get_item3(self):
        """Get the Oranges checkbox in controlled group."""
        logger.info("Getting item3 (Oranges) checkbox element")
        return self.page.get_by_role("checkbox", name=self.ITEM3_LOCATOR)
