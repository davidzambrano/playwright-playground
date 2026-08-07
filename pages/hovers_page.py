"""Page object for the Hovers page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class HoversPage(BasePage):
    """
    Page object for the Hovers page.
    Provides locators and actions for hover state interactions.
    """

    # Locators
    PAGE_HEADING = re.compile("Hovers")
    INSTRUCTION_TEXT = re.compile("Hover over the images")
    USER_1_IMAGE = "User 1"
    USER_1_CAPTION = re.compile("User 1")
    USER_2_IMAGE = "User 2"
    USER_2_CAPTION = re.compile("User 2")
    USER_3_IMAGE = "User 3"
    USER_3_CAPTION = re.compile("User 3")

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

    def get_user_1_image(self):
        """Get the User 1 image element.

        Returns:
            Locator: The locator for the User 1 image element.
        """
        logger.info("Getting User 1 image element")
        return self.page.get_by_role("img", name=self.USER_1_IMAGE)

    def get_user_1_caption(self):
        """Get the User 1 caption element.

        Returns:
            Locator: The locator for the User 1 caption element.
        """
        logger.info("Getting User 1 caption element")
        return self.page.get_by_text(self.USER_1_CAPTION)

    def get_user_2_image(self):
        """Get the User 2 image element.

        Returns:
            Locator: The locator for the User 2 image element.
        """
        logger.info("Getting User 2 image element")
        return self.page.get_by_role("img", name=self.USER_2_IMAGE)

    def get_user_2_caption(self):
        """Get the User 2 caption element.

        Returns:
            Locator: The locator for the User 2 caption element.
        """
        logger.info("Getting User 2 caption element")
        return self.page.get_by_text(self.USER_2_CAPTION)

    def get_user_3_image(self):
        """Get the User 3 image element.

        Returns:
            Locator: The locator for the User 3 image element.
        """
        logger.info("Getting User 3 image element")
        return self.page.get_by_role("img", name=self.USER_3_IMAGE)

    def get_user_3_caption(self):
        """Get the User 3 caption element.

        Returns:
            Locator: The locator for the User 3 caption element.
        """
        logger.info("Getting User 3 caption element")
        return self.page.get_by_text(self.USER_3_CAPTION)

    def hover_over_user_1(self):
        """Hover over the User 1 image.

        Returns:
            None
        """
        logger.info("Hovering over User 1 image")
        self.get_user_1_image().hover()

    def hover_over_user_2(self):
        """Hover over the User 2 image.

        Returns:
            None
        """
        logger.info("Hovering over User 2 image")
        self.get_user_2_image().hover()

    def hover_over_user_3(self):
        """Hover over the User 3 image.

        Returns:
            None
        """
        logger.info("Hovering over User 3 image")
        self.get_user_3_image().hover()
