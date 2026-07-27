"""Page object for the Home page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """Page object for the Home page."""

    # pylint: disable=R0904
    # HomePage is a navigation hub with multiple cards, each requiring getter and clicker methods
    # Following the project's Page Object Model pattern with clear separation of concerns

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
    CHECKBOXES_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[text()='Checkboxes']]"
    )
    DROPDOWN_CARD_LOCATOR = (
        "//div[contains(@class, 'rounded-lg') and .//span[contains(text(), 'Dropdown')]]"
    )
    CONTEXT_MENU_CARD_LOCATOR = "//a[contains(@href, 'context-menu')]"
    DYNAMIC_CONTROLS_CARD_LOCATOR = "//a[contains(@href, 'dynamic-controls')]"
    HOVERS_CARD_LOCATOR = "//a[contains(@href, 'hovers')]"
    JAVASCRIPT_ALERTS_CARD_LOCATOR = "//a[contains(@href, 'javascript-alerts')]"
    DISAPPEARING_ELEMENTS_CARD_LOCATOR = "//a[contains(@href, 'disappearing-elements')]"
    KEY_PRESSES_CARD_LOCATOR = "//a[contains(@href, 'key-presses')]"
    DRAG_AND_DROP_CARD_LOCATOR = "//a[contains(@href, 'drag-and-drop')]"
    DYNAMIC_CONTENT_CARD_LOCATOR = "//a[contains(@href, 'dynamic-content')]"
    DYNAMIC_LOADING_CARD_LOCATOR = "//a[contains(@href, 'dynamic-loading')]"
    ENTRY_AD_CARD_LOCATOR = "//a[contains(@href, 'entry-ad')]"
    EXIT_INTENT_CARD_LOCATOR = "//a[contains(@href, 'exit-intent')]"
    FILE_DOWNLOAD_CARD_LOCATOR = "//a[@href='/link/file-download']"
    FILE_UPLOAD_CARD_LOCATOR = "//a[@href='/link/file-upload']"
    FLOATING_MENU_CARD_LOCATOR = "//a[@href='/link/floating-menu']"
    GEOLOCATION_CARD_LOCATOR = "//a[@href='/link/geolocation']"
    HORIZONTAL_SLIDER_CARD_LOCATOR = "//a[@href='/link/horizontal-slider']"
    IFRAME_CARD_LOCATOR = "//a[@href='/link/iframe']"

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

    def click_stale_element_card(self):
        """Click the Stale Element card.

        Returns:
            None
        """
        self.get_stale_element_card().click()
        logger.info("Clicked Stale Element card")

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

    def get_checkboxes_card(self):
        """Get the Checkboxes card element.

        Returns:
            Locator: The locator for the Checkboxes card element.
        """
        logger.info("Getting Checkboxes card element")
        return self.page.locator(self.CHECKBOXES_CARD_LOCATOR)

    def get_dropdown_card(self):
        """Get the Dropdown card element.

        Returns:
            Locator: The locator for the Dropdown card element.
        """
        logger.info("Getting Dropdown card element")
        return self.page.locator(self.DROPDOWN_CARD_LOCATOR)

    def get_context_menu_card(self):
        """Get the Context Menu card element.

        Returns:
            Locator: The locator for the Context Menu card element.
        """
        logger.info("Getting Context Menu card element")
        return self.page.locator(self.CONTEXT_MENU_CARD_LOCATOR)

    def get_dynamic_controls_card(self):
        """Get the Dynamic Controls card element.

        Returns:
            Locator: The locator for the Dynamic Controls card element.
        """
        logger.info("Getting Dynamic Controls card element")
        return self.page.locator(self.DYNAMIC_CONTROLS_CARD_LOCATOR)

    def get_hovers_card(self):
        """Get the Hovers card element.

        Returns:
            Locator: The locator for the Hovers card element.
        """
        logger.info("Getting Hovers card element")
        return self.page.locator(self.HOVERS_CARD_LOCATOR)

    def get_javascript_alerts_card(self):
        """Get the JavaScript Alerts card element.

        Returns:
            Locator: The locator for the JavaScript Alerts card element.
        """
        logger.info("Getting JavaScript Alerts card element")
        return self.page.locator(self.JAVASCRIPT_ALERTS_CARD_LOCATOR)

    def get_disappearing_elements_card(self):
        """Get the Disappearing Elements card element.

        Returns:
            Locator: The locator for the Disappearing Elements card element.
        """
        logger.info("Getting Disappearing Elements card element")
        return self.page.locator(self.DISAPPEARING_ELEMENTS_CARD_LOCATOR)

    def get_key_presses_card(self):
        """Get the Key Presses card element.

        Returns:
            Locator: The locator for the Key Presses card element.
        """
        logger.info("Getting Key Presses card element")
        return self.page.locator(self.KEY_PRESSES_CARD_LOCATOR)

    def get_drag_and_drop_card(self):
        """Get the Drag and Drop card element.

        Returns:
            Locator: The locator for the Drag and Drop card element.
        """
        logger.info("Getting Drag and Drop card element")
        return self.page.locator(self.DRAG_AND_DROP_CARD_LOCATOR)

    def get_dynamic_loading_card(self):
        """Get the Dynamic Loading card element.

        Returns:
            Locator: The locator for the Dynamic Loading card element.
        """
        logger.info("Getting Dynamic Loading card element")
        return self.page.locator(self.DYNAMIC_LOADING_CARD_LOCATOR)

    def get_dynamic_content_card(self):
        """Get the Dynamic Content card element.

        Returns:
            Locator: The locator for the Dynamic Content card element.
        """
        logger.info("Getting Dynamic Content card element")
        return self.page.locator(self.DYNAMIC_CONTENT_CARD_LOCATOR)

    def get_entry_ad_card(self):
        """Get the Entry Ad card element.

        Returns:
            Locator: The locator for the Entry Ad card element.
        """
        logger.info("Getting Entry Ad card element")
        return self.page.locator(self.ENTRY_AD_CARD_LOCATOR)

    def click_entry_ad_card(self):
        """Click the Entry Ad card.

        Returns:
            None
        """
        self.get_entry_ad_card().click()
        logger.info("Clicked Entry Ad card")

    def get_exit_intent_card(self):
        """Get the Exit Intent card element.

        Returns:
            Locator: The locator for the Exit Intent card element.
        """
        logger.info("Getting Exit Intent card element")
        return self.page.locator(self.EXIT_INTENT_CARD_LOCATOR)

    def click_exit_intent_card(self):
        """Click the Exit Intent card.

        Returns:
            None
        """
        self.get_exit_intent_card().click()
        logger.info("Clicked Exit Intent card")

    def get_file_download_card(self):
        """Get the File Download card element.

        Returns:
            Locator: The locator for the File Download card element.
        """
        logger.info("Getting File Download card element")
        return self.page.locator(self.FILE_DOWNLOAD_CARD_LOCATOR)

    def click_file_download_card(self):
        """Click the File Download card.

        Returns:
            None
        """
        self.get_file_download_card().click()
        logger.info("Clicked File Download card")

    def get_file_upload_card(self):
        """Get the File Upload card element.

        Returns:
            Locator: The locator for the File Upload card element.
        """
        logger.info("Getting File Upload card element")
        return self.page.locator(self.FILE_UPLOAD_CARD_LOCATOR)

    def click_file_upload_card(self):
        """Click the File Upload card.

        Returns:
            None
        """
        self.get_file_upload_card().click()
        logger.info("Clicked File Upload card")

    def get_floating_menu_card(self):
        """Get the Floating Menu card element.

        Returns:
            Locator: The locator for the Floating Menu card element.
        """
        logger.info("Getting Floating Menu card element")
        return self.page.locator(self.FLOATING_MENU_CARD_LOCATOR)

    def click_floating_menu_card(self):
        """Click the Floating Menu card.

        Returns:
            None
        """
        self.get_floating_menu_card().click()
        logger.info("Clicked Floating Menu card")

    def get_geolocation_card(self):
        """Get the Geolocation card element.

        Returns:
            Locator: The locator for the Geolocation card element.
        """
        logger.info("Getting Geolocation card element")
        return self.page.locator(self.GEOLOCATION_CARD_LOCATOR)

    def click_geolocation_card(self):
        """Click the Geolocation card.

        Returns:
            None
        """
        self.get_geolocation_card().click()
        logger.info("Clicked Geolocation card")

    def get_horizontal_slider_card(self):
        """Get the Horizontal Slider card element.

        Returns:
            Locator: The locator for the Horizontal Slider card element.
        """
        logger.info("Getting Horizontal Slider card element")
        return self.page.locator(self.HORIZONTAL_SLIDER_CARD_LOCATOR)

    def click_horizontal_slider_card(self):
        """Click the Horizontal Slider card.

        Returns:
            None
        """
        self.get_horizontal_slider_card().click()
        logger.info("Clicked Horizontal Slider card")

    def get_iframe_card(self):
        """Get the iFrame card element.

        Returns:
            Locator: The locator for the iFrame card element.
        """
        logger.info("Getting iFrame card element")
        return self.page.locator(self.IFRAME_CARD_LOCATOR)

    def click_iframe_card(self):
        """Click the iFrame card.

        Returns:
            None
        """
        self.get_iframe_card().click()
        logger.info("Clicked iFrame card")

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

    def click_checkboxes_card(self):
        """Click the Checkboxes card.

        Returns:
            None

        """
        self.get_checkboxes_card().click()
        logger.info("Clicked Checkboxes card")

    def click_dropdown_card(self):
        """Click the Dropdown card.

        Returns:
            None

        """
        self.get_dropdown_card().click()
        logger.info("Clicked Dropdown card")

    def click_context_menu_card(self):
        """Click the Context Menu card.

        Returns:
            None

        """
        self.get_context_menu_card().click()
        logger.info("Clicked Context Menu card")

    def click_dynamic_controls_card(self):
        """Click the Dynamic Controls card.

        Returns:
            None

        """
        self.get_dynamic_controls_card().click()
        logger.info("Clicked Dynamic Controls card")

    def click_hovers_card(self):
        """Click the Hovers card.

        Returns:
            None

        """
        self.get_hovers_card().click()
        logger.info("Clicked Hovers card")

    def click_javascript_alerts_card(self):
        """Click the JavaScript Alerts card.

        Returns:
            None

        """
        self.get_javascript_alerts_card().click()
        logger.info("Clicked JavaScript Alerts card")

    def click_disappearing_elements_card(self):
        """Click the Disappearing Elements card.

        Returns:
            None

        """
        self.get_disappearing_elements_card().click()
        logger.info("Clicked Disappearing Elements card")

    def click_key_presses_card(self):
        """Click the Key Presses card.

        Returns:
            None

        """
        self.get_key_presses_card().click()
        logger.info("Clicked Key Presses card")

    def click_drag_and_drop_card(self):
        """Click the Drag and Drop card.

        Returns:
            None

        """
        self.get_drag_and_drop_card().click()
        logger.info("Clicked Drag and Drop card")

    def click_dynamic_loading_card(self):
        """Click the Dynamic Loading card.

        Returns:
            None

        """
        self.get_dynamic_loading_card().click()
        logger.info("Clicked Dynamic Loading card")

    def click_dynamic_content_card(self):
        """Click the Dynamic Content card.

        Returns:
            None

        """
        self.get_dynamic_content_card().click()
        logger.info("Clicked Dynamic Content card")
