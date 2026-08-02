"""Page object for the Floating Menu page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class FloatingMenuPage(BasePage):
    """Page object for the Floating Menu page."""

    # Locators
    PAGE_HEADING = "//h1"
    INSTRUCTION_TEXT = "//p[contains(text(), 'Scroll down')]"
    FLOATING_MENU = "//div[contains(@class, 'fixed') and contains(@class, 'bottom-4')]"
    HOME_BUTTON = "//button[.//*[local-name()='svg']]"

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

    def get_floating_menu(self):
        """Get the floating menu element.

        Returns:
            Locator: The locator for the floating menu element.
        """
        logger.info("Getting floating menu element")
        return self.page.locator(self.FLOATING_MENU)

    def scroll_down(self):
        """Scroll down the page to trigger the floating menu to hide.

        Uses mouse wheel events to ensure the scroll event fires
        with a positive delta (scrollY > lastScrollY).

        Returns:
            None
        """
        logger.info("Scrolling down the page")
        for _ in range(10):
            self.page.mouse.wheel(0, 200)
            self.page.wait_for_timeout(100)
            if self.is_menu_hidden():
                break

    def scroll_up(self):
        """Scroll up to the top of the page to trigger the floating menu to reappear.

        Uses mouse wheel events to ensure the scroll event fires
        with a negative delta (scrollY < lastScrollY).

        Returns:
            None
        """
        logger.info("Scrolling up to the top of the page")
        self.page.mouse.wheel(0, -2000)
        self.page.wait_for_timeout(300)
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(300)

    def is_menu_hidden(self) -> bool:
        """Check if the floating menu is hidden (translate-y-20 applied).

        Returns:
            bool: True if the menu is hidden, False if visible.
        """
        class_name = self.get_floating_menu().get_attribute("class")
        is_hidden = "translate-y-20" in (class_name or "")
        logger.info("Floating menu hidden: %s", is_hidden)
        return is_hidden

    def is_menu_visible(self) -> bool:
        """Check if the floating menu is visible (translate-y-0 applied).

        Returns:
            bool: True if the menu is visible, False if hidden.
        """
        class_name = self.get_floating_menu().get_attribute("class")
        is_visible = "translate-y-0" in (class_name or "")
        logger.info("Floating menu visible: %s", is_visible)
        return is_visible
