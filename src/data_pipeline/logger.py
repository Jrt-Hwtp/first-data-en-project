"""Centralized logging configuration for Data Pipeline."""

import logging

from data_pipeline.config import LOGS_DIR
from data_pipeline.constants import (
    DEFAULT_ENCODING,
    DEFAULT_LOG_FILENAME,
    LOG_DATE_FORMAT,
    LOG_FORMAT,
)


def setup_logging(
    log_filename: str = DEFAULT_LOG_FILENAME,
    level: int = logging.INFO,
) -> None:
    """Configure root logging handlers for console and file output."""
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Avoid adding duplicate handlers if setup_logging is called multiple times
    if not root_logger.handlers:
        formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

        # 1. Console Handler (Standard Output)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

        # 2. File Handler (Save to logs/pipeline.log)
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        file_path = LOGS_DIR / log_filename
        file_handler = logging.FileHandler(file_path, encoding=DEFAULT_ENCODING)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    # Silence noisy third-party loggers
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)


def get_logger(name: str | None = None) -> logging.Logger:
    """Initialize logging and return a logger instance for the given module name."""
    setup_logging()
    return logging.getLogger(name or "data_pipeline")
