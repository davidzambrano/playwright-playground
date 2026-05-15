"""Page object for the Slow Resources page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class SlowResourcesPage(BasePage):
    """Page object for the Slow Resources page."""

    # Locators
    HEADER_LOCATOR = "//span[.='Slow Resources'] | //h1[.='Slow Resources']"
    SMALL_RESOURCE_BANNER_LOCATOR = (
        "//div[@role='alert' and contains(., 'Small CSS file (5s) has finished loading.')]"
    )
    MID_RESOURCE_BANNER_LOCATOR = (
        "//div[@role='alert' and contains(., "
        "'Large Javascript bundle (15s) has finished loading.')]"
    )
    LARGE_RESOURCE_BANNER_LOCATOR = (
        "//div[@role='alert' and contains(., "
        "'High-resolution image (30s) has finished loading.')]"
    )

    def get_header(self):
        """Get the page header element."""
        logger.debug("Getting page header element with locator: %s", self.HEADER_LOCATOR)
        return self.page.locator(self.HEADER_LOCATOR)

    def get_small_resource_status_banner(self):
        """Get the small resource status banner."""
        logger.debug("Getting small resource status banner")
        return self.page.locator(self.SMALL_RESOURCE_BANNER_LOCATOR)

    def get_mid_resource_status_banner(self):
        """Get the medium resource status banner."""
        logger.debug("Getting medium resource status banner")
        return self.page.locator(self.MID_RESOURCE_BANNER_LOCATOR)

    def get_large_resource_status_banner(self):
        """Get the large resource status banner."""
        logger.debug("Getting large resource status banner")
        return self.page.locator(self.LARGE_RESOURCE_BANNER_LOCATOR)
