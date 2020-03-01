import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
SECS = 5

def main():
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    monitor = p.open(format=p.get_format_from_width(WIDTH),
                     channels=CHANNELS,
                     rate=RATE,
                     output=True,
                     frames_per_buffer=CHUNK)

    print("@@@ RECORDING @@@")

    for i in range(0, int(RATE / CHUNK * SECS)):
        data = stream.read(CHUNK)
        monitor.write(data, CHUNK)

    print('* Done')

    stream.stop_stream()
    stream.close()
    monitor.stop_stream()
    monitor.close()
    p.terminate()


if __name__ == "__main__":
    main()

