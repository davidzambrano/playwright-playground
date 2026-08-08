"""Page object for the Disappearing Elements page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DisappearingElementsPage(BasePage):
    """
    Page object for the Disappearing Elements page.
    Provides locators and actions for handling elements that randomly appear/disappear.
    """

    # Locators
    PAGE_HEADING = re.compile("Disappearing Elements")
    INSTRUCTION_TEXT = re.compile("elements on a page change")
    CONTENT_AREA = "main"

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

    def get_tab_button(self, tab_name):
        """Get a specific tab button element.

        Args:
            tab_name (str): The name of the tab (Home, About, Contact Us, Portfolio, Gallery).

        Returns:
            Locator: The locator for the tab button element.
        """
        logger.info("Getting %s tab button element", tab_name)
        return self.page.get_by_role("button", name=tab_name, exact=True)

    def get_home_tab(self):
        """Get the Home tab button element.

        Returns:
            Locator: The locator for the Home tab button element.
        """
        logger.info("Getting Home tab button element")
        return self.get_tab_button("Home")

    def get_about_tab(self):
        """Get the About tab button element.

        Returns:
            Locator: The locator for the About tab button element.
        """
        logger.info("Getting About tab button element")
        return self.get_tab_button("About")

    def get_contact_us_tab(self):
        """Get the Contact Us tab button element.

        Returns:
            Locator: The locator for the Contact Us tab button element.
        """
        logger.info("Getting Contact Us tab button element")
        return self.get_tab_button("Contact Us")

    def get_portfolio_tab(self):
        """Get the Portfolio tab button element.

        Returns:
            Locator: The locator for the Portfolio tab button element.
        """
        logger.info("Getting Portfolio tab button element")
        return self.get_tab_button("Portfolio")

    def get_gallery_tab(self):
        """Get the Gallery tab button element.

        Returns:
            Locator: The locator for the Gallery tab button element.
        """
        logger.info("Getting Gallery tab button element")
        return self.get_tab_button("Gallery")

    def get_content_area(self):
        """Get the content area element.

        Returns:
            Locator: The locator for the content area element.
        """
        logger.info("Getting content area element")
        return self.page.locator(self.CONTENT_AREA)

    def click_tab(self, tab_name):
        """Click a specific tab button.

        Args:
            tab_name (str): The name of the tab to click.

        Returns:
            None
        """
        logger.info("Clicking %s tab", tab_name)
        self.get_tab_button(tab_name).click()

    def click_home_tab(self):
        """Click the Home tab.

        Returns:
            None
        """
        logger.info("Clicking Home tab")
        self.get_home_tab().click()

    def click_about_tab(self):
        """Click the About tab.

        Returns:
            None
        """
        logger.info("Clicking About tab")
        self.get_about_tab().click()

    def click_contact_us_tab(self):
        """Click the Contact Us tab.

        Returns:
            None
        """
        logger.info("Clicking Contact Us tab")
        self.get_contact_us_tab().click()

    def click_portfolio_tab(self):
        """Click the Portfolio tab.

        Returns:
            None
        """
        logger.info("Clicking Portfolio tab")
        self.get_portfolio_tab().click()

    def click_gallery_tab(self):
        """Click the Gallery tab.

        Returns:
            None
        """
        logger.info("Clicking Gallery tab")
        self.get_gallery_tab().click()
