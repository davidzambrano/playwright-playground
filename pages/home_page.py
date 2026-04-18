"""Page object for the Home page."""

import logging

from playwright.sync_api import Page

from .base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """Page object for the Home page."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title_locator = "//h1"
        self.slow_resources_card_locator = (
            "//div[contains(@class, 'rounded-lg') and .//span[text()='Slow Resources']]"
        )
        self.stale_element_card_locator = (
            "//div[contains(@class, 'rounded-lg') and .//span[text()='Stale Element']]"
        )
        self.add_remove_element_card_locator = "//div[contains(@class, 'rounded-lg') and .//span[text()='Add/Remove Elements']]"
        self.basic_auth_card_locator = (
            "//div[contains(@class, 'rounded-lg') and .//span[text()='Basic Auth']]"
        )

    def goto_home_page(self, base_url: str):
        """Navigate to the home page.

        Args:
            base_url (str): The base URL to navigate to.

        Returns:
            None

        """
        self.navigate_to(base_url)
        self.wait_for_page_load()
        logger.info("Navigated to home page")

    def get_page_title(self):
        """Get the page title element.

        Returns:
            Locator: The locator for the page title element.

        """
        return self.page.locator(self.page_title_locator)

    def get_slow_resources_card(self):
        """Get the Slow Resources card element.

        Returns:
            Locator: The locator for the Slow Resources card element.

        """
        return self.page.locator(self.slow_resources_card_locator)

    def get_add_remove_element_card(self):
        """Get the Add/Remove Elements card element.

        Returns:
            Locator: The locator for the Add/Remove Elements card element.

        """
        return self.page.locator(self.add_remove_element_card_locator)

    def get_basic_auth_card(self):
        """Get the Basic Auth card element.

        Returns:
            Locator: The locator for the Basic Auth card element.

        """
        return self.page.locator(self.basic_auth_card_locator)

    def get_stale_element_card(self):
        """Get the Stale Element card element.

        Returns:
            Locator: The locator for the Stale Element card element.

        """
        return self.page.locator(self.stale_element_card_locator)

    def click_slow_resources_card(self):
        """Click the Slow Resources card.

        Returns:
            None

        """
        card = self.get_slow_resources_card()
        card.click()
        logger.info("Clicked Slow Resources card")

    def click_add_remove_element_card(self):
        """Click the Add/Remove Elements card.

        Returns:
            None

        """
        card = self.get_add_remove_element_card()
        card.click()
        logger.info("Clicked Add/Remove Elements card")

    def click_basic_auth_card(self):
        """Click the Basic Auth card.

        Returns:
            None

        """
        card = self.get_basic_auth_card()
        card.click()
        logger.info("Clicked Basic Auth card")
