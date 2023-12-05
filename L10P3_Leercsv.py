import socket
#como los valores de un factorial son muy grandes, el valor de socket buffer tambien
#tiene que ser grande, en este caso puse el mismo que el del servidor
SOCK_BUFFER = 1024


if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)


    sock.connect(server_address)

    try:
        with open("notas.csv", "r") as f:
            contenido = f.read()
        msg = contenido
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)#Linea que recibe la data enviada por el servidor.
        print(f"El promedio final del alumno es:  {data}") #Imprimir la data recibida
    finally:
        print("Cerrando conexion")
        sock.close()
