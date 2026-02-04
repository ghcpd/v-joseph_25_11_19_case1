#!/bin/bash

# Test runner script for Flask Project Management System
# This script runs all test files and reports results

echo "=========================================="
echo "Flask Project Management System - Test Suite"
echo "=========================================="
echo ""

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Warning: Virtual environment not activated."
    echo "Attempting to activate..."
    if [ -f ".venv/bin/activate" ]; then
        source .venv/bin/activate
        echo "Virtual environment activated."
    else
        echo "Error: Virtual environment not found. Run setup.sh first."
        exit 1
    fi
fi

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "Error: pytest is not installed."
    echo "Installing test dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "Running all tests..."
echo "=========================================="
echo ""

# Run all tests with verbose output
python -m pytest test_files/ -v --tb=short

# Capture exit code
TEST_EXIT_CODE=$?

echo ""
echo "=========================================="

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✓ All tests passed!"
else
    echo "✗ Some tests failed. See output above for details."
fi

echo "=========================================="
echo ""
echo "To run tests with coverage, use:"
echo "  python -m pytest test_files/ --cov=app --cov-report=html"
echo ""
echo "To run specific test file:"
echo "  python -m pytest test_files/test_app.py -v"
echo "=========================================="

exit $TEST_EXIT_CODE