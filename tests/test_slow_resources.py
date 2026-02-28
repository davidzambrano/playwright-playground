"""Tests for the Slow Resources page."""
import pytest
from playwright.sync_api import expect

class TestSlowResourcesPage:
    """Tests for status banner visibility on the Slow Resources page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, home_page, page, slow_resources_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.home_page = home_page
        self.slow_resources_page = slow_resources_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_slow_resources(self):
        """Fixture to navigate to the Slow Resources page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_slow_resources_card()
    
    def test_small_resource_banner_visible(self, navigate_to_slow_resources):
        """Verify that the small resource status banner appears after loading."""
        header = self.slow_resources_page.get_header()
        expect(header).to_be_visible(timeout=10000), "Page header wasn't visible - may not be on the correct page"
        
        small_banner = self.slow_resources_page.get_small_resource_status_banner()
        expect(small_banner).to_be_visible(timeout=7000)
        expect(small_banner).to_contain_text("Small CSS file (5s) has finished loading.")
    
    def test_mid_resource_banner_visible(self, navigate_to_slow_resources):
        """Verify that the mid resource status banner appears after loading."""
        header = self.slow_resources_page.get_header()
        expect(header).to_be_visible(timeout=10000), "Page header wasn't visible - may not be on the correct page"
        
        mid_banner = self.slow_resources_page.get_mid_resource_status_banner()
        expect(mid_banner).to_be_visible(timeout=17000)
        expect(mid_banner).to_contain_text("Large Javascript bundle (15s) has finished loading.")
    
    def test_large_resource_banner_visible(self, navigate_to_slow_resources):
        """Verify that the large resource status banner appears after loading."""
        header = self.slow_resources_page.get_header()
        expect(header).to_be_visible(timeout=10000), "Page header wasn't visible - may not be on the correct page"
        
        large_banner = self.slow_resources_page.get_large_resource_status_banner()
        expect(large_banner).to_be_visible(timeout=32000)
        expect(large_banner).to_contain_text("High-resolution image (30s) has finished loading.")

