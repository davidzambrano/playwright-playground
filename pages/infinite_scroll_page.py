"""Page object for the Infinite Scroll page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class InfiniteScrollPage(BasePage):
    """Page object for the Infinite Scroll page."""

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Infinite Scroll')]"
    PARAGRAPH_LOCATOR = "//div[contains(@class, 'space-y-8')]//p"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_paragraphs(self):
        """Get all paragraph elements on the page.

        Returns:
            Locator: The locator for all paragraph elements.
        """
        logger.info("Getting all paragraph elements")
        return self.page.locator(self.PARAGRAPH_LOCATOR)

    def get_paragraph_count(self):
        """Get the current count of paragraphs on the page.

        Returns:
            int: The number of paragraphs currently loaded.
        """
        logger.info("Getting paragraph count")
        return self.get_paragraphs().count()

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page to trigger loading more content.

        Returns:
            None
        """
        logger.info("Scrolling to bottom of page")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        logger.info("Scrolled to bottom of page")

    def wait_for_new_paragraphs(self, initial_count: int, timeout: int = 10000):
        """Wait for new paragraphs to load after scrolling.

        Args:
            initial_count (int): The initial paragraph count before scrolling.
            timeout (int): Maximum time to wait in milliseconds. Defaults to 10000.

        Returns:
            None
        """
        logger.info("Waiting for new paragraphs to load (initial count: %s)", initial_count)
        self.page.wait_for_function(
            "() => document.querySelectorAll('div.space-y-8 p').length > " + str(initial_count),
            timeout=timeout,
        )
        logger.info("New paragraphs loaded")
