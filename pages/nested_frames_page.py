"""Page object for the Nested Frames page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class NestedFramesPage(BasePage):
    """Page object for the Nested Frames page.

    The page demonstrates an iframe (``frame-parent``) that itself contains a
    nested iframe (``frame-child``).  Interacting with the child frame content
    requires navigating through both frames.
    """

    # Locators
    PAGE_HEADING = re.compile(r"Nested Frames")
    PARENT_FRAME_LOCATOR = "iframe[name='frame-parent']"
    CHILD_FRAME_LOCATOR = "iframe[name='frame-child']"
    PARENT_FRAME_HEADING = "Parent Frame"
    CHILD_FRAME_HEADING = "Child Frame"
    PARENT_FRAME_TEXT = re.compile(r"This is the content of the parent frame")
    CHILD_FRAME_TEXT = re.compile(r"This is the content of the child frame")
    PARENT_CHECKBOX_LOCATOR = "#parent-checkbox"
    CHILD_CHECKBOX_LOCATOR = "#child-checkbox"
    BACK_TO_HOME_LINK = "Back to Home"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_parent_frame(self):
        """Get the parent frame as a frame locator.

        Returns:
            FrameLocator: The frame locator for the parent iframe.
        """
        logger.info("Getting parent frame locator")
        return self.page.frame_locator(self.PARENT_FRAME_LOCATOR)

    def get_child_frame(self):
        """Get the child frame as a nested frame locator.

        The child frame is nested inside the parent frame, so the locator is
        obtained from the parent frame locator.

        Returns:
            FrameLocator: The frame locator for the child iframe.
        """
        logger.info("Getting child frame locator (nested in parent frame)")
        return self.get_parent_frame().frame_locator(self.CHILD_FRAME_LOCATOR)

    def get_parent_frame_heading(self):
        """Get the Parent Frame heading inside the parent iframe.

        Returns:
            Locator: The locator for the Parent Frame heading element.
        """
        logger.info("Getting parent frame heading element")
        return self.get_parent_frame().get_by_role("heading", name=self.PARENT_FRAME_HEADING)

    def get_child_frame_heading(self):
        """Get the Child Frame heading inside the child iframe.

        Returns:
            Locator: The locator for the Child Frame heading element.
        """
        logger.info("Getting child frame heading element")
        return self.get_child_frame().get_by_role("heading", name=self.CHILD_FRAME_HEADING)

    def get_parent_frame_text_element(self):
        """Get the instructional text element inside the parent frame.

        Returns:
            Locator: The locator for the parent frame text element.
        """
        logger.info("Getting parent frame text element")
        return self.get_parent_frame().get_by_text(self.PARENT_FRAME_TEXT)

    def get_child_frame_text_element(self):
        """Get the instructional text element inside the child frame.

        Returns:
            Locator: The locator for the child frame text element.
        """
        logger.info("Getting child frame text element")
        return self.get_child_frame().get_by_text(self.CHILD_FRAME_TEXT)

    def get_parent_checkbox(self):
        """Get the parent checkbox element inside the parent iframe.

        Returns:
            Locator: The locator for the parent checkbox element.
        """
        logger.info("Getting parent checkbox element")
        return self.get_parent_frame().locator(self.PARENT_CHECKBOX_LOCATOR)

    def get_child_checkbox(self):
        """Get the child checkbox element inside the child iframe.

        Returns:
            Locator: The locator for the child checkbox element.
        """
        logger.info("Getting child checkbox element")
        return self.get_child_frame().locator(self.CHILD_CHECKBOX_LOCATOR)

    def get_back_to_home_link(self):
        """Get the Back to Home link element.

        Returns:
            Locator: The locator for the Back to Home link element.
        """
        logger.info("Getting Back to Home link element")
        return self.page.get_by_role("link", name=self.BACK_TO_HOME_LINK)
