import socket 

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 2348))
    s.listen(5)

    while True:

        clientsocket, address = s.accept()
        print(f"Connected.")
        clientsocket.send(bytes("Some fuckin data.", "utf-8"))
        clientsocket.close()


if __name__ == "__main__":
    main()
