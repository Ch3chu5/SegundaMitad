import aiofiles
import asyncio
import matplotlib.pyplot as plt
import time


def generar_archivos(M,N):

    # M archivos -> 1:M+1
    for i in range(1,M+1):
        
        with open(f"./original/archivo{i}.txt","w") as write:
            write.write("."*N)



#copiar archivos de manera sincrona
def copiar_arch_sin(M,N):
    for i in range(1,M+1):
        #leemos la carpeta original y copiamos
        with open(f'./original/archivo{i}.txt','r') as read:
            content=read.read()

        with open(f'./copia/archivo{i}.txt','w') as write:
            write.write(content)

async def copiar_arch_a(M,N):
    for i in range(1,M+1):
        async with aiofiles.open(f"./original/archivo{i}.txt","r") as read:
            copiado = await read.read()

        async with aiofiles.open(f"./copia_a/archivo{i}.txt","w") as write:
            await write.write(copiado) 



if __name__ == '__main__':
    generar_archivos(3,1024)
    copiar_arch_sin(3,1024)
    asyncio.run(copiar_arch_a(3,1024))

    lista_N = [2**i for i in range(10,26)]
    tiempos_sync = []
    tiempos_async = []

    # Inserte aqui el codigo que haga falta
    for N in lista_N:
        tic1=time.perf_counter()
        copiar_arch_sin(3,N)
        tic2=time.perf_counter()
        asyncio.run(copiar_arch_a(3,N))
        tic3=time.perf_counter()

        tiempo_medido_1=tic2-tic1
        tiempo_medido_2=tic3-tic2
        tiempos_sync.append(tiempo_medido_1)
        tiempos_async.append(tiempo_medido_2)

    N_new=2**20
    lista_M = [i for i in range(2,11)]
    tiempos_sync_M = []
    tiempos_async_M = []

    for M in lista_M:
        tic4=time.perf_counter()
        copiar_arch_sin(M,N_new)
        tic5=time.perf_counter()
        asyncio.run(copiar_arch_a(M,N_new))
        tic6=time.perf_counter()

        tiempo_medido_M1=tic5-tic4
        tiempo_medido_M2=tic6-tic5
        tiempos_sync_M.append(tiempo_medido_M1)
        tiempos_async_M.append(tiempo_medido_M2)

plt.plot(lista_N,tiempos_sync)
plt.plot(lista_N,tiempos_async)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync','Async'])
plt.savefig('SizeVsTime.png')
plt.cla()

#Despues de ejecutar varias veces la función y observar el gráfico, llegué a la conclusión:

#Cuando aumenta el tamaño archivos, segun la grafica llega un punto donde es mejor hacer la ejecución de forma asincrona 
#en un principio la funcion sincrona toma menos tiempo, pero con el aumento de archivos se puede ver que la funcion asincrona
#es más rápida, caso contrario con la sincrona. 

plt.plot(lista_M,tiempos_sync_M)
plt.plot(lista_M,tiempos_async_M)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync','Async'])
plt.savefig('SizeVsTime_M.png')
plt.cla()

#Cuando aumentamos el numero de archivos por otro lado segun la gráfica se ve que es mejor usar la función sincrona,
#esto puede deberse al consumo de memoria que requiere usar un funcion asincrona para un numero de archivos grandes
