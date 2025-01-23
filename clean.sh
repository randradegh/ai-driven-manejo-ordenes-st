#!/bin/bash

echo "Cleaning project..."

# Remove Python cache files
echo "Removing Python cache files..."
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete

# Remove build artifacts
echo "Removing build artifacts..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# Remove virtual environment
echo "Removing virtual environment..."
rm -rf venv/
rm -rf env/