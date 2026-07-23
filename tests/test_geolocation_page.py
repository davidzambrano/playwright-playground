"""Tests for the Geolocation page."""

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestGeolocationPage:
    """Tests for the Geolocation page."""

    # pylint: disable=R0913,R0917
    # Pytest fixture with multiple dependencies is a standard pattern for test setup
    @pytest.fixture(autouse=True)
    def setup_pages(self, geolocation_page, home_page, base_url, context, page):
        """Set up page objects and base URL as class attributes."""
        self.geolocation_page = geolocation_page
        self.home_page = home_page
        self.base_url = base_url
        self.context = context
        self.page = page

    @pytest.fixture
    def navigate_to_geolocation_page(self):
        """Fixture to navigate to the Geolocation page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_geolocation_card()

    def test_page_heading_is_visible(self, navigate_to_geolocation_page):
        """
        Test that the page heading is visible.
        """
        expect(self.geolocation_page.get_page_heading()).to_be_visible()

    def test_where_am_i_button_is_visible(self, navigate_to_geolocation_page):
        """
        Test that the Where am I? button is visible.
        """
        expect(self.geolocation_page.get_where_am_i_button()).to_be_visible()

    def _mock_geolocation(self, latitude=40.4168, longitude=-3.7038):
        """Mock the browser geolocation API with fixed coordinates."""
        self.context.grant_permissions(["geolocation"])
        self.page.evaluate(f"""
            () => {{
                const mockPosition = {{
                    coords: {{
                        latitude: {latitude},
                        longitude: {longitude},
                        accuracy: 10,
                        altitude: null,
                        altitudeAccuracy: null,
                        heading: null,
                        speed: null
                    }},
                    timestamp: Date.now()
                }};
                navigator.geolocation.getCurrentPosition = (success, error, options) => {{
                    success(mockPosition);
                }};
            }}
        """)

    def test_get_location_displays_coordinates(self, navigate_to_geolocation_page):
        """
        Test that clicking Where am I? displays latitude and longitude values.
        """
        self._mock_geolocation()
        self.geolocation_page.click_where_am_i()
        expect(self.geolocation_page.get_latitude_value()).to_have_text("40.4168")
        expect(self.geolocation_page.get_longitude_value()).to_have_text("-3.7038")

    def test_google_maps_link_appears(self, navigate_to_geolocation_page):
        """
        Test that the See it on Google link appears after getting coordinates.
        """
        self._mock_geolocation()
        self.geolocation_page.click_where_am_i()
        expect(self.geolocation_page.get_google_maps_link()).to_be_visible()
        expect(self.geolocation_page.get_google_maps_link()).to_have_attribute(
            "href", "https://www.google.com/maps?q=40.4168,-3.7038"
        )
