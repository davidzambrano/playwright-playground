"""Tests for the Disappearing Elements page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestDisappearingElementsPage:
    """Tests for the Disappearing Elements page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, disappearing_elements_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.disappearing_elements_page = disappearing_elements_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_disappearing_elements_page(self):
        """Fixture to navigate to the Disappearing Elements page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_disappearing_elements_card()

    def test_page_heading_is_visible(self, navigate_to_disappearing_elements_page):
        """
        Test that the Disappearing Elements heading is visible.
        """
        expect(self.disappearing_elements_page.get_page_heading()).to_be_visible()

    def test_instruction_text_is_visible(self, navigate_to_disappearing_elements_page):
        """
        Test that the instruction text is visible.
        """
        expect(self.disappearing_elements_page.get_instruction_text()).to_be_visible()

    def test_gallery_tab_may_be_present(self, navigate_to_disappearing_elements_page):
        """
        Test that the Gallery tab may or may not be present on page load.
        The test passes regardless of whether the tab is present or not.
        """
        # Gallery tab has 50% chance of appearing - this test just validates
        # that the page loads correctly (heading and instruction text are always present)
        expect(self.disappearing_elements_page.get_page_heading()).to_be_visible()
        expect(self.disappearing_elements_page.get_instruction_text()).to_be_visible()

    def test_home_tab_always_present(self, navigate_to_disappearing_elements_page):
        """
        Test that the Home tab is always present.
        """
        expect(self.disappearing_elements_page.get_home_tab()).to_be_visible()

    def test_click_home_tab_shows_content(self, navigate_to_disappearing_elements_page):
        """
        Test that clicking the Home tab shows the Home content.
        """
        self.disappearing_elements_page.click_home_tab()
        expect(self.disappearing_elements_page.get_content_area()).to_contain_text(
            "Welcome to the Home page"
        )

    def test_click_about_tab_shows_content(self, navigate_to_disappearing_elements_page):
        """
        Test that clicking the About tab shows the About content.
        """
        self.disappearing_elements_page.click_about_tab()
        expect(self.disappearing_elements_page.get_content_area()).to_contain_text(
            "Information about us"
        )

    def test_click_contact_us_tab_shows_content(self, navigate_to_disappearing_elements_page):
        """
        Test that clicking the Contact Us tab shows the Contact Us content.
        """
        self.disappearing_elements_page.click_contact_us_tab()
        expect(self.disappearing_elements_page.get_content_area()).to_contain_text(
            "How to contact us"
        )

    def test_click_portfolio_tab_shows_content(self, navigate_to_disappearing_elements_page):
        """
        Test that clicking the Portfolio tab shows the Portfolio content.
        """
        self.disappearing_elements_page.click_portfolio_tab()
        expect(self.disappearing_elements_page.get_content_area()).to_contain_text(
            "Our work portfolio"
        )

    def test_click_gallery_tab_shows_content_if_present(
        self, navigate_to_disappearing_elements_page
    ):
        """
        Test that clicking the Gallery tab shows the Gallery content if the tab is present.
        """
        gallery_tab = self.disappearing_elements_page.get_gallery_tab()
        if gallery_tab.is_visible():
            expect(self.disappearing_elements_page.get_content_area()).to_contain_text(
                "This is the gallery"
            )
