import numpy as np
def calculo_promedio(contenido):
    contenido_float = []
    contenido = contenido.split(", ")
    for i in range(len(contenido)):
        contenido_float.append(float(contenido[i].removeprefix("b'").removesuffix("'")))
    practicas = (contenido_float[0:4])
    labs = (contenido_float[4:14])
    ta = ([contenido_float[14]])
    practicas_arr = np.asarray(practicas)
    labs_arr = np.asarray(labs)
    practicas = practicas.remove(np.min(practicas_arr))
    labs = labs.remove(np.min(labs_arr))
    practicas_f = np.mean(np.asarray(practicas))
    labs_f = np.mean(np.asarray(labs))          
    nf = 3*practicas_f + 3*labs_f + 4*ta[0]
    #nf = 15
    #Al probar el modulo con un valor fijo de nf, el valor se envia a tracves del servidor;  pero
    #al ejecutar con las lineas de comando que se usan para calcular la nota final, hay un problema de tipos al usar np.mean

    

    #El problema que estás experimentando se debe a que la función np.mean() solo puede calcular la media de una matriz de números. En tu caso, la función np.mean() está tratando de calcular la media de una lista de cadenas de caracteres.
    #Para solucionar este problema, puedes usar la función np.asarray() para convertir la lista de cadenas de caracteres a una matriz de números. La función np.asarray() convierte cada elemento de la lista a un número.

    
    return nf
import socket
import numpy as np



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
                    data = str(calculo_promedio(str(data)))
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
