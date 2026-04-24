"""Page object for the Slow Resources page."""

import logging

from playwright.sync_api import Page

from .base_page import BasePage

logger = logging.getLogger(__name__)


class SlowResourcesPage(BasePage):
    """Page object for the Slow Resources page."""

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.header_locator = "//span[.='Slow Resources'] | //h1[.='Slow Resources']"
        self.small_resource_banner_locator = (
            "//div[@role='alert' and contains(., 'Small CSS file (5s) has finished loading.')]"
        )
        self.mid_resource_banner_locator = (
            "//div[@role='alert' and contains(., "
            "'Large Javascript bundle (15s) has finished loading.')]"
        )
        self.large_resource_banner_locator = (
            "//div[@role='alert' and contains(., "
            "'High-resolution image (30s) has finished loading.')]"
        )

    def get_header(self):
        """Get the page header element."""
        logger.debug("Getting page header element with locator: %s", self.header_locator)
        return self.page.locator(self.header_locator)

    def get_small_resource_status_banner(self):
        """Get the small resource status banner."""
        logger.debug("Getting small resource status banner")
        return self.page.locator(self.small_resource_banner_locator)

    def get_mid_resource_status_banner(self):
        """Get the medium resource status banner."""
        logger.debug("Getting medium resource status banner")
        return self.page.locator(self.mid_resource_banner_locator)

    def get_large_resource_status_banner(self):
        """Get the large resource status banner."""
        logger.debug("Getting large resource status banner")
        return self.page.locator(self.large_resource_banner_locator)
