import socket
SOCK_BUFFER = 1024
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    print(f"Servidor de chat escuchando en {server_address[0]}:{server_address[1]}")
    sock.bind(server_address)
    sock.listen(1)
    conn, client_address = sock.accept()
    print(f"Conexion entrante desde ('{client_address[0]}', {client_address[1]})")
    try:
        while True:
            
            data = conn.recv(SOCK_BUFFER)
            data = data.decode("utf-8")
            fin = 'exit'
            d_str = str(data)
            if (d_str != fin):
                print(f"Cliente: {data}")

                msg = input("Servidor: ")
                conn.sendall(msg.encode("utf-8"))
            else:
                print(f"Cliente: {data}")
                break
    finally:    
        conn.close()
