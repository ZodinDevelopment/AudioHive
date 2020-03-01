import socket
import time 


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2348))
s.listen(5)


while True:

    clientsocket, address = s.accept()
    print(f"Connection from {address}")

    msg = "This is some arbitrary unicode string to be sent in bytes form through the socket to the client."

    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg, 'utf-8'))


