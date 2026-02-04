#!/bin/bash

# Setup script for Flask Project Management System
# This script creates a virtual environment and installs dependencies

echo "Setting up Flask Project Management System..."

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "Error: Python is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Use python3 if available, otherwise use python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "Using Python: $PYTHON_CMD"

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON_CMD -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run the app, run:"
echo "  python app.py"
echo ""
echo "To run tests, run:"
echo "  bash run_tests.sh"
echo "=========================================="