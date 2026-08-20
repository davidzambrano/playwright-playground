"""Tests for the Shadow DOM page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestShadowDomPage:
    """Tests for the Shadow DOM page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, shadow_dom_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.shadow_dom_page = shadow_dom_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_shadow_dom_page(self):
        """Fixture to navigate to the Shadow DOM page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_shadow_dom_card()

    def test_page_heading_is_visible(self, navigate_to_shadow_dom_page):
        """
        Test that the Shadow DOM page heading is visible.
        """
        expect(self.shadow_dom_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_shadow_dom_page):
        """
        Test that the instruction text about Shadow DOM is visible.
        """
        expect(self.shadow_dom_page.get_instruction_text()).to_be_visible()

    def test_back_to_home_link_is_visible(self, navigate_to_shadow_dom_page):
        """
        Test that the Back to Home link is visible on the page.
        """
        expect(self.shadow_dom_page.get_back_to_home_link()).to_be_visible()

    def test_first_shadow_host_has_shadow_root(self, navigate_to_shadow_dom_page):
        """
        Verifies that the first host element actually exposes a shadow root,
        confirming the encapsulated DOM boundary exists.
        """
        assert (
            self.shadow_dom_page.first_host_has_shadow_root()
        ), "First host element should expose a shadow root"

    def test_second_shadow_host_has_shadow_root(self, navigate_to_shadow_dom_page):
        """
        Test that the second host element also exposes a shadow root.
        """
        assert (
            self.shadow_dom_page.second_host_has_shadow_root()
        ), "Second host element should expose a shadow root"

    def test_first_shadow_element_is_visible(self, navigate_to_shadow_dom_page):
        """
        Verifies that the text element inside the first shadow root is
        visible when queried from the main document context.
        """
        expect(self.shadow_dom_page.get_first_paragraph()).to_be_visible()

    def test_first_shadow_element_text(self, navigate_to_shadow_dom_page):
        """
        Verifies that the paragraph inside the shadow root has the expected
        text "Let's have some different text!".
        """
        expect(self.shadow_dom_page.get_first_paragraph()).to_have_text(
            "Let's have some different text!"
        )

    def test_list_items_inside_shadow_root(self, navigate_to_shadow_dom_page):
        """
        Test that the list items inside the second shadow root are accessible
        and have the expected contents.
        """
        list_items = self.shadow_dom_page.get_list_items()
        expect(list_items).to_have_count(2)
        expect(list_items).to_have_text(["Let's have some different text!", "In a list!"])
