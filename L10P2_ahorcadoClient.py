import socket
host = "127.0.0.1"
port = 5000
size = 2048

#esta codigo es dato lo unico a modificar es el server

if __name__=='__main__':
	print("Conectandome a servidor....")
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			s.connect((host,port))
			break
		except ConnectionRefusedError:
			print("El puerto del servidor no se ha inicializado...\nReintentando.")
	print("¡Conectado!")

	while True:
		cmd=input("Tipee lo que quieres enviar:\n")
		if cmd=='stop':
			s.close()
			break
		elif cmd!='start':
			print("Ingrese 'start' para iniciar el juego o 'stop' para finalizar el programa.")
		else:
			s.send(b'start')
			word_received=s.recv(1024).decode()
			print("Mensaje recibido: ",word_received)
			print("Tienes 5 oportunidades!")
			contadorEquivocaciones=0
			aux=0
			while True:
					print("Tipee lo que quieres enviar:")
					cmd=input()
					if len(cmd)==1:
						s.send(cmd.encode())
						word_received=s.recv(1024).decode()
						contadorEquivocaciones+=(word_received=='Intento Incorrecto')
						print("Mensaje recibido: ",word_received)
						if contadorEquivocaciones==5:
							print("Ha fallado 5 veces.")
							break
					else:
						print("Ingrese un caracter.")
					if word_received[0:16]=='¡Lo conseguiste!':
						break
			print("Partida finalizada.\nEscribe 'start' si deseas seguir jugando o 'stop' para acabar el programa")
			
