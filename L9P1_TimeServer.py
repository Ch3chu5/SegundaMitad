import socket
import datetime
SOCK_BUFFER = 1024
def tiempo():
    rn = datetime.datetime.now()
    tiempo = f"{rn:%a %b %d %H:%M:%S %Y}"
    return tiempo

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    sock.bind(server_address)
    sock.listen(1)
    print(f"Servidor de tiempo escuchando en {server_address[0]}:{server_address[1]}")
    while True:
        conn, client_address = sock.accept()
        print(f"Conexion entrante desde ('{client_address[0]}', {client_address[1]})")
        try:
            data = tiempo()
            conn.sendall(data.encode("utf-8"))
        finally:
            conn.close()
