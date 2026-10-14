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

## IDE Debugger setup (vscode, antigravity, any vscode base ide)
#### you can debug this project by setup launch.json in .vscode folder 
#### add breakpoint at line need to debug
#### press F5 (Fn + F5 on mac, F5 on window, F5 on linux) to run debugger (or click debug button in ide)
#### if click debug button in ide then press ▶️ Run Data Pipeline
#### if you want change default debug target_date, modify lauch.json file (eg. line 18)
#### You can test with input date that you want to debug (eg. input : 2026-10-14)

## how to run pipeline with cronjob (system task scheduler)
