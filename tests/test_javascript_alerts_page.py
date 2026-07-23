"""Tests for the JavaScript Alerts page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestJavaScriptAlertsPage:
    """Tests for the JavaScript Alerts page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, javascript_alerts_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.javascript_alerts_page = javascript_alerts_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_javascript_alerts_page(self):
        """Fixture to navigate to the JavaScript Alerts page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_javascript_alerts_card()

    def test_page_heading_is_visible(self, navigate_to_javascript_alerts_page):
        """
        Test that the JavaScript Alerts heading is visible.
        """
        expect(self.javascript_alerts_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_javascript_alerts_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.javascript_alerts_page.get_instruction_text()).to_be_visible()

    def test_handle_js_alert(self, navigate_to_javascript_alerts_page):
        """
        Test that clicking JS Alert and accepting it shows the success message.
        """
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.javascript_alerts_page.click_js_alert_button()
        expect(self.javascript_alerts_page.get_result_text()).to_have_text(
            "You successfully clicked an alert"
        )

    def test_handle_js_confirm_accept(self, navigate_to_javascript_alerts_page):
        """
        Test that clicking JS Confirm and accepting it shows the Ok message.
        """
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.javascript_alerts_page.click_js_confirm_button()
        expect(self.javascript_alerts_page.get_result_text()).to_have_text("You clicked: Ok")

    def test_handle_js_confirm_dismiss(self, navigate_to_javascript_alerts_page):
        """
        Test that clicking JS Confirm and dismissing it shows the Cancel message.
        """
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.javascript_alerts_page.click_js_confirm_button()
        expect(self.javascript_alerts_page.get_result_text()).to_have_text("You clicked: Cancel")

    def test_handle_js_prompt_accept(self, navigate_to_javascript_alerts_page):
        """
        Test that clicking JS Prompt, entering text, and accepting it shows the entered text.
        """
        test_text = "Hello"
        self.page.on("dialog", lambda dialog: dialog.accept(test_text))
        self.javascript_alerts_page.click_js_prompt_button()
        expect(self.javascript_alerts_page.get_result_text()).to_have_text(
            f"You entered: {test_text}"
        )

    def test_handle_js_prompt_dismiss(self, navigate_to_javascript_alerts_page):
        """
        Test that clicking JS Prompt and dismissing it shows the null message.
        """
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.javascript_alerts_page.click_js_prompt_button()
        expect(self.javascript_alerts_page.get_result_text()).to_have_text("You entered: null")
