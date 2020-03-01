import socket 


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2348))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("data length:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False


        print(f"Length of total data: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print('Data receieved.')
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""



    
