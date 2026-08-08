"""Page object for the Exit Intent page."""

import logging
import re

from .modal_page import ModalPage

logger = logging.getLogger(__name__)


class ExitIntentPage(ModalPage):
    """Page object for the Exit Intent page."""

    # Locators
    PAGE_HEADING = re.compile("Exit Intent")
    INSTRUCTION_TEXT = re.compile("Move your mouse out of the top")
    MODAL_TITLE = re.compile("Wait! Don't Go!")
    MODAL_BODY = re.compile("about to leave")

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def trigger_exit_intent(self):
        """Trigger the exit intent modal by dispatching a mouseout event
        at the top edge of the viewport (clientY <= 0).

        The client component must be hydrated (its event listener attached)
        before the synthetic event is dispatched, otherwise the event is lost.
        We wait for the instruction text to be visible as a hydration signal.

        Returns:
            None
        """
        logger.info("Waiting for client component hydration")
        self.get_instruction_text().wait_for(state="visible", timeout=10000)
        logger.info("Triggering exit intent by dispatching mouseout event")
        self.page.evaluate(
            "() => {"
            "  const event = new MouseEvent('mouseout', {"
            "    bubbles: true, clientX: 0, clientY: 0"
            "  });"
            "  document.dispatchEvent(event);"
            "}"
        )

    def get_instruction_text(self):
        """Get the instruction text element.

        Returns:
            Locator: The locator for the instruction text element.
        """
        logger.info("Getting instruction text element")
        return self.page.get_by_text(self.INSTRUCTION_TEXT)

    def get_modal_title(self):
        """Get the modal title element.

        Returns:
            Locator: The locator for the modal title element.
        """
        logger.info("Getting modal title element")
        return self.get_modal().get_by_text(self.MODAL_TITLE)

    def get_modal_body(self):
        """Get the modal body element.

        Returns:
            Locator: The locator for the modal body element.
        """
        logger.info("Getting modal body element")
        return self.get_modal().get_by_text(self.MODAL_BODY)
