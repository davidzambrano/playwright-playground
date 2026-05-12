"""Base page object with common functionality for all pages."""

import logging
import os
from typing import Literal

from playwright.sync_api import Page

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common functionality for all page objects."""

    def __init__(self, page: Page):
        """Initialize the BasePage with a page object.

        Args:
            page (Page): The page object.

        Returns:
            None

        """
        self.page = page

    def navigate_to(self, url: str) -> None:
        """Navigate to the specified URL.

        Args:
            url (str): The URL to navigate to.

        Returns:
            None

        """
        logger.info("Navigating to: %s", url)
        self.page.goto(url)

    def wait_for_page_load(
        self, state: Literal["domcontentloaded", "load", "networkidle"] = "load"
    ) -> None:
        """Wait for the page to reach the specified load state.

        Args:
            state (str): The load state to wait for. Options: 'load', 'domcontentloaded',
                         'networkidle'. Defaults to 'load'.

        Returns:
            None

        """
        self.page.wait_for_load_state(state)
        logger.info("Page load completed")

    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot of the current page.

        Args:
            filename (str): The name of the screenshot file.

        Returns:
            None

        """
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = f"{screenshot_dir}/{filename}.png"
        self.page.screenshot(path=screenshot_path, full_page=True)
        logger.info("Screenshot saved: %s", screenshot_path)

    def scroll_to_element(self, locator: str) -> None:
        """Scroll to a specific element.

        Args:
            locator (str): The CSS selector or XPath for the element.

        Returns:
            None

        """
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed()
        logger.info("Scrolled to element: %s", locator)

    def get_page_title(self) -> str:
        """Get the current page title.

        Returns:
            str: The title of the current page.

        """
        title = self.page.title()
        logger.info("Page title: %s", title)
        return title
