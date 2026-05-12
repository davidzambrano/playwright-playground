"""Test data fixtures for generating synthetic test data."""

from typing import Dict

import pytest

from utils.helpers import TestDataGenerator


@pytest.fixture(scope="function")
def test_user_data() -> Dict:
    """Generate test user data."""
    return {
        "username": TestDataGenerator.random_email(),
        "password": TestDataGenerator.random_string(12) + "1A!",
        "first_name": TestDataGenerator.random_string(8).capitalize(),
        "last_name": TestDataGenerator.random_string(8).capitalize(),
        "phone": TestDataGenerator.random_phone_number(),
    }


@pytest.fixture(scope="function")
def api_test_data() -> Dict:
    """Generate API test data."""
    return {
        "user_id": TestDataGenerator.random_string(10),
        "session_token": TestDataGenerator.random_string(32),
        "request_id": TestDataGenerator.random_string(16),
        "timestamp": TestDataGenerator.random_date(),
    }
