import socket
SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)


    sock.connect(server_address)

    try:
        data = sock.recv(SOCK_BUFFER)
        msg = data.decode("utf-8")
        print(f"{msg}") 
    finally:
        sock.close()
