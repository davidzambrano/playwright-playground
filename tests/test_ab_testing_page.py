"""Tests for the A/B Testing page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.smoke
class TestABTestingPage:
    """Tests for the A/B Testing page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, ab_testing_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.ab_testing_page = ab_testing_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_ab_testing_page(self):
        """Fixture to navigate to the A/B Testing page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_ab_testing_card()

    def test_signup_displays_confirmation_toast(self, navigate_to_ab_testing_page):
        """
        Test that clicking the sign up button on the active A/B version
        shows a confirmation toast.
        """
        version_a_title = self.ab_testing_page.get_version_a_title()
        version_b_title = self.ab_testing_page.get_version_b_title()

        version_a_title.or_(version_b_title).wait_for()

        if version_a_title.is_visible():
            expect(self.ab_testing_page.get_version_a_description()).to_be_visible()
            self.ab_testing_page.click_version_a_signup()
            expect(self.ab_testing_page.get_toast_title()).to_be_visible()
            expect(self.ab_testing_page.get_toast_version_a_description()).to_be_visible()
        else:
            expect(self.ab_testing_page.get_version_b_description()).to_be_visible()
            self.ab_testing_page.click_version_b_signup()
            expect(self.ab_testing_page.get_toast_title()).to_be_visible()
            expect(self.ab_testing_page.get_toast_version_b_description()).to_be_visible()

    def test_active_version_elements_are_displayed(self, navigate_to_ab_testing_page):
        """
        Test that the heading, description, card content, and sign up button are all visible
        for the active A/B version.
        """
        version_a_title = self.ab_testing_page.get_version_a_title()
        version_b_title = self.ab_testing_page.get_version_b_title()

        version_a_title.or_(version_b_title).wait_for()

        if version_a_title.is_visible():
            expect(version_a_title).to_have_text("Get Our Newsletter")
            expect(self.ab_testing_page.get_version_a_description()).to_be_visible()
            expect(self.ab_testing_page.get_version_a_description()).to_have_text(
                "Stay up to date with our latest news and offers."
            )
            expect(self.ab_testing_page.get_heading()).to_be_visible()
            expect(self.ab_testing_page.get_description()).to_be_visible()
            expect(self.ab_testing_page.get_version_a_signup_button()).to_be_visible()
        else:
            expect(version_b_title).to_have_text("Unlock Exclusive Content!")
            expect(self.ab_testing_page.get_version_b_description()).to_be_visible()
            expect(self.ab_testing_page.get_version_b_description()).to_have_text(
                "Don't miss out on tips, tricks, and special promotions."
            )
            expect(self.ab_testing_page.get_heading()).to_be_visible()
            expect(self.ab_testing_page.get_description()).to_be_visible()
            expect(self.ab_testing_page.get_version_b_signup_button()).to_be_visible()

    def test_page_heading_and_description_text_are_correct(self, navigate_to_ab_testing_page):
        """
        Test that the static page heading and description text are correct
        regardless of A/B version.
        """
        expect(self.ab_testing_page.get_heading()).to_have_text("A/B Test: Call to Action")
        expect(self.ab_testing_page.get_description()).to_be_visible()

    def test_only_one_ab_version_is_displayed_at_a_time(self, navigate_to_ab_testing_page):
        """
        Test that only one A/B version card is visible at a time - never both simultaneously.
        """
        version_a_title = self.ab_testing_page.get_version_a_title()
        version_b_title = self.ab_testing_page.get_version_b_title()

        version_a_title.or_(version_b_title).wait_for()

        if version_a_title.is_visible():
            expect(version_b_title).to_be_hidden()
        else:
            expect(version_a_title).to_be_hidden()

    def test_active_version_card_body_content_is_displayed(self, navigate_to_ab_testing_page):
        """
        Test that the card body paragraph for the active A/B version is visible
        and has correct content.
        """
        version_a_title = self.ab_testing_page.get_version_a_title()
        version_b_title = self.ab_testing_page.get_version_b_title()

        version_a_title.or_(version_b_title).wait_for()

        if version_a_title.is_visible():
            expect(self.ab_testing_page.get_version_a_body()).to_be_visible()
            expect(self.ab_testing_page.get_version_a_body()).to_have_text(
                "Join thousands of subscribers and get the best content directly in your inbox."
            )
        else:
            expect(self.ab_testing_page.get_version_b_body()).to_be_visible()
            expect(self.ab_testing_page.get_version_b_body()).to_have_text(
                (
                    "You're one click away from getting premium content delivered weekly to your "
                    "inbox. It's free!"
                )
            )
