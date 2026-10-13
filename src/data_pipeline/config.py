import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# Search for .env at project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE)
else:
    load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Environment configuration settings for the data pipeline."""

    # Environment & Logging
    environment: str = field(
        default_factory=lambda: os.getenv("ENVIRONMENT", "development")
    )
    log_level: str = field(
        default_factory=lambda: os.getenv("LOG_LEVEL", "INFO")
    )

    # Weather API
    weather_api_key: str = field(
        default_factory=lambda: os.getenv("OPENWEATHER_API_KEY", "")
    )
    weather_city: str = field(
        default_factory=lambda: os.getenv("WEATHER_CITY", "Bangkok")
    )
    weather_api_url: str = field(
        default_factory=lambda: os.getenv(
            "WEATHER_API_URL", "https://api.openweathermap.org/data/2.5/weather"
        )
    )

    # AWS S3 (Data Lake)
    aws_access_key_id: str = field(
        default_factory=lambda: os.getenv("AWS_ACCESS_KEY_ID", "")
    )
    aws_secret_access_key: str = field(
        default_factory=lambda: os.getenv("AWS_SECRET_ACCESS_KEY", "")
    )
    aws_region: str = field(
        default_factory=lambda: os.getenv("AWS_DEFAULT_REGION", "ap-southeast-1")
    )
    s3_bucket: str = field(
        default_factory=lambda: os.getenv("S3_BUCKET_NAME", "")
    )
    s3_prefix: str = field(
        default_factory=lambda: os.getenv("S3_PREFIX", "raw/weather")
    )


settings = Settings()
