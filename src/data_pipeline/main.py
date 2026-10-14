import json

from data_pipeline import fetch_daily_market_stocks, get_logger
from data_pipeline.config import ENVIRONMENT, POLYGON_BASE_URL, RAW_DATA_DIR
from data_pipeline.constants import (
    DEFAULT_ENCODING,
    DEFAULT_TARGET_DATE,
    JSON_INDENT,
    KEY_RESULTS,
    STOCK_FILENAME_TEMPLATE,
)

logger = get_logger(__name__)


def main(target_date: str = DEFAULT_TARGET_DATE):
    logger.info("--- Start --- Environment : %s", ENVIRONMENT)
    logger.info("Polygon URL : %s", POLYGON_BASE_URL)
    logger.info("Fetch data of %s...", target_date)
    
    try:
        data = fetch_daily_market_stocks(target_date)
        results = data.get(KEY_RESULTS, [])
        logger.info("Success to fetch data! Find %s stocks", len(results))
        
        # Create Raw Data Directory if not exists
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        output_filename = STOCK_FILENAME_TEMPLATE.format(target_date=target_date)
        output_file = RAW_DATA_DIR / output_filename
        
        with open(output_file, "w", encoding=DEFAULT_ENCODING) as f:
            json.dump(data, f, indent=JSON_INDENT)
        logger.info("Save file %s successfully!", output_file)
        
    except Exception:
        logger.exception("Failed to run Pipeline")


if __name__ == "__main__":
    main()