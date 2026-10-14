"""Data Pipeline Package."""

from data_pipeline.group_market_stock_api import fetch_daily_market_stocks

__version__ = "0.1.0"

__all__ = ["__version__", "fetch_daily_market_stocks"]
