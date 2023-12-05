import random
import time
from multiprocessing import Process
def calculo_pi_serial(n):
    dentro = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        circulo = x**2 + y**2
        if circulo < 1:
            dentro += 1
    pi = 4*dentro/n
    return pi
def calculo_pi_paralelo(n, res):
    dentro = 0
    for i in range(int(n/4)):
        x = random.uniform(-0.25, 0.25)
        y = random.uniform(-0.25, 0.25)
        circulo = x**2 + y**2
        if circulo < 0.0626:
            dentro += 1
    res[0] = 4*dentro/n
    

N = 10000000
if __name__ == "__main__":
    tic = time.perf_counter()
    pi_serial = calculo_pi_serial(N)
    toc = time.perf_counter()
    time_serial = toc - tic
    res0 = [0]
    res1 = [0]
    res2 = [0]
    res3 = [0]
    tic_paralelo = time.perf_counter()
    p1 = Process(target=calculo_pi_paralelo(N, res0))
    p2 = Process(target=calculo_pi_paralelo(N, res1))
    p3 = Process(target=calculo_pi_paralelo(N, res2))
    p4 = Process(target=calculo_pi_paralelo(N, res3))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    pi_paralelo = res0[0] + res1[0] + res2[0] + res3[0]
    toc_paralelo = time.perf_counter()
    time_paralelo = toc_paralelo - tic_paralelo
    print(f"El valor calculado de pi es: {pi_serial}")
    print(f"El tiempo serial del calculo de pi es: {time_serial}")
    print(f"El valor calculado mediante paralelizacion de pi es: {pi_paralelo} segundos")
    print(f"El tiempo paralelo del calculo de pi es: {time_paralelo} segundos")
