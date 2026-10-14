import requests

from data_pipeline.config import POLYGON_API_KEY, POLYGON_BASE_URL
from data_pipeline.constants import (
    ADJUSTED_PARAM,
    API_TIMEOUT_SECONDS,
    ENDPOINTS,
    HTTP_STATUS_OK,
)


def fetch_daily_market_stocks(target_date: str) -> dict:
    """Get daily market stocks data from Polygon API"""
    endpoint = ENDPOINTS["grouped_daily"].format(date=target_date)
    url = f"{POLYGON_BASE_URL}{endpoint}"
    
    params = {
        "adjusted": ADJUSTED_PARAM,
        "apiKey": POLYGON_API_KEY,
    }
    
    response = requests.get(url, params=params, timeout=API_TIMEOUT_SECONDS)
    
    # If HTTP Status is not 200 (e.g., 401 Key is wrong or 429 exceeded limit) raise an error immediately
    if response.status_code != HTTP_STATUS_OK:
        raise Exception(f"API Error (Status {response.status_code}): {response.text}")
        
    return response.json()