"""Page object for the Dynamic Loading page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class DynamicLoadingPage(BasePage):
    """
    Page object for the Dynamic Loading page.
    Provides locators and actions for Example 1 (hidden element) and Example 2 (rendered element).
    """

    # Locators
    PAGE_HEADING = re.compile("Dynamic Loading")

    # Example 1: Hidden element
    EXAMPLE1_START_BUTTON = re.compile("Example 1")
    EXAMPLE1_HIDDEN_DIV = "#start"
    EXAMPLE1_CONTENT = "#start p"

    # Example 2: Rendered element
    EXAMPLE2_START_BUTTON = re.compile("Example 2")
    EXAMPLE2_LOADING_SKELETON = "#finish .space-y-2"
    EXAMPLE2_FINISH_CARD = "#finish p"
    EXAMPLE2_LOADING_BUTTON_TEXT = "Loading..."

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    # Example 1: Hidden element methods

    def get_example1_start_button(self):
        """Get the Example 1 Start button.

        Returns:
            Locator: The locator for the Example 1 Start button.
        """
        logger.info("Getting Example 1 Start button")
        return self.page.get_by_role("button", name="Start").first

    def get_example1_hidden_div(self):
        """Get the Example 1 hidden div element.

        Returns:
            Locator: The locator for the Example 1 hidden div.
        """
        logger.info("Getting Example 1 hidden div")
        return self.page.locator(self.EXAMPLE1_HIDDEN_DIV)

    def get_example1_content(self):
        """Get the Example 1 content paragraph.

        Returns:
            Locator: The locator for the Example 1 content paragraph.
        """
        logger.info("Getting Example 1 content")
        return self.page.locator(self.EXAMPLE1_CONTENT)

    def click_example1_start_button(self):
        """Click the Example 1 Start button to reveal the hidden element.

        Returns:
            None
        """
        logger.info("Clicking Example 1 Start button")
        self.get_example1_start_button().click()

    def is_example1_content_visible(self) -> bool:
        """Check if the Example 1 hidden content is visible.

        Returns:
            bool: True if the content is visible, False otherwise.
        """
        logger.info("Checking if Example 1 content is visible")
        return self.get_example1_content().is_visible()

    def wait_for_example1_content_visible(self):
        """Wait for the Example 1 content to become visible.

        Returns:
            None
        """
        logger.info("Waiting for Example 1 content to become visible")
        self.get_example1_content().wait_for(state="visible")

    # Example 2: Rendered element methods

    def get_example2_start_button(self):
        """Get the Example 2 Start button.

        Returns:
            Locator: The locator for the Example 2 Start button.
        """
        logger.info("Getting Example 2 Start button")
        return self.page.get_by_role("button", name="Start").nth(1)

    def click_example2_start_button(self):
        """Click the Example 2 Start button to trigger the async load.

        Returns:
            None
        """
        logger.info("Clicking Example 2 Start button")
        self.get_example2_start_button().click()

    def get_example2_finish_content(self):
        """Get the Example 2 finish content paragraph.

        Returns:
            Locator: The locator for the Example 2 finish content paragraph.
        """
        logger.info("Getting Example 2 finish content")
        return self.page.locator(self.EXAMPLE2_FINISH_CARD)

    def is_example2_finish_content_visible(self) -> bool:
        """Check if the Example 2 finish content is visible.

        Returns:
            bool: True if the content is visible, False otherwise.
        """
        logger.info("Checking if Example 2 finish content is visible")
        return self.get_example2_finish_content().is_visible()

    def wait_for_example2_content_loaded(self):
        """Wait for the Example 2 content to load after the async request.

        Waits for the "Hello World!" text to appear in the finish div.

        Returns:
            None
        """
        logger.info("Waiting for Example 2 content to load")
        self.get_example2_finish_content().wait_for(state="visible", timeout=10000)

    def get_example2_content_text(self) -> str:
        """Get the text content from Example 2's finish element.

        Returns:
            str: The text content of the finish element.
        """
        logger.info("Getting Example 2 content text")
        return self.get_example2_finish_content().text_content()
