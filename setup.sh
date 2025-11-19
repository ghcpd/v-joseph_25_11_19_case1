#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

if [ ! -d ".venv" ]; then
  "${PYTHON_BIN}" -m venv .venv
fi

if [ ! -x ".venv/bin/pip3" ]; then
  .venv/bin/python -m ensurepip
fi

.venv/bin/pip3 install -r requirements.txt
