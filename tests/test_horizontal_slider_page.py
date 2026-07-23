"""Tests for the Horizontal Slider page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestHorizontalSliderPage:
    """Tests for the Horizontal Slider page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, horizontal_slider_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.horizontal_slider_page = horizontal_slider_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_horizontal_slider_page(self):
        """Fixture to navigate to the Horizontal Slider page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_horizontal_slider_card()

    def test_page_heading_is_visible(self, navigate_to_horizontal_slider_page):
        """
        Test that the page heading is visible.
        """
        expect(self.horizontal_slider_page.get_page_heading()).to_be_visible()

    def test_single_slider_is_visible(self, navigate_to_horizontal_slider_page):
        """
        Test that the single value slider is visible.
        """
        expect(self.horizontal_slider_page.get_single_slider()).to_be_visible()

    def test_range_slider_is_visible(self, navigate_to_horizontal_slider_page):
        """
        Test that the range slider is visible.
        """
        expect(self.horizontal_slider_page.get_range_slider_min()).to_be_visible()
        expect(self.horizontal_slider_page.get_range_slider_max()).to_be_visible()

    def test_move_slider_updates_value(self, navigate_to_horizontal_slider_page):
        """
        Test that moving the single slider to a new position updates the displayed value.
        """
        self.horizontal_slider_page.set_slider_value(75)
        expect(self.horizontal_slider_page.get_range_value()).to_have_text("75")

    def test_range_slider_default_values(self, navigate_to_horizontal_slider_page):
        """
        Test that the range slider displays the default values.
        """
        expect(self.horizontal_slider_page.get_range_values()).to_have_text("25 - 75")

    def test_set_range_slider_min(self, navigate_to_horizontal_slider_page):
        """
        Test that setting the range slider minimum thumb updates the displayed values.
        """
        self.horizontal_slider_page.set_range_slider_min(10)
        expect(self.horizontal_slider_page.get_range_values()).to_have_text("10 - 75")

    def test_set_range_slider_max(self, navigate_to_horizontal_slider_page):
        """
        Test that setting the range slider maximum thumb updates the displayed values.
        """
        self.horizontal_slider_page.set_range_slider_max(90)
        expect(self.horizontal_slider_page.get_range_values()).to_have_text("25 - 90")
