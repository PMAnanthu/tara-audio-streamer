#!/bin/bash
# Script to activate the virtual environment and run the audio streamer and subscriber

set -e

ENV_DIR=".venv"

if [ ! -d "$ENV_DIR" ]; then
    echo "Virtual environment not found. Please run install_env.sh first."
    exit 1
fi

source $ENV_DIR/bin/activate

echo "Starting audio streamer (publisher)..."
python src/audio_streamer.py &
STREAMER_PID=$!

sleep 2  # Give the publisher time to start

echo "Starting audio subscriber (player)..."
python test/audio_subscriber.py

# Cleanup
kill $STREAMER_PID
