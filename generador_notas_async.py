import aiofiles
import asyncio
import random
import time

async def genera_labs():
    codigo_inicial = 20230001

    async with aiofiles.open("notas_labs.csv", "w+") as f:
        cabecera = "codigo,"
        cabecera += ",".join([f"lab_{i}" for i in range(1, 15)])
        cabecera += "\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},"
            linea += ",".join([f"{random.randint(0, 20)}" for i in range(1, 15)])
            linea += "\n"
            await f.write(linea)


async def genera_parcial():
    codigo_inicial = 20230001

    async with aiofiles.open("notas_parcial.csv", "w+") as f:
        cabecera = "codigo,parcial\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def genera_final():
    codigo_inicial = 20230001

    async with aiofiles.open("notas_final.csv", "w+") as f:
        cabecera = "codigo,final\n"
        await f.write(cabecera)
        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def main():
    await asyncio.gather(genera_labs(), genera_parcial(), genera_final())


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")
