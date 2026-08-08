"""Page object for the iFrame page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class IFramePage(BasePage):
    """Page object for the iFrame page."""

    # Locators
    PAGE_HEADING = re.compile("iFrame")
    IFRAME = "#mce_0_ifr"
    IFRAME_BODY = "body"
    BACK_TO_HOME_LINK = "Back to Home"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_iframe_element(self):
        """Get the iFrame element (not frame locator).

        Returns:
            Locator: The locator for the iFrame element.
        """
        logger.info("Getting iFrame element")
        return self.page.locator(self.IFRAME)

    def get_iframe(self):
        """Get the iFrame as a frame locator for interaction.

        Returns:
            FrameLocator: The frame locator for the iFrame.
        """
        logger.info("Getting iFrame frame locator")
        return self.page.frame_locator(self.IFRAME)

    def get_iframe_body(self):
        """Get the editable body element inside the iFrame.

        Returns:
            Locator: The locator for the iFrame body element.
        """
        logger.info("Getting iFrame body element")
        return self.get_iframe().locator(self.IFRAME_BODY)

    def get_iframe_text(self):
        """Get the text content of the iFrame body.

        Returns:
            str: The text content of the iFrame.
        """
        logger.info("Getting iFrame text content")
        return self.get_iframe_body().inner_text()

    def clear_iframe_content(self):
        """Clear the content of the iFrame using keyboard shortcut.

        Returns:
            None
        """
        logger.info("Clearing iFrame content")
        body = self.get_iframe_body()
        body.click()
        body.press("Control+a")
        body.press("Backspace")

    def type_in_iframe(self, text: str):
        """Type text into the iFrame.

        Args:
            text (str): The text to type into the iFrame.

        Returns:
            None
        """
        logger.info("Typing text into iFrame: %s", text)
        body = self.get_iframe_body()
        body.click()
        body.type(text)

    def get_back_to_home_link(self):
        """Get the Back to Home link element.

        Returns:
            Locator: The locator for the Back to Home link element.
        """
        logger.info("Getting Back to Home link element")
        return self.page.get_by_role("link", name=self.BACK_TO_HOME_LINK)
