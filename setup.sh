#!/bin/bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Note for Windows PowerShell users:
# run the following in PowerShell instead of running this script:
# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# pip install -r requirements.txt
