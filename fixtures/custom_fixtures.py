import pytest
from playwright.sync_api import Page, BrowserContext
from typing import Generator, Dict
import json
from utils.helpers import TestDataGenerator


@pytest.fixture(scope="function")
def test_user_data() -> Dict:
    """Generate test user data."""
    return {
        "username": TestDataGenerator.random_email(),
        "password": TestDataGenerator.random_string(12) + "1A!",
        "first_name": TestDataGenerator.random_string(8).capitalize(),
        "last_name": TestDataGenerator.random_string(8).capitalize(),
        "phone": TestDataGenerator.random_phone_number()
    }


@pytest.fixture(scope="function")
def api_test_data() -> Dict:
    """Generate API test data."""
    return {
        "user_id": TestDataGenerator.random_string(10),
        "session_token": TestDataGenerator.random_string(32),
        "request_id": TestDataGenerator.random_string(16),
        "timestamp": TestDataGenerator.random_date()
    }


@pytest.fixture(scope="function")
def mock_api_responses(page: Page) -> Generator[Page, None, None]:
    """Mock API responses for testing."""
    # Mock login API
    page.route("**/api/login", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps({
            "success": True,
            "token": "mock_token_12345",
            "user_id": "test_user_123"
        })
    ))

    # Mock user profile API
    page.route("**/api/user/profile", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps({
            "username": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "role": "user"
        })
    ))

    yield page


@pytest.fixture(scope="function")
def slow_network(page: Page) -> Generator[Page, None, None]:
    """Simulate slow network conditions."""
    context = page.context
    # Simulate 3G network conditions
    context.route("**/*", lambda route: route.fulfill(
        status=200,
        headers={"Content-Type": "text/html"},
        body="<html><body>Slow network test</body></html>"
    ))

    yield page


@pytest.fixture(scope="function")
def mobile_viewport(page: Page) -> Generator[Page, None, None]:
    """Set mobile viewport for responsive testing."""
    page.set_viewport_size({"width": 375, "height": 667})
    yield page
    # Reset to desktop viewport
    page.set_viewport_size({"width": 1920, "height": 1080})


@pytest.fixture(scope="function")
def offline_mode(page: Page) -> Generator[Page, None, None]:
    """Simulate offline mode."""
    context = page.context
    context.set_offline(True)
    yield page
    context.set_offline(False)


@pytest.fixture(scope="function")
def browser_storage(context: BrowserContext) -> Generator[BrowserContext, None, None]:
    """Browser storage fixture for testing local/session storage."""
    # Set up initial storage state
    context.add_init_script("""
        localStorage.setItem('test_item', 'test_value');
        sessionStorage.setItem('session_test', 'session_value');
    """)

    yield context
