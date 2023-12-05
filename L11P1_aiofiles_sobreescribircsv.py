import asyncio
import random
import aiofiles
async def sim_sms():
    tiempo_envio = random.randint(10, 100)
    tiempo_recepcion = random.randint(10, 100)
    latencia = tiempo_envio + tiempo_recepcion
    await asyncio.sleep(latencia/1000)
    print(f"La corrutina de la tecnologia SMS tuvo una latencia de {latencia} ms")
    async with aiofiles.open("latencias_sms.csv", "a") as f:
        linea = "\n"
        linea += str(latencia)
        await f.write(linea)
        
async def sim_3G():
    tiempo_i_v = random.randint(100, 300)
    tiempo_recepcion = random.randint(10, 100)
    latencia = 2*(tiempo_i_v + tiempo_recepcion)
    await asyncio.sleep(latencia/1000)
    print(f"La corrutina de la tecnologia 3G tuvo una latencia de {latencia} ms")
    async with aiofiles.open("latencias_3G.csv", "a") as f:
        linea = "\n"
        linea += str(latencia)
        await f.write(linea)
async def sim_sat():
    reatrdo = random.randint(500, 700)
    tiempo_recepcion = random.randint(10, 100)
    latencia = 2*reatrdo + tiempo_recepcion
    await asyncio.sleep(latencia/1000)
    print(f"La corrutina de la tecnologia 3G tuvo una latencia de {latencia} ms")
    async with aiofiles.open("latencias_satelital.csv", "a") as f:
        linea = "\n"
        linea += str(latencia)
        await f.write(linea)
async def main():
    await asyncio.gather(sim_sms(), sim_3G(), sim_sat())





if __name__ == "__main__":
    asyncio.run(main())
