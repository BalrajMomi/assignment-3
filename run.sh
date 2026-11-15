#!/bin/bash
echo "Setting up isolated Python Virtual Environment..."
python3 -m venv venv_temp
source venv_temp/bin/activate

echo "Installing package requirements..."
pip install -r requirements.txt

echo "Running machine learning pipeline..."
python main.py

deactivate
echo "Tearing down environment and removing temporary virtual files..."
rm -rf venv_temp

echo "Run completed. Exiting."
exit 0
