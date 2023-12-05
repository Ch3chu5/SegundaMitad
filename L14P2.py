import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool

"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""

def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

    
    histograma_list = [0] * 256
    for i in range(M):
        for j in range(N):
            histograma_list[imagen[i][j]] += 1
    return histograma_list

"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def paralelizacion(args):
    imagen, filename, color = args
    return graficar_histograma(calcular_histograma(imagen), filename, color)

imagenes_x2 = ['goldhill_x2.npy', 'hong kong_x2.npy', 'lena_x2.npy', 'stonehenge_x2.npy']
imagenes = ['goldhill.npy', 'hong kong.npy', 'lena.npy', 'stonehenge.npy']
filename_serial = ['grafico1s', 'grafico2s', 'grafico3s', 'grafico4s']
filename_paralelo = ['grafico1p', 'grafico2p', 'grafico3p', 'grafico4p']
filename_serial_small = ['grafico1ss', 'grafico2ss', 'grafico3ss', 'grafico4ss']
filename_paralelo_small = ['grafico1ps', 'grafico2ps', 'grafico3ps', 'grafico4ps']
color = ['red' , 'green', 'blue', 'yellow']
if __name__ == '__main__':
    # Parte a: Calculo del histograma en serial
    tic = time.perf_counter()
    for i in range(4):
        graficar_histograma(calcular_histograma(imagenes_x2[i]), filename_serial[i], color[i])
    toc = time.perf_counter()
    tiempo_serial = toc - tic
    print(f"Tiempo total en serie: {tiempo_serial}")

    # Parte b: Calculo del histograma en paralelo
    
    tic_paralelo = time.perf_counter()
    args = zip(imagenes_x2, filename_paralelo, color)
    with Pool(processes= 4) as p:
        p.map(paralelizacion, args)
    toc_paralelo = time.perf_counter()
    tiempo_paralelo = toc_paralelo - tic_paralelo
    print(f'Tiempo de ejecucion en paralelo: {tiempo_paralelo}s')
    print(f"SpeedUp : {tiempo_serial /tiempo_paralelo }") #La version paralelizada es mas rapida
    
    ##########Ahora con las imagenes mas pequeñas###################
    print("----------------------------Ahora para imagenes más pequeñas----------------------------")
    tic = time.perf_counter()
    for i in range(4):
        graficar_histograma(calcular_histograma(imagenes[i]), filename_serial[i], color[i])
    toc = time.perf_counter()
    tiempo_serial = toc - tic
    print(f"Tiempo total en serie: {tiempo_serial}")

    
    tic_paralelo = time.perf_counter()
    args = zip(imagenes, filename_paralelo, color)
    with Pool(processes= 4) as p:
        p.map(paralelizacion, args)
    toc_paralelo = time.perf_counter()
    tiempo_paralelo = toc_paralelo - tic_paralelo
    print(f'Tiempo de ejecucion en paralelo: {tiempo_paralelo} s')
    print(f"SpeedUp : {tiempo_serial /tiempo_paralelo }") #La version serial es mas rapida(En algunos casos; me toco apreciar una ejecucion en la que sucedia esto); esto debido a que levantar cada Process toma su tiempo y, al ser operaciones que no saturan tanto a la CPU (se puede apreciar en el tiempo de ejecucion), la version serial termina siendo más rápida
