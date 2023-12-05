import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 20 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

vocales=['a','e','i','o','u']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

def fuerza_b():
	for primeraL in vocales:
		for segundaL in vocales:
			for terceraL in abecedario:
				if comparar_con_password_correcto(primeraL+segundaL+terceraL):
					return primeraL+segundaL+terceraL
	return False

def fuerza_b_paralelo(primeraL):
	for segundaL in vocales:
		for terceraL in abecedario:
			if comparar_con_password_correcto(primeraL+segundaL+terceraL):
				return primeraL+segundaL+terceraL
	return False

def paralelo():
	p=Pool(processes=5)
	resultados=p.map(fuerza_b_paralelo,('a','e','i','o','u'))
	p.close()
	if resultados[0]!=False:
		return resultados[0]
	elif resultados[1]!=False:
		return resultados[1]
	elif resultados[2]!=False:
		return resultados[2]
	elif resultados[3]!=False:
		return resultados[3]
	elif resultados[4]!=False:
		return resultados[4]
	else: 
		return False

if __name__ == "__main__":
	
	t1=time.perf_counter()
	clave_s=fuerza_b()
	t2=time.perf_counter()
	clave_p=paralelo()
	t3=time.perf_counter()
	if clave_s:
		print(f"La clave encontrada por el método serial es {clave_s} y el tiempo de ejecución es {t2-t1}")
	if not clave_s:
		print("La contraseña no fue encontrada serialmente")
	if clave_p:
		print(f"La clave encontrada por el método paralelo es {clave_p} y el tiempo de ejecución es {t3-t2}")
	if not clave_s:
		print("La contraseña no fue encontrada paralelamente")
