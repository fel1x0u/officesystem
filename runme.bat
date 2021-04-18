@echo off
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install -U -r requirements.txt
python main.py