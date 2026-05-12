"""Network and browser environment fixtures for testing edge cases."""

import json
import time
from typing import Generator

import pytest
from playwright.sync_api import BrowserContext, Page


@pytest.fixture(scope="function")
def mock_api_responses(page: Page) -> Generator[Page, None, None]:
    """Mock API responses for testing."""
    page.route(
        "**/api/login",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(
                {
                    "success": True,
                    "token": "mock_token_12345",
                    "user_id": "test_user_123",
                }
            ),
        ),
    )

    page.route(
        "**/api/user/profile",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(
                {
                    "username": "testuser@example.com",
                    "first_name": "Test",
                    "last_name": "User",
                    "role": "user",
                }
            ),
        ),
    )

    yield page


@pytest.fixture(scope="function")
def slow_network(page: Page) -> Generator[Page, None, None]:
    """Simulate slow network by adding latency to every request.

    Adds a 2-second delay to each network request using route interception.
    Works across all browsers (chromium, firefox, webkit).
    """

    def delay_route(route):
        time.sleep(2)
        route.continue_()

    page.route("**/*", delay_route)
    yield page
    page.unroute("**/*", delay_route)


@pytest.fixture(scope="function")
def slow_network_cdp(page: Page) -> Generator[Page, None, None]:
    """Simulate 3G network conditions via CDP (Chromium only).

    Emulates network throttling at the protocol level for realistic latency,
    download/upload speed limits. Will fail on Firefox/WebKit.
    """
    cdp = page.context.new_cdp_session(page)
    cdp.send(
        "Network.emulateNetworkConditions",
        {
            "offline": False,
            "downloadThroughput": 1.5 * 1024 * 1024 / 8,  # 1.5 Mbps
            "uploadThroughput": 750 * 1024 / 8,  # 750 Kbps
            "latency": 100,  # 100ms RTT
        },
    )
    yield page
    cdp.send(
        "Network.emulateNetworkConditions",
        {
            "offline": False,
            "downloadThroughput": -1,
            "uploadThroughput": -1,
            "latency": 0,
        },
    )
    cdp.detach()


@pytest.fixture(scope="function")
def mobile_viewport(page: Page) -> Generator[Page, None, None]:
    """Set mobile viewport for responsive testing."""
    page.set_viewport_size({"width": 375, "height": 667})
    yield page
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
    context.add_init_script("""
        localStorage.setItem('test_item', 'test_value');
        sessionStorage.setItem('session_test', 'session_value');
    """)

    yield context
