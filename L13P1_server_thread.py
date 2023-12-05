import socket
import time
from threading import Thread
SOCK_BUFFER = 1024
stock = {"lavadora": 5, "refrigerador": 3, "aspiradora": 2, "licuadora": 4}
def conn_handle(conn,client_address):
    print(f"Conexion desde {client_address[0]}:{client_address[1]}")
    try:
        while True:
            data = conn.recv(SOCK_BUFFER)
            data = data.decode("utf-8")
            msg ="0"
            if data in stock:
                if stock[data] > 0:
                    msg = "1"
                    stock[data]-=1
            conn.sendall(msg.encode("utf-8"))
            print(stock)#De esta manera se monitorea desde el cliente como va variando el stock
    except ConnectionResetError:
        print("el cliente ha cerrado abruptamente la conexion")
    finally:
        
        conn.close()

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)
    sock.bind(server_address)
    sock.listen(5)#Numero de clientes que puede manejar el servidor de manera simultantea(Elegi 5 porque es un numero razonable teniendo en cuenta el total de elementos en stock de la tienda)
    
    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        #ejecucion hilos
        t1 = Thread(target = conn_handle, args = (conn,client_address))
        t1.start()
