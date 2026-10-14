import json

from data_pipeline import fetch_daily_market_stocks
from data_pipeline.config import POLYGON_BASE_URL, RAW_DATA_DIR, ENVIRONMENT
from data_pipeline.constants import (
    DEFAULT_ENCODING,
    DEFAULT_TARGET_DATE,
    JSON_INDENT,
    KEY_RESULTS,
    STOCK_FILENAME_TEMPLATE,
)

def main(target_date: str = DEFAULT_TARGET_DATE):
    print(f"--- Start --- Environment : {ENVIRONMENT}")
    print(f"Polygon URL : {POLYGON_BASE_URL}")
    print(f"Fetch data of {target_date}...")
    
    try:
        data = fetch_daily_market_stocks(target_date)
        results = data.get(KEY_RESULTS, [])
        print(f"Success to fetch data! Find {len(results)} stocks")
        
        # Create Raw Data Directory if not exists
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        output_filename = STOCK_FILENAME_TEMPLATE.format(target_date=target_date)
        output_file = RAW_DATA_DIR / output_filename
        
        with open(output_file, "w", encoding=DEFAULT_ENCODING) as f:
            json.dump(data, f, indent=JSON_INDENT)
        print(f"Save file {output_file} successfully!")
        
    except Exception as e:
        print(f"Failed to run Pipeline: {e}")

if __name__ == "__main__":
    main()