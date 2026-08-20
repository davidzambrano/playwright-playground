"""Tests for the Nested Frames page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestNestedFramesPage:
    """Tests for the Nested Frames page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, nested_frames_page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.nested_frames_page = nested_frames_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_nested_frames_page(self):
        """Fixture to navigate to the Nested Frames page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_nested_frames_card()

    def test_page_heading_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the Nested Frames page heading is visible.
        """
        expect(self.nested_frames_page.get_page_heading()).to_be_visible()

    def test_back_to_home_link_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the Back to Home link is visible on the page.
        """
        expect(self.nested_frames_page.get_back_to_home_link()).to_be_visible()

    def test_switch_to_parent_frame(self, navigate_to_nested_frames_page):
        """
        Test Case 28.1: Switch context to the parent frame (frame-parent).

        Verifies that content inside the parent iframe is accessible after
        switching to the parent frame.
        """
        # Access the parent frame and verify its heading is visible
        expect(self.nested_frames_page.get_parent_frame_heading()).to_be_visible()

    def test_switch_to_child_frame(self, navigate_to_nested_frames_page):
        """
        Test Case 28.2: From the parent frame, switch context to the child frame
        (frame-child).

        Verifies that the child frame is nested inside the parent frame and
        its content is accessible.
        """
        # Access the child frame (nested in parent) and verify its heading is visible
        expect(self.nested_frames_page.get_child_frame_heading()).to_be_visible()

    def test_interact_with_child_content(self, navigate_to_nested_frames_page):
        """
        Test Case 28.3: Inside the child frame, assert that the text "Child Frame" is
        visible. Then, switch back to the default content.

        Verifies that the "Child Frame" heading text is visible within the child
        frame, and that the parent page content is accessible after returning to
        the default content (switching back from the nested frame).
        """
        # Assert that the "Child Frame" text is visible inside the child frame
        child_heading = self.nested_frames_page.get_child_frame_heading()
        expect(child_heading).to_be_visible()
        expect(child_heading).to_have_text("Child Frame")

        # Switch back to the default content (parent page level)
        # Verify that a parent page element is accessible after returning to default content
        expect(self.nested_frames_page.get_page_heading()).to_be_visible()

    def test_parent_frame_content_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the parent frame content (heading and instructional text) is
        visible after switching to the parent frame.
        """
        expect(self.nested_frames_page.get_parent_frame_heading()).to_be_visible()
        expect(self.nested_frames_page.get_parent_frame_text_element()).to_be_visible()

    def test_parent_checkbox_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the parent checkbox inside the parent frame is visible.
        """
        expect(self.nested_frames_page.get_parent_checkbox()).to_be_visible()

    def test_child_frame_content_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the child frame content (heading and instructional text) is
        visible after switching through the parent frame to the child frame.
        """
        expect(self.nested_frames_page.get_child_frame_heading()).to_be_visible()
        expect(self.nested_frames_page.get_child_frame_text_element()).to_be_visible()

    def test_child_checkbox_is_visible(self, navigate_to_nested_frames_page):
        """
        Test that the child checkbox inside the child frame is visible.
        """
        expect(self.nested_frames_page.get_child_checkbox()).to_be_visible()

    def test_parent_frame_heading_text(self, navigate_to_nested_frames_page):
        """
        Test that the parent frame heading has the correct text "Parent Frame".
        """
        expect(self.nested_frames_page.get_parent_frame_heading()).to_have_text("Parent Frame")

    def test_child_frame_heading_text(self, navigate_to_nested_frames_page):
        """
        Test that the child frame heading has the correct text "Child Frame".
        """
        expect(self.nested_frames_page.get_child_frame_heading()).to_have_text("Child Frame")
