"""Page object for the Inputs page."""

import logging

from .base_page import BasePage

logger = logging.getLogger(__name__)


class InputsPage(BasePage):
    """Page object for the Inputs page."""

    # Locators
    PAGE_HEADING = "//h1[contains(text(), 'Inputs')]"
    NAME_INPUT = "//input[@placeholder='John Doe']"
    EMAIL_INPUT = "//input[@type='email' and @placeholder='john.doe@example.com']"
    PASSWORD_INPUT = "//input[@type='password' and @placeholder='********']"
    NUMBER_INPUT = "//input[@type='number' and @placeholder='Enter a positive number']"
    WEBSITE_INPUT = "//input[@type='url' and @placeholder='https://example.com']"
    SUBMIT_BUTTON = "//button[normalize-space()='Submit']"
    TOAST_TITLE = "//li[@role='status']//div[contains(text(), 'Form Submitted!')]"
    EMAIL_ERROR_MESSAGE = "//p[contains(@class, 'text-destructive')]"

    def get_page_heading(self):
        """Get the page heading element.

        Returns:
            Locator: The locator for the page heading element.
        """
        logger.info("Getting page heading element")
        return self.page.locator(self.PAGE_HEADING)

    def get_name_input(self):
        """Get the Name input field.

        Returns:
            Locator: The locator for the Name input field.
        """
        logger.info("Getting Name input field")
        return self.page.locator(self.NAME_INPUT)

    def get_email_input(self):
        """Get the Email input field.

        Returns:
            Locator: The locator for the Email input field.
        """
        logger.info("Getting Email input field")
        return self.page.locator(self.EMAIL_INPUT)

    def get_password_input(self):
        """Get the Password input field.

        Returns:
            Locator: The locator for the Password input field.
        """
        logger.info("Getting Password input field")
        return self.page.locator(self.PASSWORD_INPUT)

    def get_number_input(self):
        """Get the Number input field.

        Returns:
            Locator: The locator for the Number input field.
        """
        logger.info("Getting Number input field")
        return self.page.locator(self.NUMBER_INPUT)

    def get_website_input(self):
        """Get the Website input field.

        Returns:
            Locator: The locator for the Website input field.
        """
        logger.info("Getting Website input field")
        return self.page.locator(self.WEBSITE_INPUT)

    def get_submit_button(self):
        """Get the Submit button.

        Returns:
            Locator: The locator for the Submit button.
        """
        logger.info("Getting Submit button")
        return self.page.locator(self.SUBMIT_BUTTON)

    def get_toast_title(self):
        """Get the toast notification title.

        Returns:
            Locator: The locator for the toast title.
        """
        logger.info("Getting toast title")
        return self.page.locator(self.TOAST_TITLE)

    def get_email_error_message(self):
        """Get the email validation error message.

        Returns:
            Locator: The locator for the email error message.
        """
        logger.info("Getting email error message")
        return self.page.locator(self.EMAIL_ERROR_MESSAGE)

    def fill_name(self, name: str):
        """Fill the Name input field.

        Args:
            name (str): The name to enter.

        Returns:
            None
        """
        logger.info("Filling Name input: %s", name)
        self.get_name_input().fill(name)

    def fill_email(self, email: str):
        """Fill the Email input field.

        Args:
            email (str): The email to enter.

        Returns:
            None
        """
        logger.info("Filling Email input: %s", email)
        self.get_email_input().fill(email)

    def fill_password(self, password: str):
        """Fill the Password input field.

        Args:
            password (str): The password to enter.

        Returns:
            None
        """
        logger.info("Filling Password input")
        self.get_password_input().fill(password)

    def fill_number(self, number: str):
        """Fill the Number input field.

        Args:
            number (str): The number to enter.

        Returns:
            None
        """
        logger.info("Filling Number input: %s", number)
        self.get_number_input().fill(number)

    def fill_website(self, website: str):
        """Fill the Website input field.

        Args:
            website (str): The website URL to enter.

        Returns:
            None
        """
        logger.info("Filling Website input: %s", website)
        self.get_website_input().fill(website)

    def click_submit(self):
        """Click the Submit button.

        Returns:
            None
        """
        logger.info("Clicking Submit button")
        self.get_submit_button().click()

    # pylint: disable=too-many-arguments,too-many-positional-arguments
    def submit_form(self, name: str, email: str, password: str, number: str, website: str):
        """Fill and submit the form with all fields.

        Args:
            name (str): The name to enter.
            email (str): The email to enter.
            password (str): The password to enter.
            number (str): The number to enter.
            website (str): The website URL to enter.

        Returns:
            None
        """
        logger.info("Submitting form with all fields")
        self.fill_name(name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_number(number)
        self.fill_website(website)
        self.click_submit()
