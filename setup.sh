#!/usr/bin/env bash
set -euo pipefail

# Create venv if missing
if [ ! -d ".venv" ]; then
	python3 -m venv .venv
fi

# Activate (POSIX shells)
# shellcheck disable=SC1091
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Environment ready. Run the app with: python app.py"