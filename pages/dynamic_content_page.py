"""Page object for the Dynamic Content page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DynamicContentPage(BasePage):
    """
    Page object for the Dynamic Content page.
    Provides locators and actions for handling dynamically changing content.
    """

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Dynamic Content')]"
    INSTRUCTION_TEXT = "//p[contains(text(), 'content that can change')]"
    RANDOMIZE_BUTTON = "//button[contains(text(), 'Randomize Content')]"
    CONTENT_ITEMS = "//div[contains(@class, 'animate-in')]//p"
    CONTENT_IMAGES = "//div[contains(@class, 'animate-in')]//img"

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

    def get_randomize_button(self):
        """Get the Randomize Content button element.

        Returns:
            Locator: The locator for the Randomize Content button element.
        """
        logger.info("Getting Randomize Content button element")
        return self.page.locator(self.RANDOMIZE_BUTTON)

    def get_content_items(self):
        """Get all content item text elements.

        Returns:
            Locator: The locator for all content item text elements.
        """
        logger.info("Getting content item text elements")
        return self.page.locator(self.CONTENT_ITEMS)

    def get_content_images(self):
        """Get all content image elements.

        Returns:
            Locator: The locator for all content image elements.
        """
        logger.info("Getting content image elements")
        return self.page.locator(self.CONTENT_IMAGES)

    def click_randomize_button(self):
        """Click the Randomize Content button.

        Returns:
            None
        """
        logger.info("Clicking Randomize Content button")
        self.get_randomize_button().click()

    def get_content_texts(self):
        """Get the text content of all content items.

        Returns:
            list: A list of text content from all content items.
        """
        logger.info("Getting text content of all items")
        self.get_content_items().first.wait_for(state="visible")
        items = self.get_content_items().all()
        return [item.text_content() for item in items]

    def get_image_sources(self):
        """Get the src attributes of all content images.

        Returns:
            list: A list of src attributes from all content images.
        """
        logger.info("Getting src attributes of all images")
        self.get_content_images().first.wait_for(state="visible")
        images = self.get_content_images().all()
        return [image.get_attribute("src") for image in images]
