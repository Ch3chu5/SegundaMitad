import socket
SOCK_BUFFER = 1024


if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5001)
    sock.connect(server_address)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address2 = ('127.0.0.1', 5000)
    sock2.connect(server_address2)
    try:
        while True: 
            data = sock.recv(SOCK_BUFFER)
            message = data.decode("utf-8")
            print(f"Informacion de uso del servidor {server_address[0]}:{server_address[1]}: {message}")
            data2 = sock2.recv(SOCK_BUFFER)
            message2 = data2.decode("utf-8")
            print(f"Informacion de uso del servidor {server_address2[0]}:{server_address2[1]}: {message2}")
    finally:
        print("Cerrando conexion")
        sock.close()
