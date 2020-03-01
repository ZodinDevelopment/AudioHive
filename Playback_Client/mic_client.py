import pyaudio
import socket 
import sys

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('10.42.0.24', 4444))

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

    try:
        while True:
            data = s.recv(CHUNK)
            stream.write(data)
    except KeyboardInterrupt:
        pass

    print('Closing down')
    s.close()
    stream.close()
    audio.terminate()



if __name__ == "__main__":
    main()


