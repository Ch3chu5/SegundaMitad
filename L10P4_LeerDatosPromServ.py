import numpy as np
def abrir_archivo():
    with open("data.csv", "r") as f:
        contenido = f.read()
        return contenido
def promedio_edades():
    info = abrir_archivo()
    info_flat = info.split(", ")
    edades= []
    i =1
    while i < 30:
        edades.append(info_flat[i])
        i+=3
    edades_np = np.asarray(edades)
    edades_avg = np.mean(edades_np)
    return edades_avg
#Los otros modulos que faltan, siguen la msma logica. el ultimo enparticular es restar 10-cant_sanos
#Se tiene que crear un arreglo con la columna de estado del paciente y contar cuantos "1" se encuentras, para cant_enfermos
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

                    print(f"Opcion recibida: {data}")
                    if str(data) == "a":
                        msg = promedio_edades()
                    if str(data) == "b":
                        msg = "falto tiempo" #cant_enfermos()
                    if str(data) == "c":
                        msg = "falto tiempo" #cant_sanos()
                    conn.sendall(data.encode("utf-8"))
                else:
                    print(f"No hay mas datos")
                    break
        except ConnectionResetError:
            print("el cliente ha cerrado abruptamente la conexion")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()
