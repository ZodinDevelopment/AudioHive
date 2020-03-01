import os
import pyaudio
import wave
import socket
import time
import pickle


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SECS = 5


def capture():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    os.system('clear')

    print('@@@ Recording Now @@@')

    frames = []

    for i in range(0, int(RATE / CHUNK * SECS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print('@ Done Recording')

    stream.stop_stream()
    stream.close()
    p.terminate()
    
    print(f'Frames captured: {len(frames)}')
    audio_bytes = {}
    for key, frame in enumerate(frames):
        audio_bytes[key] = frames[key]

    msg = pickle.dumps(audio_bytes)

    msg = bytes(f"{len(msg):<{CHUNK}}", 'utf-8') + msg

    return msg
    
    #full_data = b''.join(frames)

    #print(f'Length of data {len(full_data)}')

    #return full_data 


def sendit():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('10.42.0.24', 2348))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"{address} connected.")

        input('Press enter to capture and send')

        msg = capture()


        clientsocket.send(msg)

if __name__ == "__main__":
    sendit()
