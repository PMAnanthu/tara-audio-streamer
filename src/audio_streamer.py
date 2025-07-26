import sounddevice as sd
import zmq
import time
import numpy as np

SAMPLE_RATE = 16000  # 16kHz
CHUNK_DURATION = 1  # seconds
CHUNK_SIZE = SAMPLE_RATE * CHUNK_DURATION
ZMQ_PUB_ADDRESS = "tcp://*:5555"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(ZMQ_PUB_ADDRESS)

print(f"Publishing audio chunks at {SAMPLE_RATE}Hz, {CHUNK_DURATION}s per chunk on {ZMQ_PUB_ADDRESS}")

def audio_callback(indata, frames, time_info, status):
    global start_time
    if status:
        print(status)
    end_time = int(time.time() * 1000)
    packet = {
        'startTime': start_time,
        'endTime': end_time,
        'data': indata.tobytes()
    }
    socket.send_pyobj(packet)
    start_time = end_time

start_time = int(time.time() * 1000)

with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='int16', blocksize=CHUNK_SIZE, callback=audio_callback):
    print("Streaming... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")
