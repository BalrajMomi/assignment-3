# Mushroom Classification Pipeline Project

This project downloads the UCI Mushroom dataset, preprocesses categorical attributes using One-Hot Encoding, trains a Random Forest Classifier, and evaluates its predictive parameters.

## Method 1: Cross-Platform Clean Execution (No Remnants Left)
Run the automated wrapper scripts which initialize, execute, and destroy the temporary environment on exit.

### macOS / Linux
Open a terminal inside the project directory and run:
```bash
chmod +x run.sh
./run.sh
```

### Windows
Double-click `run.bat` or run it inside Command Prompt:
```cmd
run.bat
```

## Method 2: Vanilla Execution (Manual Step-by-Step)
If you prefer setting up the workspace manually:

1. Establish a standard Python Virtual Environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual workspace:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate.bat`
3. Install libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute pipeline:
   ```bash
   python main.py
   ```
