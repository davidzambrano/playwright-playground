"""Page object for the Secure File Download page."""

import logging
import re

from .base_page import BasePage

logger = logging.getLogger(__name__)


class SecureFileDownloadPage(BasePage):
    """Page object for the Secure File Download page."""

    # Locators
    PAGE_HEADING = re.compile("Secure File Download")
    LOGIN_CARD_TITLE = "Secure Login"
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "Login"
    SECURE_AREA_HEADING = "Secure Area"
    WELCOME_TEXT = re.compile("secure file download area")
    LOGOUT_BUTTON = "Log out"
    FILE_NAME = "sample.txt"
    DOWNLOAD_BUTTON = "Download"

    def get_page_heading(self):
        """Get the page heading element."""
        logger.info("Getting page heading element")
        return self.page.get_by_role("heading", name=self.PAGE_HEADING)

    def get_login_card_title(self):
        """Get the login card title element."""
        logger.info("Getting login card title element")
        return self.page.get_by_text(self.LOGIN_CARD_TITLE)

    def get_username_input(self):
        """Get the username input element."""
        logger.info("Getting username input element")
        return self.page.locator(self.USERNAME_INPUT)

    def get_password_input(self):
        """Get the password input element."""
        logger.info("Getting password input element")
        return self.page.locator(self.PASSWORD_INPUT)

    def get_login_button(self):
        """Get the Login button element."""
        logger.info("Getting Login button element")
        return self.page.get_by_role("button", name=self.LOGIN_BUTTON)

    def get_secure_area_heading(self):
        """Get the Secure Area heading element."""
        logger.info("Getting Secure Area heading element")
        return self.page.get_by_text(self.SECURE_AREA_HEADING)

    def get_welcome_text(self):
        """Get the welcome text element."""
        logger.info("Getting welcome text element")
        return self.page.get_by_text(self.WELCOME_TEXT)

    def get_logout_button(self):
        """Get the Log out button element."""
        logger.info("Getting Log out button element")
        return self.page.get_by_role("button", name=self.LOGOUT_BUTTON)

    def get_file_card(self, file_name):
        """Get a file card element by file name."""
        logger.info("Getting file card element: %s", file_name)
        return self.page.get_by_text(file_name, exact=True)

    def get_download_button(self, file_name):
        """Get the Download button for a specific file."""
        logger.info("Getting Download button for file: %s", file_name)
        return (
            self.get_file_card(file_name)
            .locator("..")
            .get_by_role("button", name=self.DOWNLOAD_BUTTON)
        )

    def enter_username(self, username):
        """Enter the username."""
        logger.info("Entering username: %s", username)
        self.get_username_input().fill(username)

    def enter_password(self, password):
        """Enter the password."""
        logger.info("Entering password")
        self.get_password_input().fill(password)

    def click_login(self):
        """Click the Login button."""
        logger.info("Clicking Login button")
        self.get_login_button().click()

    def login(self, username, password):
        """Perform login."""
        logger.info("Performing login")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_logout(self):
        """Click the Log out button."""
        logger.info("Clicking Log out button")
        self.get_logout_button().click()

    def click_download(self, file_name):
        """Click the Download button for a file."""
        logger.info("Clicking Download button for file: %s", file_name)
        self.get_download_button(file_name).click()
