#!/usr/bin/env bash
set -euo pipefail

./setup.sh

.venv/bin/python -m pytest -q -s test_files
