import socket

if __name__ == '__main__':

    in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    in_addr.connect(("www.google.co.kr", 443))
    print(in_addr.getsockname()[0])