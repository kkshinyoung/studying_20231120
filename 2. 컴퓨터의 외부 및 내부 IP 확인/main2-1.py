import socket

if __name__ == '__main__':
    in_addr = socket.gethostbyname(socket.gethostname())

    print(in_addr)