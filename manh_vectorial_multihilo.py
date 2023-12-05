import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

#No se cambian los arreglos por iteración ya que sino cada medición del tiempo involucraría un diferente cálculo. Deben estar en igualdad de condiciones.

def multiHilo(arreglo1,arreglo2,hilos):
    return sum(list(PoolThreads.map(multiHiloAux,[[arreglo1,arreglo2,i,hilos] for i in range(hilos)])))

#Se usó la función .map tomando como argumento a un solo parámetro de entrada pero que conforma una lista con todos los argumentos necesarios.

def multiHiloAux(args):
    arreglo1,arreglo2,inicio,hilos=args #Se desempaquetan los argumentos
    length=len(arreglo1)
    suma=0
    for i in range(inicio,length,hilos):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma

if __name__=='__main__':
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    cantHilos=[1,2,4,8,16]
    for hilos in cantHilos:
        listaTiempos=[]
        PoolThreads=ThreadPoolExecutor(max_workers=hilos)
        for i in range(100):
            t=time.perf_counter()
            multiHilo(arreglo1,arreglo2,hilos)
            listaTiempos.append(time.perf_counter()-t)
        print(f"La mediana de los tiempos de ejecución del programa al emplear {hilos} hilos es de {np.median(listaTiempos)} segundos.")
