"""Page object for the Geolocation page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class GeolocationPage(BasePage):
    """Page object for the Geolocation page."""

    # Locators
    PAGE_HEADING = "//h1"
    WHERE_AM_I_BUTTON = "//button[normalize-space()='Where am I?']"
    LATITUDE_VALUE = "#lat-value"
    LONGITUDE_VALUE = "#long-value"
    ERROR_MESSAGE = "//p[contains(@class, 'text-destructive')]"
    GOOGLE_MAPS_LINK = "//a[contains(text(), 'See it on Google')]"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_where_am_i_button(self):
        """Get the Where am I? button element.

        Returns:
            Locator: The locator for the Where am I? button.
        """
        logger.info("Getting Where am I? button element")
        return self.page.locator(self.WHERE_AM_I_BUTTON)

    def click_where_am_i(self):
        """Click the Where am I? button.

        Returns:
            None
        """
        logger.info("Clicking Where am I? button")
        self.get_where_am_i_button().click()

    def get_latitude_value(self):
        """Get the latitude value element.

        Returns:
            Locator: The locator for the latitude value span.
        """
        logger.info("Getting latitude value element")
        return self.page.locator(self.LATITUDE_VALUE)

    def get_longitude_value(self):
        """Get the longitude value element.

        Returns:
            Locator: The locator for the longitude value span.
        """
        logger.info("Getting longitude value element")
        return self.page.locator(self.LONGITUDE_VALUE)

    def get_error_message(self):
        """Get the error message element.

        Returns:
            Locator: The locator for the error message element.
        """
        logger.info("Getting error message element")
        return self.page.locator(self.ERROR_MESSAGE)

    def get_google_maps_link(self):
        """Get the See it on Google link element.

        Returns:
            Locator: The locator for the Google Maps link.
        """
        logger.info("Getting Google Maps link element")
        return self.page.locator(self.GOOGLE_MAPS_LINK)
