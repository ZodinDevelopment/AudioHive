import pyaudio
import socket
import select

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

"""
def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        s.send(in_data)
    return (None, pyaudio.paContinue)
"""
def main():

    def callback(in_data, frame_count, time_info, status):
        for s in read_list[1:]:
            s.send(in_data)
        return (None, pyaudio.paContinue)


    audio = pyaudio.PyAudio()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('10.42.0.24', 4444))
    server.listen(5)


    #start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)

    read_list = [server]
    print('Recording ..')

    try:
        while True:
            readable, writable, errored = select.select(read_list, [], [])
            for s in readable:
                if s is server:
                    (clientsocket, address) = server.accept()
                    read_list.append(clientsocket)
                    print('Connection')
                else:
                    data = s.recv(1024)
                    if not data:
                        read_list.remove(s)
    except KeyboardInterrupt:
        pass 


    print('Finished')

    server.close()

    stream.stop_stream()
    stream.close()
    audio.terminate()



if __name__ == "__main__":
    main()


