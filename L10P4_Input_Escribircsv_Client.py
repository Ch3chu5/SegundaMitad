import socket
SOCK_BUFFER = 1024
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    print(f"Conectando al servidor")
    sock.connect(server_address)
    try:
        while True: 
                msg = input()#No pongo mensaje para solicitar datos al cliente, para que se pueda añadir directamente a la linea que sera escrita al archivo csv
                sock.sendall(msg.encode("utf-8"))
                data = sock.recv(SOCK_BUFFER)
                data = data.decode("utf-8")
                print(f"Informacion solicitada: {data}")
                with open("resultados.csv", "w+", encoding="utf-8") as f:
                        f.write(f"{msg}, {data}\n")
    finally:
        sock.close()
