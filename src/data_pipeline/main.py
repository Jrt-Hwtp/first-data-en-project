import json
from data_pipeline import fetch_daily_market_stocks

# def main():
#     print(f"Environment : {settings.environment}")
#     print(f"Polygon URL : {settings.polygon_api_url}")

def main():
    target_date = "2026-10-13"
    print(f"Fetch data of {target_date}...")
    
    try:
        data = fetch_daily_market_stocks(target_date)
        results = data.get("results", [])
        print(f"Success to fetch data! Find {len(results)} stocks")
        
        output_file = f"stocks_{target_date}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Save file {output_file} successfully!")
        
    except Exception as e:
        print(f"Failed to run Pipeline: {e}")

if __name__ == "__main__":
    main()