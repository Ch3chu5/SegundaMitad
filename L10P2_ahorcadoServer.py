import random,socket,numpy as np

my_IP = "127.0.0.1"
port = 5000
dictionary = ["hola", "pucp", "ciclo", "arquitectura", "ingenieria", "servidor", "computadora", "amazon", "peru", "universidad", "jazz"]

if __name__ == "__main__":
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(f"Arrancando servidor en {my_IP}:{port}")
	s.bind((my_IP, port))
	s.listen(1)
	while True:
            try:
                print("Esperando conexión de un cliente")
                c,cAddr=s.accept()
                print(f"...conexion de: {cAddr}")
                ex=True
                while ex:
                    mensaje=c.recv(1024).decode()
                    if mensaje=='start':
                        print("recbi comando start")	
                        random_word=np.random.choice(dictionary)
                        print(f"Palabra elegida: {random_word}")
                        hidden_word='*'*len(random_word)
                        c.send(hidden_word.encode())
                        ex2=True
                        random_wordAux=list(random_word)
                        while ex2:
                            client_guess=c.recv(1024).decode()
                            if client_guess=='':
                                print("El cliente se ha desconectado.")
                                ex=False
                                break
                            print(f"Client guess: {client_guess}")
                            for idx in range(len(random_word)):
                                aux=0
                                if random_wordAux[idx] == client_guess:
                                    aux=1
                                    hidden_word = hidden_word[:idx] + client_guess + hidden_word[idx+1:]
                                    random_wordAux[idx]='*'
                                    if hidden_word==random_word:
                                        c.sendall('¡Lo conseguiste! La palabra correcta es: '.encode())
                                        ex2=False
                                        ex=False
                                    break
                            if aux==1:
                                c.sendall(hidden_word.encode())
                            else:
                                c.sendall(b'Intento Incorrecto')
                    elif mensaje=='':
                        print("El cliente se ha desconectado.")
                        break
                print("La partida ha finalizado.")
            except KeyboardInterrupt:
                print("Se ha interrumpido el programa.")
                break
