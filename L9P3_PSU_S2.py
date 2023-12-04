import socket
import time
import psutil
def monitorizar_recursos():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_info = psutil.virtual_memory()
    msg = (f"CPU usage: {cpu_percent}% | RAM usage: {mem_info.percent}%")
    time.sleep(5)
    return msg
SOCK_BUFFER = 1024
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)
    sock.bind(server_address)
    sock.listen(1)
    print(f"Conexion desde {server_address[0]}:{server_address[1]}")
    while True:
        conn, client_address = sock.accept()
        try:
            while True:
                msg = monitorizar_recursos()
                conn.sendall(msg.encode("utf-8"))
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
