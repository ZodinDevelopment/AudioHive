import os
import pyaudio
import wave
import socket
import time
import pickle 

CHUNK = 1024
CHANNELS = 2
FORMAT = pyaudio.paInt16
RATE = 44100


def playback_data(data, p):
    
    input('Press enter >> ')

    stream = p.open(format=p.get_format_from_width(data.getsampwidth()),
                    channels=data.getnchannels(),
                    rate=data.getframerate(),
                    output=True)

    audio = data.readframes(CHUNK)

    while audio != '':
        stream.write(audio)
        audio = data.readframes(CHUNK)
        if len(audio) <= 0:
            break
    stream.stop_stream()
    stream.close()

    p.terminate()
    data.close()
    print('Complete!')
    print('Reconnecting to server.')
    time.sleep(2)






def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.42.0.24', 2348))

    while True:

        full_msg = b''
        new_msg = True

        while True:
            msg = s.recv(1024)
            if new_msg:
                print('Received:',msg[:CHUNK])
                msglen = int(msg[:CHUNK])
                new_msg = False

            full_msg += msg

            print(len(full_msg))

            if len(full_msg)-CHUNK == msglen:
                print('Received audio.')
                print(full_msg[CHUNK:])
                data = pickle.loads(full_msg[CHUNK:])
                data = list(data.values())
                data = b''.join(data)
                p = pyaudio.PyAudio()
                os.system('clear')
                wf = wave.open('data.wav', 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(data)
                wf.close()


                FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.wav')

                data = wave.open(FILE, 'rb')
                playback_data(data, p)
                
                new_msg = True
                full_msg = b""


if __name__ == "__main__":
    main()

