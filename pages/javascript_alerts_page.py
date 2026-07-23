"""Page object for the JavaScript Alerts page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class JavaScriptAlertsPage(BasePage):
    """
    Page object for the JavaScript Alerts page.
    Provides locators and actions for handling JavaScript alerts, confirms, and prompts.
    """

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'JavaScript Alerts')]"
    INSTRUCTION_TEXT = "//p[contains(text(), 'JavaScript alerts')]"
    JS_ALERT_BUTTON = "//button[contains(text(), 'Click for JS Alert')]"
    JS_CONFIRM_BUTTON = "//button[contains(text(), 'Click for JS Confirm')]"
    JS_PROMPT_BUTTON = "//button[contains(text(), 'Click for JS Prompt')]"
    RESULT_TEXT = "//p[@id='result']"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_instruction_text(self):
        """Get the instruction text element.

        Returns:
            Locator: The locator for the instruction text element.
        """
        logger.info("Getting instruction text element")
        return self.page.locator(self.INSTRUCTION_TEXT)

    def get_js_alert_button(self):
        """Get the JS Alert button element.

        Returns:
            Locator: The locator for the JS Alert button element.
        """
        logger.info("Getting JS Alert button element")
        return self.page.locator(self.JS_ALERT_BUTTON)

    def get_js_confirm_button(self):
        """Get the JS Confirm button element.

        Returns:
            Locator: The locator for the JS Confirm button element.
        """
        logger.info("Getting JS Confirm button element")
        return self.page.locator(self.JS_CONFIRM_BUTTON)

    def get_js_prompt_button(self):
        """Get the JS Prompt button element.

        Returns:
            Locator: The locator for the JS Prompt button element.
        """
        logger.info("Getting JS Prompt button element")
        return self.page.locator(self.JS_PROMPT_BUTTON)

    def get_result_text(self):
        """Get the result text element.

        Returns:
            Locator: The locator for the result text element.
        """
        logger.info("Getting result text element")
        return self.page.locator(self.RESULT_TEXT)

    def click_js_alert_button(self):
        """Click the JS Alert button.

        Returns:
            None
        """
        logger.info("Clicking JS Alert button")
        self.get_js_alert_button().click()

    def click_js_confirm_button(self):
        """Click the JS Confirm button.

        Returns:
            None
        """
        logger.info("Clicking JS Confirm button")
        self.get_js_confirm_button().click()

    def click_js_prompt_button(self):
        """Click the JS Prompt button.

        Returns:
            None
        """
        logger.info("Clicking JS Prompt button")
        self.get_js_prompt_button().click()
