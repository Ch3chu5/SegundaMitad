def factorial(x):
    if x == 0:
        return 1
    else:
        f= 1
        for i in range(1,x+1):
            f = f*i
        return f

import socket
SOCK_BUFFER = 4


import socket

SOCK_BUFFER = 1024


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    print(f"Iniciando servidor en IP {server_address[0]} y puerto {server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        try:
            while True:
                data = conn.recv(SOCK_BUFFER) 

                if data:
                    data = str(factorial(int(data)))
                    print(f"Enviando:  {data}")
                    conn.sendall(data.encode("utf-8"))
                else:
                    print(f"No hay mas datos")
                    break
        except ConnectionResetError:
            print("el cliente ha cerrado abruptamente la conexion")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
