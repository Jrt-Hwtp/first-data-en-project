"""Constants for Data Pipeline.

This module contains fixed constants, templates, and configurations
that do not change across different environments.
"""

# Default Pipeline Parameters
DEFAULT_TARGET_DATE = "2026-10-13"

# File & Directory Settings
STOCK_FILENAME_TEMPLATE = "stocks_{target_date}.json"
DEFAULT_ENCODING = "utf-8"
JSON_INDENT = 4

# Logging Settings
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_FILENAME = "pipeline.log"

# API Parameters & Settings
API_TIMEOUT_SECONDS = 30
HTTP_STATUS_OK = 200
ADJUSTED_PARAM = "true"

# API Response Keys
KEY_RESULTS = "results"

# API Endpoints (Fixed Polygon API routes)
ENDPOINT_GROUPED_DAILY = "/v2/aggs/grouped/locale/us/market/stocks/{date}"
ENDPOINT_CUSTOM_BARS = "/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}"
ENDPOINT_PREVIOUS_CLOSE = "/v2/aggs/ticker/{ticker}/prev"

ENDPOINTS = {
    "grouped_daily": ENDPOINT_GROUPED_DAILY,
    "custom_bars": ENDPOINT_CUSTOM_BARS,
    "previous_close": ENDPOINT_PREVIOUS_CLOSE,
}
