#!/bin/bash
# Script to create Python virtual environment and install required libraries

set -e

ENV_DIR=".venv"
PYTHON_BIN="python3.10"

# Create virtual environment if it doesn't exist
if [ ! -d "$ENV_DIR" ]; then
    $PYTHON_BIN -m venv $ENV_DIR
    echo "Created virtual environment in $ENV_DIR"
fi

# Activate virtual environment
source $ENV_DIR/bin/activate

echo "Installing required libraries..."
pip install --upgrade pip
pip install sounddevice pyzmq numpy

echo "All dependencies installed. To activate the environment, run:"
echo "source $ENV_DIR/bin/activate"
