"""Page object for the Horizontal Slider page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class HorizontalSliderPage(BasePage):
    """Page object for the Horizontal Slider page."""

    # Locators
    PAGE_HEADING = "//h1"
    SINGLE_SLIDER = "[role='slider']:not([aria-label])"
    RANGE_SLIDER_MIN = "[role='slider'][aria-label='Minimum']"
    RANGE_SLIDER_MAX = "[role='slider'][aria-label='Maximum']"
    RANGE_VALUE = "#range"
    RANGE_VALUES = "#range-values"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_single_slider(self):
        """Get the single value slider element.

        Returns:
            Locator: The locator for the single value slider.
        """
        logger.info("Getting single value slider element")
        return self.page.locator(self.SINGLE_SLIDER)

    def get_range_slider_min(self):
        """Get the range slider minimum thumb element.

        Returns:
            Locator: The locator for the range slider minimum thumb.
        """
        logger.info("Getting range slider minimum thumb element")
        return self.page.locator(self.RANGE_SLIDER_MIN)

    def get_range_slider_max(self):
        """Get the range slider maximum thumb element.

        Returns:
            Locator: The locator for the range slider maximum thumb.
        """
        logger.info("Getting range slider maximum thumb element")
        return self.page.locator(self.RANGE_SLIDER_MAX)

    def get_range_value(self):
        """Get the single range value display element.

        Returns:
            Locator: The locator for the range value span.
        """
        logger.info("Getting range value element")
        return self.page.locator(self.RANGE_VALUE)

    def get_range_values(self):
        """Get the range values display element.

        Returns:
            Locator: The locator for the range values span.
        """
        logger.info("Getting range values element")
        return self.page.locator(self.RANGE_VALUES)

    def set_slider_value(self, value: int):
        """Set the single value slider to a specific value using keyboard arrows.

        Args:
            value (int): The value to set (0-100).

        Returns:
            None
        """
        logger.info("Setting single slider value to %s", value)
        slider = self.get_single_slider()
        slider.click()
        current = int(slider.get_attribute("aria-valuenow") or "0")
        steps = value - current
        if steps > 0:
            for _ in range(steps):
                slider.press("ArrowRight")
        elif steps < 0:
            for _ in range(abs(steps)):
                slider.press("ArrowLeft")

    def set_range_slider_min(self, value: int):
        """Set the range slider minimum thumb to a specific value using keyboard arrows.

        Args:
            value (int): The minimum value to set (0-100).

        Returns:
            None
        """
        logger.info("Setting range slider minimum to %s", value)
        slider = self.get_range_slider_min()
        slider.click()
        current = int(slider.get_attribute("aria-valuenow") or "0")
        steps = value - current
        if steps > 0:
            for _ in range(steps):
                slider.press("ArrowRight")
        elif steps < 0:
            for _ in range(abs(steps)):
                slider.press("ArrowLeft")

    def set_range_slider_max(self, value: int):
        """Set the range slider maximum thumb to a specific value using keyboard arrows.

        Args:
            value (int): The maximum value to set (0-100).

        Returns:
            None
        """
        logger.info("Setting range slider maximum to %s", value)
        slider = self.get_range_slider_max()
        slider.click()
        current = int(slider.get_attribute("aria-valuenow") or "0")
        steps = value - current
        if steps > 0:
            for _ in range(steps):
                slider.press("ArrowRight")
        elif steps < 0:
            for _ in range(abs(steps)):
                slider.press("ArrowLeft")

    def set_range_value(self, min_val: int, max_val: int):
        """Set the range slider to specific min and max values.

        Args:
            min_val (int): The minimum value (0-100).
            max_val (int): The maximum value (0-100).

        Returns:
            None
        """
        logger.info("Setting range slider to %s - %s", min_val, max_val)
        self.set_range_slider_min(min_val)
        self.set_range_slider_max(max_val)
