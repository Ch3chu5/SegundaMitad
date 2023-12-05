import socket
SOCK_BUFFER = 1024
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)
    print(f"Conectando al servidor")
    sock.connect(server_address)
    try: 
        while True:
            msg = input("Ingrese el nombre del electrodoméstico: ")

            sock.sendall(msg.encode("utf-8"))
            data = sock.recv(SOCK_BUFFER)
            data = data.decode("utf-8")
            if data == "1":
                print("Producto en stock. Pedido procesado")
            else:
                print("Producto agotado. Pedido no aceptado")
                           
    finally:
        sock.close()
