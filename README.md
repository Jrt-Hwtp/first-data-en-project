# first-data-en-project

# *** Important ***
#### run this script before edit code or run project
#### ``` source .venv/bin/activate ```
#### if success this command it will display (venv name) if front of folder name in terminal
#### example: (first-data-en-project) ➜  first-data-en-project git:(feature/setup) ✗


## Project Structure should look like
### first-data-en-project/
### ├── .venv/
### ├── pyproject.toml
### ├── src/
### │   └── data_pipeline/
### │       ├── __init__.py
### │       ├── main.py
### │       └── weather.py
### └── tests/

## command
#### before edit or run : source .venv/bin/activate
#### run command: PYTHONPATH=src uv run python -m data_pipeline.main
#### example: 
##### (first-data-en-project) ➜  first-data-en-project git:(feature/setup) ✗ PYTHONPATH=src uv run python -m data_pipeline.main
##### --- Start --- Environment : development
##### Polygon URL : https://api.polygon.io
##### Fetch data of 2026-10-13...
##### Success to fetch data! Find 2710 stocks
##### Save file [pwd]/first-data-en-project/data/raw/stocks_2026-10-13.json successfully!