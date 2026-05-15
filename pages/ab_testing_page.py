"""Page object for the A/B Testing page, supporting both Version A and Version B."""

import logging

from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ABTestingPage(BasePage):
    """
    Page object for the A/B Testing page.
    Provides locators and actions for both Version A (Control) and Version B (Variant).
    """

    # Headings
    HEADING_LOCATOR = "h2:text('A/B Test: Call to Action')"
    DESCRIPTION_LOCATOR = "p.text-muted-foreground"

    # Version A elements
    VERSION_A_TITLE_LOCATOR = "div.text-2xl:text('Get Our Newsletter')"
    VERSION_A_DESCRIPTION_LOCATOR = (
        "div.text-2xl:text('Get Our Newsletter') + div.text-sm.text-muted-foreground"
    )
    VERSION_A_SIGNUP_BUTTON_LOCATOR = "button.w-full:has-text('Sign Up')"
    VERSION_A_CARD_CONTAINER = "div.max-w-md:has(div.text-2xl:has-text('Get Our Newsletter'))"

    # Version B elements
    VERSION_B_TITLE_LOCATOR = "div.text-green-500:text('Unlock Exclusive Content!')"
    VERSION_B_DESCRIPTION_LOCATOR = (
        "div.text-green-500:text('Unlock Exclusive Content!') + div.text-sm.text-muted-foreground"
    )
    VERSION_B_SIGNUP_BUTTON_LOCATOR = "button.bg-green-600:has-text('Sign Up Now')"
    VERSION_B_CARD_CONTAINER = (
        "div.max-w-md:has(div.text-green-500:has-text('Unlock Exclusive Content!'))"
    )

    # Toast elements
    TOAST_TITLE_LOCATOR = ".text-sm.font-semibold:has-text('Thank you for signing up!')"
    TOAST_VERSION_A_DESCRIPTION_LOCATOR = (
        ".text-sm.opacity-90:has-text('(Conversion from Version A)')"
    )
    TOAST_VERSION_B_DESCRIPTION_LOCATOR = (
        ".text-sm.opacity-90:has-text('(Conversion from Version B)')"
    )

    def get_heading(self):
        """Get the heading element for the A/B Testing page.

        Returns:
            Locator: The locator for the heading element.
        """
        logger.info("Getting heading element for A/B Testing page")
        return self.page.locator(self.HEADING_LOCATOR)

    def get_description(self):
        """Get the unique static description element for the A/B Testing page."""
        logger.info("Getting page description element for A/B Testing page")
        return self.page.locator(
            self.DESCRIPTION_LOCATOR, has_text="This page demonstrates an A/B test."
        )

    def get_version_a_title(self):
        """Get the Version A title element.

        Returns:
            Locator: The locator for the Version A title element.
        """
        logger.info("Getting Version A title element")
        return self.page.locator(self.VERSION_A_TITLE_LOCATOR)

    def get_version_a_description(self):
        """Get the Version A description element.

        Returns:
            Locator: The locator for the Version A description element.
        """
        logger.info("Getting Version A description element")
        return self.page.locator(self.VERSION_A_DESCRIPTION_LOCATOR)

    def get_version_a_signup_button(self):
        """Get the Version A sign up button element.

        Returns:
            Locator: The locator for the Version A sign up button.
        """
        logger.info("Getting Version A sign up button element")
        return self.page.locator(self.VERSION_A_SIGNUP_BUTTON_LOCATOR)

    def get_version_a_body(self):
        """Get the Version A card body paragraph element.

        Returns:
            Locator: The locator for the Version A card body paragraph.
        """
        logger.info("Getting Version A card body paragraph element")
        return self.page.locator(f"{self.VERSION_A_CARD_CONTAINER} div.p-6.pt-0 > p")

    def click_version_a_signup(self):
        """Click the Version A sign up button.

        Returns:
            None
        """
        logger.info("Clicking Version A sign up button")
        self.page.locator(self.VERSION_A_SIGNUP_BUTTON_LOCATOR).click()

    def get_version_b_title(self):
        """Get the Version B title element.

        Returns:
            Locator: The locator for the Version B title element.
        """
        logger.info("Getting Version B title element")
        return self.page.locator(self.VERSION_B_TITLE_LOCATOR)

    def get_version_b_description(self):
        """Get the Version B description element.

        Returns:
            Locator: The locator for the Version B description element.
        """
        logger.info("Getting Version B description element")
        return self.page.locator(self.VERSION_B_DESCRIPTION_LOCATOR)

    def get_version_b_signup_button(self):
        """Get the Version B sign up button element.

        Returns:
            Locator: The locator for the Version B sign up button.
        """
        logger.info("Getting Version B sign up button element")
        return self.page.locator(self.VERSION_B_SIGNUP_BUTTON_LOCATOR)

    def get_version_b_body(self):
        """Get the Version B card body paragraph element.

        Returns:
            Locator: The locator for the Version B card body paragraph.
        """
        logger.info("Getting Version B card body paragraph element")
        return self.page.locator(f"{self.VERSION_B_CARD_CONTAINER} div.p-6.pt-0 > p")

    def click_version_b_signup(self):
        """Click the Version B sign up button.

        Returns:
            None
        """
        logger.info("Clicking Version B sign up button")
        self.page.locator(self.VERSION_B_SIGNUP_BUTTON_LOCATOR).click()

    def get_toast_title(self):
        """Get the toast title element shown after signing up.

        Returns:
            Locator: The locator for the toast title element.
        """
        logger.info("Getting toast title element")
        return self.page.locator(self.TOAST_TITLE_LOCATOR)

    def get_toast_version_a_description(self):
        """Get the toast description element for Version A sign up.

        Returns:
            Locator: The locator for the Version A toast description element.
        """
        logger.info("Getting toast description element for Version A")
        return self.page.locator(self.TOAST_VERSION_A_DESCRIPTION_LOCATOR)

    def get_toast_version_b_description(self):
        """Get the toast description element for Version B sign up.

        Returns:
            Locator: The locator for the Version B toast description element.
        """
        logger.info("Getting toast description element for Version B")
        return self.page.locator(self.TOAST_VERSION_B_DESCRIPTION_LOCATOR)
