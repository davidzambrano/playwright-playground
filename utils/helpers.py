"""Utility helper classes for test data generation and common operations."""

import logging
import os
import random
import string
import time
from datetime import datetime


class TestDataGenerator:
    """Utility class for generating test data.

    This class provides static methods for generating various types of test data
    including strings, emails, phone numbers, and dates for use in automated tests.
    """

    @staticmethod
    def random_string(length: int = 10) -> str:
        """Generate a random string of specified length.

        Args:
            length (int): The length of the string to generate. Defaults to 10.

        Returns:
            str: A random string containing letters and digits.
        """
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def random_email() -> str:
        """Generate a random email address.

        Returns:
            str: A randomly generated email address in the format username@domain.com.
        """
        username = TestDataGenerator.random_string(8).lower()
        domain = f"{TestDataGenerator.random_string(5).lower()}.com"
        return f"{username}@{domain}"

    @staticmethod
    def random_phone_number() -> str:
        """Generate a random US phone number.

        Returns:
            str: A randomly generated US phone number in the format (XXX) XXX-XXXX.
        """
        area_code = random.randint(200, 999)
        exchange = random.randint(200, 999)
        number = random.randint(1000, 9999)
        return f"({area_code}) {exchange}-{number}"

    @staticmethod
    def random_date(start_year: int = 1990, end_year: int = 2005) -> str:
        """Generate a random date in YYYY-MM-DD format.

        Args:
            start_year (int): The starting year for date generation. Defaults to 1990.
            end_year (int): The ending year for date generation. Defaults to 2005.

        Returns:
            str: A random date in YYYY-MM-DD format between the specified years.
        """
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date.strftime("%Y-%m-%d")


class ScreenshotManager:
    """Utility class for managing screenshots.

    This class provides methods for ensuring screenshot directories exist
    and generating unique screenshot filenames for test automation.
    """

    @staticmethod
    def ensure_screenshot_directory() -> None:
        """Ensure screenshot directory exists.

        Creates the 'reports/screenshots' directory if it doesn't already exist.
        This method is safe to call multiple times.
        """
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

    @staticmethod
    def generate_screenshot_name(test_name: str, timestamp: bool = True) -> str:
        """Generate a unique screenshot filename.

        Args:
            test_name (str): The base name for the screenshot (usually the test name).
            timestamp (bool): Whether to include a timestamp in the filename. Defaults to True.

        Returns:
            str: A unique screenshot filename with .png extension.
                 If timestamp is True, includes YYYYMMDD_HHMMSS format.
                 If timestamp is False, returns just test_name.png.
        """
        if timestamp:
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            return f"{test_name}_{timestamp_str}.png"
        return f"{test_name}.png"


class WaitHelper:  # pylint: disable=too-few-public-methods
    """Utility class for custom wait conditions.

    This class provides methods for implementing custom wait logic that can be used
    when built-in waits are not sufficient for specific test scenarios.
    """

    @staticmethod
    def wait_for_condition(
        condition_func, timeout: int = 10000, poll_interval: int = 500
    ) -> bool:
        """Wait for a custom condition to be true.

        Args:
            condition_func (callable): A function that returns True when the condition is met.
                                       This function should be callable with no arguments.
            timeout (int): Maximum time to wait in milliseconds. Defaults to 10000 (10 seconds).
            poll_interval (int): Time to wait between condition checks in milliseconds.
                                Defaults to 500 (0.5 seconds).

        Returns:
            bool: True if the condition was met within the timeout period, False otherwise.
        """
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            if condition_func():
                return True
            time.sleep(poll_interval / 1000)
        return False


class Logger:  # pylint: disable=too-few-public-methods
    """Custom logger utility.

    This class provides methods for setting up and configuring loggers with
    both console and file output for test automation logging needs.
    """

    @staticmethod
    def setup_logger(
        name: str, log_file: str = None, level: int = logging.INFO
    ) -> logging.Logger:
        """Set up a logger with file and console handlers.

        Args:
            name (str): The name for the logger (usually the module or class name).
            log_file (str, optional): Path to the log file. If provided, logs will be written
                                     to this file in addition to console. Defaults to None.
            level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
                        Defaults to logging.INFO.

        Returns:
            logging.Logger: A configured logger instance with the specified name and handlers.

        Note:
            This method clears any existing handlers on the logger before setting up new ones.
            File handler includes more detailed formatting than console handler.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Clear existing handlers
        logger.handlers.clear()

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler (if log_file is provided)
        if log_file:
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(funcName)s:%(lineno)d - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        return logger
