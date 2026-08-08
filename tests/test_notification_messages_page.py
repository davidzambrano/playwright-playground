"""Tests for the Notification Messages page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestNotificationMessagesPage:
    """Tests for the Notification Messages page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, notification_messages_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.notification_messages_page = notification_messages_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_notification_messages_page(self):
        """Fixture to navigate to the Notification Messages page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_notification_messages_card()

    def test_page_heading_is_visible(self, navigate_to_notification_messages_page):
        """
        Test that the Notification Messages heading is visible.
        """
        expect(self.notification_messages_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_notification_messages_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.notification_messages_page.get_instruction_text()).to_be_visible()

    def test_click_here_link_is_visible(self, navigate_to_notification_messages_page):
        """
        Test that the Click here link is visible.
        """
        expect(self.notification_messages_page.get_click_here_link()).to_be_visible()

    def test_notification_alert_is_visible(self, navigate_to_notification_messages_page):
        """
        Test that the notification alert is visible on page load.
        """
        expect(self.notification_messages_page.get_notification_alert()).to_be_visible()

    def test_notification_message_is_valid(self, navigate_to_notification_messages_page):
        """
        Test that the notification message is one of the possible messages.
        """
        message_text = self.notification_messages_page.get_notification_message().inner_text()
        assert message_text in self.notification_messages_page.POSSIBLE_MESSAGES

    def test_click_here_loads_new_message(self, navigate_to_notification_messages_page):
        """
        Test that clicking the Click here link loads a new message.
        """
        self.notification_messages_page.click_click_here()
        expect(self.notification_messages_page.get_notification_alert()).to_be_visible()

    def test_close_button_hides_notification(self, navigate_to_notification_messages_page):
        """
        Test that clicking the close button hides the notification.
        """
        self.notification_messages_page.click_close_button()
        expect(self.notification_messages_page.get_notification_alert()).not_to_be_visible()
