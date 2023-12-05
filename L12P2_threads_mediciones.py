import time
from threading import Thread
import matplotlib.pyplot as plt
import statistics
def descargar_archivo(link):
    from urllib.request import urlopen
    url = link
    with urlopen(url) as page:
        image_data = page.read()

#iterar esta lista
#url = f'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{n}.png' for n in range 1,29 (no olvidar usar str en estos casos)
url_lst = ["https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/01.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/02.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/03.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/04.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/05.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/06.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/07.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/08.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/09.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/10.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/11.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/12.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/13.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/14.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/15.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/16.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/17.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/18.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/19.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/20.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/21.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/22.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/23.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/24.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/25.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/26.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/27.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/28.png",
           "https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/29.png"]
def descargar_grupo(url_lst, lista):
    for item in (lista):
        descargar_archivo(url_lst[item])
if __name__ == "__main__":
    #Parte a:#####################################
    time_a = []
    for i in range(5):
        tic = time.perf_counter()
        for item in url_lst:
            descargar_archivo(item)
        toc = time.perf_counter()
        t_sync = toc - tic
        #print(f"Tiempo de ejecucion sincrono: {toc-tic}")
        time_a.append(t_sync*1e3)
    print("Mediana ejecucion sincrona: ", statistics.median(time_a), "ms")
    plt.plot(time_a)
    plt.ylabel("Tiempo de ejecucion [ms]")
    plt.savefig("ParteA.png")
    plt.cla()
    #Parte b:####################################
    time_b = []
    for i in range(5):
        tic2 = time.perf_counter()
        
        im1 = Thread(target=descargar_archivo(url_lst[0]))
        im2 = Thread(target=descargar_archivo(url_lst[1]))
        im3 = Thread(target=descargar_archivo(url_lst[2]))
        im4 = Thread(target=descargar_archivo(url_lst[3]))
        im5 = Thread(target=descargar_archivo(url_lst[4]))
        im6 = Thread(target=descargar_archivo(url_lst[5]))
        im7 = Thread(target=descargar_archivo(url_lst[6]))
        im8 = Thread(target=descargar_archivo(url_lst[7]))
        im9 = Thread(target=descargar_archivo(url_lst[8]))
        im10 = Thread(target=descargar_archivo(url_lst[9]))
        im11 = Thread(target=descargar_archivo(url_lst[10]))
        im12 = Thread(target=descargar_archivo(url_lst[11]))
        im13 = Thread(target=descargar_archivo(url_lst[12]))
        im14 = Thread(target=descargar_archivo(url_lst[13]))
        im15 = Thread(target=descargar_archivo(url_lst[14]))
        im16 = Thread(target=descargar_archivo(url_lst[15]))
        im17 = Thread(target=descargar_archivo(url_lst[16]))
        im18 = Thread(target=descargar_archivo(url_lst[17]))
        im19 = Thread(target=descargar_archivo(url_lst[18]))
        im20 = Thread(target=descargar_archivo(url_lst[19]))
        im21 = Thread(target=descargar_archivo(url_lst[20]))
        im22 = Thread(target=descargar_archivo(url_lst[21]))
        im23 = Thread(target=descargar_archivo(url_lst[22]))
        im24 = Thread(target=descargar_archivo(url_lst[23]))
        im25 = Thread(target=descargar_archivo(url_lst[24]))
        im26 = Thread(target=descargar_archivo(url_lst[25]))
        im27 = Thread(target=descargar_archivo(url_lst[26]))
        im28 = Thread(target=descargar_archivo(url_lst[27]))
        im29 = Thread(target=descargar_archivo(url_lst[28]))
        
        toc2 = time.perf_counter()
        t_async = toc2 - tic2
        #print("Tiempo de ejecucion 29 hilos: ",t_async)
        time_b.append(t_async*1e3)
    
    print("Mediana ejecucion 29 hilos: ", statistics.median(time_b), "ms")
    plt.plot(time_b)
    plt.ylabel("Tiempo de ejecucion [ms]")
    plt.savefig("ParteB.png")
    plt.cla()
    #Parte C: Para esta parte, por cada thread que use, se dividira el total de imagenes en 3 y cada hilo va a descargar secuencialmente los grupos que obtenga
    time_c = []
    for i in range(5):
        tic3 = time.perf_counter()
        lst1 = [n for n in range(10)]
        lst2 = [(n+10) for n in range(10)]
        lst3 = [(n+20) for n in range(9)]
        th1 = Thread(target = descargar_grupo(url_lst, lst1))
        th2 = Thread(target = descargar_grupo(url_lst, lst2))
        th3 = Thread(target = descargar_grupo(url_lst, lst3))
        toc3 = time.perf_counter()
        t_async_g = toc3 - tic3
        #print("Tiempo de ejecucion 3 hilos: ",t_async_g)
        time_c.append(t_async_g*1e3)

    print("Mediana ejecucion 3 hilos: ", statistics.median(time_c), "ms")
    plt.plot(time_c)
    plt.ylabel("Tiempo de ejecucion [ms]")
    plt.savefig("ParteC.png")
    plt.cla()
