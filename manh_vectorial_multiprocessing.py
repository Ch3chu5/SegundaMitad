import numpy as np
import time
from multiprocessing import Pool

#No se cambian los arreglos por iteración ya que sino cada medición del tiempo involucraría un diferente cálculo. Deben estar en igualdad de condiciones.

def multiProcess(arreglo1,arreglo2,procesos):
    return sum(PoolProcess.starmap(multiProcessAux,([arreglo1,arreglo2,i,procesos] for i in range(procesos))))

def multiProcessAux(arreglo1,arreglo2,inicio,procesos):
    length=len(arreglo1)
    suma=0
  #La sentencia for i in range(inicio,length,procesos): itera sobre el arreglo arreglo1 desde el índice inicio hasta el índice length - 1, 
  #avanzando de a procesos índices cada vez. Por ejemplo, si inicio es 0, length es 10 y procesos es 2, la sentencia for iterará sobre los índices 0, 2, 4, 6, 8, 10.
    for i in range(inicio,length,procesos):
        suma+=abs(arreglo2[i]-arreglo1[i])
    return suma

if __name__=='__main__':
    cantProcesos=[1,2,4,8,16]
    arreglo1=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    arreglo2=np.random.randint(-100000,100001,size=4096,dtype=np.int32)
    for procesos in cantProcesos:
        listaTiempos=[]
        PoolProcess=Pool(processes=procesos)
        for i in range(100):
            t=time.perf_counter()
            multiProcess(arreglo1,arreglo2,procesos)
            listaTiempos.append(time.perf_counter()-t)
        print(f"La mediana de los tiempos de ejecución del programa al emplear {procesos} procesos es de {np.median(listaTiempos)} segundos.")
        PoolProcess.close()
        PoolProcess.join()

#Se cierra el Pool de Procesos por cada iteración debido a que la cantidad de procesos a evaluar va cambiando.
#Si no se cerrara, estos procesos seguirían activos y ello haría que el rendimiento del programa empeore al tener procesos trabajando en nada.
