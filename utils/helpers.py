"""Utility helper classes for common operations."""

import logging
import os


class Logger:  # pylint: disable=too-few-public-methods
    """Custom logger utility.

    This class provides methods for setting up and configuring loggers with
    both console and file output for test automation logging needs.
    """

    @staticmethod
    def setup_logger(
        name: str,
        log_file: str = None,
        level: int = logging.INFO,
        file_level: int = None,
        console_level: int = None,
    ) -> logging.Logger:
        """Set up a logger with file and console handlers.

        Args:
            name (str): The name for the logger (usually the module or class name).
            log_file (str, optional): Path to the log file. If provided, logs will be written
                                     to this file in addition to console. Defaults to None.
            level (int): The default logging level (e.g., logging.INFO, logging.DEBUG).
                        Defaults to logging.INFO.
            file_level (int, optional): The logging level for the file handler.
                                        If not provided, uses the default level.
            console_level (int, optional): The logging level for the console handler.
                                           If not provided, uses the default level.

        Returns:
            logging.Logger: A configured logger instance with the specified name and handlers.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Clear existing handlers to avoid duplicate log entries on repeated calls
        logger.handlers.clear()

        # Use provided levels or fall back to default level
        actual_console_level = console_level if console_level is not None else level
        actual_file_level = file_level if file_level is not None else level

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(actual_console_level)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler (if log_file is provided)
        if log_file:
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(actual_file_level)
            file_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
            )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

        return logger
