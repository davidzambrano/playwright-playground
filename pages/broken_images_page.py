"""Page object for the Broken Images page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class BrokenImagesPage(BasePage):
    """
    Page object for the Broken Images page.
    Provides locators and actions for working and broken images.
    """

    # Locators
    HEADING_LOCATOR = "Broken Images"
    DESCRIPTION_LOCATOR = re.compile("images that fail to load")
    IMAGE_LOCATOR = "img"
    WORKING_IMAGE_LOCATOR = "A working image"
    BROKEN_IMAGE_LOCATORS = ["A broken image", "Another broken image"]

    def get_heading(self):
        """Get the page heading element."""
        logger.info("Getting Broken Images page heading element")
        return self.page.get_by_role("heading", name=self.HEADING_LOCATOR)

    def get_description(self):
        """Get the page description element."""
        logger.info("Getting Broken Images page description element")
        return self.page.get_by_text(self.DESCRIPTION_LOCATOR)

    def get_all_images(self):
        """Get all image elements on the page."""
        logger.info("Getting all image elements on Broken Images page")
        return self.page.locator(self.IMAGE_LOCATOR)

    def get_working_image(self):
        """Get the working image element (should load successfully)."""
        logger.info("Getting working image element")
        return self.page.get_by_role("img", name=self.WORKING_IMAGE_LOCATOR)

    def get_broken_images(self):
        """Get all broken image elements (should fail to load)."""
        logger.info("Getting broken image elements")
        return [self.page.get_by_role("img", name=alt) for alt in self.BROKEN_IMAGE_LOCATORS]
