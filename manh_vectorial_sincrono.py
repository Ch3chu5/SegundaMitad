import numpy as np
import time

def sincrono(arreglo1,arreglo2):
    length=len(arreglo1)
    suma=0
    for i in range(length):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma


if __name__=='__main__':
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    listaTiempos=[]
    for i in range(100):
        t=time.perf_counter()
        sincrono(arreglo1,arreglo2)
        listaTiempos.append(time.perf_counter()-t)
    print(f"La mediana de los tiempos de ejecución del programa de forma síncrona es de {np.median(listaTiempos)} segundos.")

