import socket
#como los valores de un factorial son muy grandes, el valor de socket buffer tambien
#tiene que ser grande, en este caso puse el mismo que el del servidor
SOCK_BUFFER = 1024


if __name__ == "__main__":

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)


    sock.connect(server_address)

    try:
        msg = input("Ingrese un numero: ")
        sock.sendall(msg.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)#Linea que recibe la data enviada por el servidor.
        print(f"El factorial del numero ingresado es:  {data}") #Imprimir la data recibida
    finally:
        print("Cerrando conexion")
        sock.close()
