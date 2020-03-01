import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2348))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    print(f"Connection from {address}")

    msg = """Come not between the nazgul and his pray, or he will not slay thee in thy turn. He will bear thee away to the houses of lamentation, beyond all darkkness. Where thy flesh shall be devoured and thy shrivelled mind left naked to the lidless eye!"""

    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,'utf-8'))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg, 'utf-8'))
