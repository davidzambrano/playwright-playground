"""Page object for the Home page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """Page object for the Home page."""

    # Locators
    PAGE_TITLE_LOCATOR = "//h1"
    SLOW_RESOURCES_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Slow Resources']]"
    )
    STALE_ELEMENT_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Stale Element']]"
    )
    ADD_REMOVE_ELEMENT_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Add/Remove Elements']]"
    )
    BASIC_AUTH_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Basic Auth']]"
    )
    AB_TESTING_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='A/B Testing']]"
    )
    BROKEN_IMAGES_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Broken Images']]"
    )
    CHALLENGING_DOM_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Challenging DOM']]"
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

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_TITLE_LOCATOR)

    def get_slow_resources_card(self):
        """Get the Slow Resources card element.

        Returns:
            Locator: The locator for the Slow Resources card element.
        """
        logger.info("Getting Slow Resources card element")
        return self.page.locator(self.SLOW_RESOURCES_CARD_LOCATOR)

    def get_add_remove_element_card(self):
        """Get the Add/Remove Elements card element.

        Returns:
            Locator: The locator for the Add/Remove Elements card element.
        """
        logger.info("Getting Add/Remove Elements card element")
        return self.page.locator(self.ADD_REMOVE_ELEMENT_CARD_LOCATOR)

    def get_basic_auth_card(self):
        """Get the Basic Auth card element.

        Returns:
            Locator: The locator for the Basic Auth card element.
        """
        logger.info("Getting Basic Auth card element")
        return self.page.locator(self.BASIC_AUTH_CARD_LOCATOR)

    def get_stale_element_card(self):
        """Get the Stale Element card element.

        Returns:
            Locator: The locator for the Stale Element card element.
        """
        logger.info("Getting Stale Element card element")
        return self.page.locator(self.STALE_ELEMENT_CARD_LOCATOR)

    def get_ab_testing_card(self):
        """Get the A/B Testing card element.

        Returns:
            Locator: The locator for the A/B Testing card element.
        """
        logger.info("Getting A/B Testing card element")
        return self.page.locator(self.AB_TESTING_CARD_LOCATOR)

    def get_challenging_dom_card(self):
        """Get the Challenging DOM card element.

        Returns:
            Locator: The locator for the Challenging DOM card element.
        """
        logger.info("Getting Challenging DOM card element")
        return self.page.locator(self.CHALLENGING_DOM_CARD_LOCATOR)

    def get_broken_images_card(self):
        """Get the Broken Images card element.

        Returns:
            Locator: The locator for the Broken Images card element.
        """
        logger.info("Getting Broken Images card element")
        return self.page.locator(self.BROKEN_IMAGES_CARD_LOCATOR)

    def click_slow_resources_card(self):
        """Click the Slow Resources card.

        Returns:
            None

        """
        self.get_slow_resources_card().click()
        logger.info("Clicked Slow Resources card")

    def click_add_remove_element_card(self):
        """Click the Add/Remove Elements card.

        Returns:
            None
        """
        self.get_add_remove_element_card().click()
        logger.info("Clicked Add/Remove Elements card")

    def click_basic_auth_card(self):
        """Click the Basic Auth card.

        Returns:
            None
        """
        self.get_basic_auth_card().click()
        logger.info("Clicked Basic Auth card")

    def click_ab_testing_card(self):
        """Click the A/B Testing card.

        Returns:
            None
        """
        self.get_ab_testing_card().click()
        logger.info("Clicked A/B Testing card")

    def click_challenging_dom_card(self):
        """Click the Challenging DOM card.

        Returns:
            None
        """
        self.get_challenging_dom_card().click()
        logger.info("Clicked Challenging DOM card")

    def click_broken_images_card(self):
        """Click the Broken Images card.

        Returns:
            None
        """
        self.get_broken_images_card().click()
        logger.info("Clicked Broken Images card")
