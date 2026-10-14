import os
from dotenv import load_dotenv

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
POLYGON_BASE_URL = os.getenv("POLYGON_BASE_URL", "https://api.polygon.io")

if not POLYGON_API_KEY:
    raise ValueError("POLYGON_API_KEY is missing. Please provide it in the .env file")

ENDPOINTS = {
    "grouped_daily": "/v2/aggs/grouped/locale/us/market/stocks/{date}",
    "custom_bars": "/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}",
    "previous_close": "/v2/aggs/ticker/{ticker}/prev"
}