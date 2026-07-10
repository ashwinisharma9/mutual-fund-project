@echo off

cd /d "C:\Users\Dell\Desktop\mutual fund project"

call venv\Scripts\activate

python scripts\etl_pipeline.py >> logs\etl_log.txt 2>&1