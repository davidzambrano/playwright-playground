"""Page object for the Shadow DOM page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class ShadowDomPage(BasePage):
    """Page object for the Shadow DOM page.

    The page renders two host elements (``div``) with open shadow roots via
    ``react-shadow``.  Playwright locators pierce open shadow DOM boundaries
    automatically, so shadowed elements can be located and asserted directly.
    """

    # Locators
    PAGE_HEADING = re.compile(r"Shadow DOM")
    INSTRUCTION_TEXT = re.compile(r"The Shadow DOM is a browser feature")
    HOST_LOCATOR = "div.space-y-4 > div"
    FIRST_PARAGRAPH_TEXT = re.compile(r"Let's have some different text!")
    LIST_ITEM_LOCATOR = "ul li"
    BACK_TO_HOME_LINK = "Back to Home"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_instruction_text(self):
        """Get the instruction text element on the page.

        Returns:
            Locator: The locator for the instruction text element.
        """
        logger.info("Getting instruction text element")
        return self.page.get_by_text(self.INSTRUCTION_TEXT)

    def get_first_shadow_host(self):
        """Get the host element of the first shadow DOM section.

        Returns:
            Locator: The locator for the first shadow host element.
        """
        logger.info("Getting first shadow host element")
        return self.page.locator(self.HOST_LOCATOR).first

    def get_second_shadow_host(self):
        """Get the host element of the second shadow DOM section.

        Returns:
            Locator: The locator for the second shadow host element.
        """
        logger.info("Getting second shadow host element")
        return self.page.locator(self.HOST_LOCATOR).nth(1)

    def first_host_has_shadow_root(self) -> bool:
        """Check whether the first host element has a shadow root attached.

        This verifies the shadow root exists directly on the host element.

        Returns:
            bool: True if the first host has a shadow root, False otherwise.
        """
        logger.info("Checking first host for shadow root")
        return self.get_first_shadow_host().evaluate("el => el.shadowRoot !== null")

    def second_host_has_shadow_root(self) -> bool:
        """Check whether the second host element has a shadow root attached.

        Returns:
            bool: True if the second host has a shadow root, False otherwise.
        """
        logger.info("Checking second host for shadow root")
        return self.get_second_shadow_host().evaluate("el => el.shadowRoot !== null")

    def get_first_paragraph(self):
        """Get the paragraph element inside the first shadow root.

        Playwright locators pierce the shadow boundary automatically, so the
        text-only ``p`` element inside the shadow root is directly addressable.

        Returns:
            Locator: The locator for the first shadow paragraph element.
        """
        logger.info("Getting first shadow paragraph element")
        return self.page.locator("p", has_text=self.FIRST_PARAGRAPH_TEXT)

    def get_list_items(self):
        """Get the list items inside the second shadow root.

        Returns:
            Locator: The locator matching the shadow ul/ol list items.
        """
        logger.info("Getting list items from second shadow root")
        return self.page.locator(self.LIST_ITEM_LOCATOR)

    def get_back_to_home_link(self):
        """Get the Back to Home link element.

        Returns:
            Locator: The locator for the Back to Home link element.
        """
        logger.info("Getting Back to Home link element")
        return self.page.get_by_role("link", name=self.BACK_TO_HOME_LINK)
