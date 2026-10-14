import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()



# Project Paths
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
POLYGON_BASE_URL = os.getenv("POLYGON_BASE_URL", "https://api.polygon.io")

if not POLYGON_API_KEY:
    raise ValueError("POLYGON_API_KEY is missing. Please provide it in the .env file")