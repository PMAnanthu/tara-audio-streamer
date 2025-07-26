# tara-audio-streamer

## Overview
This project captures audio from the microphone at 16kHz, chunks it into 1-second blocks, and publishes each chunk as raw bytes to a ZeroMQ PUB socket. A subscriber can receive these packets and play the audio in real time.

## Features
- Real-time audio capture and streaming
- 16kHz mono audio, 1-second chunks
- ZeroMQ PUB/SUB communication
- Subscriber script plays audio through speakers

## Project Structure
```
src/
  audio_streamer.py      # Publishes audio packets

test/
  audio_subscriber.py    # Subscribes and plays audio packets

install_env.sh          # Script to set up Python environment and install dependencies
run_project.sh          # Script to run both publisher and subscriber
```

## Setup
1. **Install Python 3.10** (if not already installed)
2. **Set up the environment and dependencies:**
   ```bash
   bash install_env.sh
   ```
3. **Activate the environment:**
   ```bash
   source .venv/bin/activate
   ```

## Running the Project
To run both the audio streamer and subscriber together:
```bash
bash run_project.sh
```

Or, to run them separately:
- Start the publisher:
  ```bash
  python src/audio_streamer.py
  ```
- In another terminal, start the subscriber:
  ```bash
  python test/audio_subscriber.py
  ```

## Requirements
- Python 3.10
- sounddevice
- pyzmq
- numpy

## How it Works
- The publisher captures audio, chunks it, and sends packets like:
  ```python
  packet = {
      'startTime': <ms>,
      'endTime': <ms>,
      'data': <raw audio bytes>
  }
  ```
- The subscriber receives and plays each chunk in real time.

## License
MIT