"""Tests for the Infinite Scroll page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestInfiniteScrollPage:
    """Tests for the Infinite Scroll page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, infinite_scroll_page, page, home_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.infinite_scroll_page = infinite_scroll_page
        self.home_page = home_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_infinite_scroll_page(self):
        """Fixture to navigate to the Infinite Scroll page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_infinite_scroll_card()

    def test_page_heading_is_visible(self, navigate_to_infinite_scroll_page):
        """
        Test that the Infinite Scroll page heading is visible.
        """
        expect(self.infinite_scroll_page.get_page_heading()).to_be_visible()

    def test_initial_paragraphs_present(self, navigate_to_infinite_scroll_page):
        """
        Test that initial paragraphs are present on page load.
        """
        # Wait for paragraphs to load (React client-side rendering)
        expect(self.infinite_scroll_page.get_paragraphs().first).to_be_visible(timeout=15000)
        initial_count = self.infinite_scroll_page.get_paragraph_count()
        assert initial_count > 0, "Should have at least one paragraph on page load"

    def test_scroll_loads_more_content(self, navigate_to_infinite_scroll_page):
        """
        Test that scrolling to bottom loads more content (Test Case 23.1).
        """
        # Get initial paragraph count
        initial_count = self.infinite_scroll_page.get_paragraph_count()

        # Scroll to bottom
        self.infinite_scroll_page.scroll_to_bottom()

        # Wait for new paragraphs to load
        self.infinite_scroll_page.wait_for_new_paragraphs(initial_count)

        # Verify more paragraphs were loaded
        new_count = self.infinite_scroll_page.get_paragraph_count()
        assert (
            new_count > initial_count
        ), f"Expected more paragraphs after scrolling. Initial: {initial_count}, After: {new_count}"

    def test_paragraphs_have_content(self, navigate_to_infinite_scroll_page):
        """
        Test that loaded paragraphs contain text content.
        """
        paragraphs = self.infinite_scroll_page.get_paragraphs()
        # Check first few paragraphs have content
        for i in range(min(3, paragraphs.count())):
            text = paragraphs.nth(i).inner_text()
            assert len(text.strip()) > 0, f"Paragraph {i} should have content"

    def test_multiple_scrolls_load_incremental_content(self, navigate_to_infinite_scroll_page):
        """
        Test that multiple consecutive scrolls continue to load more content.
        """
        # Get initial count
        initial_count = self.infinite_scroll_page.get_paragraph_count()

        # Scroll and wait three times
        for scroll_num in range(3):
            self.infinite_scroll_page.scroll_to_bottom()
            self.infinite_scroll_page.wait_for_new_paragraphs(initial_count + (scroll_num * 10))

        # Verify content increased significantly
        final_count = self.infinite_scroll_page.get_paragraph_count()
        assert final_count > initial_count + 20, (
            f"Expected at least 20+ new paragraphs after 3 scrolls. "
            f"Initial: {initial_count}, Final: {final_count}"
        )

    def test_new_content_is_different(self, navigate_to_infinite_scroll_page):
        """
        Test that newly loaded content is different from initial content.
        """
        # Get initial paragraph text
        initial_text = self.infinite_scroll_page.get_paragraphs().first.inner_text()

        # Scroll to load more
        initial_count = self.infinite_scroll_page.get_paragraph_count()
        self.infinite_scroll_page.scroll_to_bottom()
        self.infinite_scroll_page.wait_for_new_paragraphs(initial_count)

        # Get the last paragraph (newly loaded)
        new_count = self.infinite_scroll_page.get_paragraph_count()
        last_paragraph = self.infinite_scroll_page.get_paragraphs().nth(new_count - 1)
        new_text = last_paragraph.inner_text()

        # Verify content is different
        assert initial_text != new_text, "New content should be different from initial content"
