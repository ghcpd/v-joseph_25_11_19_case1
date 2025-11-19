#!/bin/bash
set -e

# Run tests using pytest (no server required; tests use Flask test_client)
python -m venv .venv || true
source .venv/bin/activate || true
pip install -r requirements.txt
pip install pytest

echo "Running pytest..."
pytest -q
