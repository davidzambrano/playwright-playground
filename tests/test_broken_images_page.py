"""Tests for the Broken Images page."""

import allure
import pytest
from playwright.sync_api import expect


@allure.epic("Broken Images Interactions")
@pytest.mark.ui
@pytest.mark.regression
class TestBrokenImagesPage:
    """Tests for the Broken Images page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, broken_images_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.broken_images_page = broken_images_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_broken_images_page(self):
        """Fixture to navigate to the Broken Images page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_broken_images_card()

    @allure.story("Broken Images behaviour")
    @allure.title("Page content is correct")
    @allure.severity(allure.severity_level.NORMAL)
    def test_page_content_is_correct(self, navigate_to_broken_images_page):
        """
        Test that the heading and description text are correct and visible.
        """
        expect(self.broken_images_page.get_heading()).to_be_visible()
        expect(self.broken_images_page.get_heading()).to_have_text("Broken Images")
        expect(self.broken_images_page.get_description()).to_be_visible()
        expect(self.broken_images_page.get_description()).to_have_text(
            "This page demonstrates how images that fail to load are displayed."
        )

    @allure.story("Broken Images behaviour")
    @allure.title("All images are present in dom")
    @allure.severity(allure.severity_level.NORMAL)
    def test_all_images_are_present_in_dom(self, navigate_to_broken_images_page):
        """
        Test that all images (working and broken) are present in the DOM.
        """
        expect(self.broken_images_page.get_all_images()).to_have_count(3)

    @allure.story("Broken Images behaviour")
    @allure.title("Working image loads successfully")
    @allure.severity(allure.severity_level.NORMAL)
    def test_working_image_loads_successfully(self, navigate_to_broken_images_page):
        """
        Test that the working image loads successfully.
        """
        img = self.broken_images_page.get_working_image()
        expect(img).to_be_visible()
        # Wait for the image to complete loading
        img.evaluate(
            "el => new Promise(resolve => { if (el.complete) resolve(); "
            "else el.onload = resolve; })"
        )
        # Assert that the image's naturalWidth is not 0, indicating it loaded successfully.
        expect(img).not_to_have_js_property("naturalWidth", 0)

    @allure.story("Broken Images behaviour")
    @allure.title("Broken images fail to load")
    @allure.severity(allure.severity_level.NORMAL)
    def test_broken_images_fail_to_load(self, navigate_to_broken_images_page):
        """
        Test that broken images fail to load (naturalWidth == 0).
        """
        expect(self.broken_images_page.get_all_images()).to_have_count(3)
        for broken_img in self.broken_images_page.get_broken_images():
            expect(broken_img).to_be_visible()
            # Assert that the naturalWidth JavaScript property is 0, indicating a broken image
            expect(broken_img).to_have_js_property("naturalWidth", 0)

    @allure.story("Broken Images behaviour")
    @allure.title("All images have alt text")
    @allure.severity(allure.severity_level.NORMAL)
    def test_all_images_have_alt_text(self, navigate_to_broken_images_page):
        """
        Test that all images have non-empty alt text.
        """
        images = self.broken_images_page.get_all_images()
        for img in images.all():
            # Assert that the alt attribute exists
            expect(img).to_have_attribute("alt")
