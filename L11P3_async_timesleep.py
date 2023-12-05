import asyncio
import time
async def dia1(valores):
    valores[0][1]+=1
    valores[4][1]+=1
    valores[1][1]+=1
    await asyncio.sleep(0.15)
async def dia2(valores):
    valores[0][1]+=1
    valores[2][1]+=1
    valores[3][1]+=1
    await asyncio.sleep(0.15)
async def dia3(valores):
    valores[0][1]+=1
    valores[2][1]+=1
    valores[1][1]+=1
    await asyncio.sleep(0.15)
async def dia4(valores):
    valores[0][1]+=1
    valores[1][1]+=1
    valores[2][1]+=1
    await asyncio.sleep(0.15)
async def dia5(valores):
    valores[0][1]+=1
    valores[1][1]+=1
    valores[3][1]+=1
    await asyncio.sleep(0.15)

    
async def fase_rondas_async(valores):
    await asyncio.gather(dia1(valores))
    await asyncio.gather(dia2(valores))
    await asyncio.gather(dia3(valores))
    await asyncio.gather(dia4(valores))
    await asyncio.gather(dia5(valores))
    for i in range(5):
        ganador = 0
        if int(valores[i][1]) > int(valores[ganador][1]):
            ganador = i
    msg = f"El ganador es {valores[ganador][0]}, con un puntaje de {valores[ganador][1]}"
    return msg
def fase_rondas_sync(valores):
    for i in range(5):
        valores[0][1] += 1
        time.sleep(0.15)
    for i in range(4):
        valores[1][1] += 1
        time.sleep(0.15)
    for i in range(3):
        valores[2][1] += 1
        time.sleep(0.15)
    for i in range(2):
        valores[3][1] += 1
        time.sleep(0.15)
    valores[4][1] += 1
    time.sleep(0.15)      
    for i in range(5):
        ganador = 0
        if int(valores[i][1]) > int(valores[ganador][1]):
            ganador = i
    msg = f"El ganador es {valores[ganador][0]}, con un puntaje de {valores[ganador][1]}"
    return msg


if __name__ == "__main__":
    ##Leyendo el contenido de players.csv
    with open("players.csv", "r", encoding="utf-8") as f:
        contenido = f.read()
    contenido_l = contenido.split("\n")
    contenido_l = contenido_l[1:]  #de esta manera, me queda una lista con los jugadores y sus puntajes respectivos
    c_s_l = []
    for linea in contenido_l:
        datos = linea.split(";")
        if len(datos) >= 2:
            nombre = datos[0]
            puntaje = int(datos[1]) 
            c_s_l.append([nombre, puntaje])

    a = fase_rondas_sync(c_s_l)
    print(a)
    b = asyncio.run(fase_rondas_async(c_s_l))
    print(b)
    print("Observacion, en ambos casos Magnus gana, pero en el segundo tiene un mayor puntaje; esto debido a que la 'base de datos' se actualiza debido a la ejecucion del programa. Esto no afecta al resultado final porque, debido a la logica del programa, Magnus siempre iba a ganar esta ronda. Con un poco mas de tiempo, tal vez podria haber sido solucionado este problema pero no tiene sentido; porque en un torneo real, luego de una ronda quieres que los datos de actualicen (eso creo)")
