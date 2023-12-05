import time
import requests
from concurrent.futures import ThreadPoolExecutor
import statistics

def obtener_html_threaded(workers, urls):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for i in range(len(urls)):
            executor.submit(crear_html, urls[i], i)

def obtener_html_secuencial(urls):
    for i in range(len(urls)):
        crear_html(urls[i], i)
        
def crear_html(url, i):
        response = requests.get(url)
        if response.status_code == 200:
            nombre = "pagina"+str(i+1)+".html"
            with open(f"{nombre}", "w", encoding="utf-8") as f:
                a = response.text
                f.write(a)
if __name__ == "__main__":
    urls = [
            "https://www.wikipedia.org/",
            "https://www.nytimes.com/",
            "https://www.bbc.com/",
            "https://www.python.org/",
            "https://www.reddit.com/",
            "https://www.instagram.com/",
            "https://www.twitter.com/",
            "https://www.cnn.com/",
            "https://www.github.com/",
            "https://www.spotify.com/",
            ]
    tiempo_s = []
    tiempo_th = []
    tiempo_th_sl = []
    tiempo_th_f = []
    tiempo_th_f2 = []
    for i in range(5):
        tic = time.perf_counter()
        obtener_html_secuencial(urls)
        toc = time.perf_counter()
        obtener_html_threaded(3, urls)
        toc2 = time.perf_counter()
        obtener_html_threaded(4, urls)
        toc3 = time.perf_counter()
        obtener_html_threaded(5, urls)
        toc4 = time.perf_counter()
        obtener_html_threaded(10, urls)
        toc5 = time.perf_counter()
        tiempo_s.append(toc-tic)
        tiempo_th.append(toc2-toc)
        tiempo_th_sl.append(toc3-toc2)
        tiempo_th_f.append(toc4-toc3)
        tiempo_th_f2.append(toc5-toc4)
    print("Tiempo mediano secuencial: ", statistics.mean(tiempo_s), "s")
    print("Tiempo mediano threaded 3 trabajadores: ", statistics.mean(tiempo_th),"s")
    print("SpeedUp", (statistics.mean(tiempo_s)/statistics.mean(tiempo_th)))
    print("----------------------------------------------")
    print("Tiempo mediano threaded 4 trabajadores: ", statistics.mean(tiempo_th_sl),"s")
    print("Tiempo mediano threaded 5 trabajadores: ", statistics.mean(tiempo_th_f),"s")
    print("Tiempo mediano threaded 10 trabajadores: ", statistics.mean(tiempo_th_f2),"s")
    #Cabe comentar que los aarchivos html creados no contienen los estilos (CSS creo) de las paaginas; no tengo ideaa por que se da eso pero en algunas de estos archivos se daba ese problema
