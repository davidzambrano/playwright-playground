"""Page object for the Exit Intent page."""

import logging

from .modal_page import ModalPage

logger = logging.getLogger(__name__)


class ExitIntentPage(ModalPage):
    """Page object for the Exit Intent page."""

    # Locators
    PAGE_HEADING = "//h1"
    INSTRUCTION_TEXT = "//p[contains(text(), 'Move your mouse out of the top')]"
    MODAL_TITLE = '//h2[contains(text(), "Wait! Don\'t Go!")]'
    MODAL_BODY = "//*[contains(text(), 'about to leave')]"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

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
        return self.page.locator(self.INSTRUCTION_TEXT)
