"""Tests for the JavaScript onload event error page."""

import allure
import pytest
from playwright.sync_api import expect


@allure.epic("JavaScript onload event error Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestJavascriptOnloadErrorPage:
    """Tests for the JavaScript onload event error page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, javascript_onload_error_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.javascript_onload_error_page = javascript_onload_error_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_javascript_onload_error_page(self):
        """Fixture to navigate to the JavaScript onload event error page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_javascript_onload_error_card()

    @allure.story("JavaScript onload event error behaviour")
    @allure.title("Page heading is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_heading_is_visible(self, navigate_to_javascript_onload_error_page):
        """
        Test that the page heading is visible.
        """
        expect(self.javascript_onload_error_page.get_page_heading()).to_be_visible()

    @allure.story("JavaScript onload event error behaviour")
    @allure.title("Instruction text is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_instruction_text_is_visible(self, navigate_to_javascript_onload_error_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.javascript_onload_error_page.get_instruction_text()).to_be_visible()

    @allure.story("JavaScript onload event error behaviour")
    @allure.title("Console hint text is visible")
    @allure.severity(allure.severity_level.NORMAL)
    def test_console_hint_text_is_visible(self, navigate_to_javascript_onload_error_page):
        """
        Test that the console hint text is visible.
        """
        expect(self.javascript_onload_error_page.get_console_hint_text()).to_be_visible()

    @allure.story("JavaScript onload event error behaviour")
    @allure.title("Console error is captured")
    @allure.severity(allure.severity_level.NORMAL)
    def test_console_error_is_captured(self):
        """
        Test that a JavaScript console error is captured when the page loads.
        """
        with self.page.expect_console_message(
            lambda msg: "Caught intentional onload error" in msg.text
        ):
            self.home_page.goto_home_page(self.base_url)
            self.home_page.click_javascript_onload_error_card()
        expect(self.javascript_onload_error_page.get_page_heading()).to_be_visible()
