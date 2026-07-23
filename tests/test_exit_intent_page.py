"""Tests for the Exit Intent page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestExitIntentPage:
    """Tests for the Exit Intent page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, exit_intent_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.exit_intent_page = exit_intent_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_exit_intent_page(self):
        """Fixture to navigate to the Exit Intent page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_exit_intent_card()

    def test_page_heading_is_visible(self, navigate_to_exit_intent_page):
        """
        Test that the page heading is visible.
        """
        expect(self.exit_intent_page.get_page_heading()).to_be_visible()

    def test_modal_triggers_on_exit_intent(self, navigate_to_exit_intent_page):
        """
        Test that moving the mouse out of the top of the viewport
        triggers the exit intent modal.
        """
        self.exit_intent_page.trigger_exit_intent()
        self.exit_intent_page.wait_for_modal()
        expect(self.exit_intent_page.get_modal()).to_be_visible()

    def test_modal_has_title(self, navigate_to_exit_intent_page):
        """
        Test that the exit intent modal has the expected title.
        """
        self.exit_intent_page.trigger_exit_intent()
        self.exit_intent_page.wait_for_modal()
        expect(self.exit_intent_page.get_modal_title()).to_be_visible()

    def test_modal_has_body_text(self, navigate_to_exit_intent_page):
        """
        Test that the exit intent modal has body text.
        """
        self.exit_intent_page.trigger_exit_intent()
        self.exit_intent_page.wait_for_modal()
        expect(self.exit_intent_page.get_modal_body()).to_be_visible()

    def test_close_modal(self, navigate_to_exit_intent_page):
        """
        Test that clicking the Close button dismisses the modal.
        """
        self.exit_intent_page.trigger_exit_intent()
        self.exit_intent_page.wait_for_modal()
        self.exit_intent_page.click_close_button()
        expect(self.exit_intent_page.get_modal()).not_to_be_visible()
