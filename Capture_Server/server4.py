import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2348))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"{address} connected.")  

    d = {1:"sending audio", 2:"playback"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

    print(msg)

    clientsocket.send(msg)


