@echo off
echo Setting up isolated Python Virtual Environment...
python -m venv venv_temp
call venv_temp\Scripts\activate.bat

echo Installing package requirements...
pip install -r requirements.txt

echo Running machine learning pipeline...
python main.py

call venv_temp\Scripts\deactivate.bat
echo Tearing down environment and removing temporary virtual files...
rd /s /q venv_temp

echo Run completed. Exiting.
pause
exit /b 0
