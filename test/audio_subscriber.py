import zmq
import sounddevice as sd
import numpy as np

ZMQ_SUB_ADDRESS = "tcp://localhost:5555"
SAMPLE_RATE = 16000

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(ZMQ_SUB_ADDRESS)
socket.setsockopt_string(zmq.SUBSCRIBE, "")

print("Listening for audio packets and playing through speaker...")

while True:
    packet = socket.recv_pyobj()
    audio_data = np.frombuffer(packet['data'], dtype=np.int16)
    sd.play(audio_data, samplerate=SAMPLE_RATE)
    sd.wait()
    print(f"Played packet: startTime={packet['startTime']}, endTime={packet['endTime']}, data_length={len(packet['data'])} bytes")
