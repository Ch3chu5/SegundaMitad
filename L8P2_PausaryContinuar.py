

import asyncio
import psutil

pausa = asyncio.Event()  # Crear un evento que permite pausar y reanudar

async def monitorizar_recursos():
    while True:
        await pausa.wait()  
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        print(f"Uso de CPU: {cpu}% | Uso de memoria: {mem.percent}%")
        await asyncio.sleep(2)

async def main():
    print("Monitorización de recursos del sistema")
    print("Presione 'p' para pausar o reanudar la monitorización")
    
    # Se crea la tarea para que se pueda ingresar datos por el terminal (p, para pausar o reanudar la tarea)
    # Probe llamando la funcion por medio de await monitorizar_recursos() y no me dejaba ingresar datos por el terminal
    monitorizacion_task = asyncio.create_task(monitorizar_recursos())

    try:
        entrada = "q" #Inicio la variable entrada en un valor distinto de p para que en el if se vaya a la opcion de monitoreo de datos al ejecutar el codigo
        while True:
            if entrada.strip() == "p":
                pausa.clear()  #Se pausa el monitoreo
                print("Monitorización pausada. Presione 'p' para reanudar")
            else:
                pausa.set()  #Se reanuda el monitoreo
                print("Monitorizando datos. Presione 'p' para pausar")
            entrada = await asyncio.to_thread(input) #Cada que termina una iteracion, se espera un valor a ingresar; de no ingresarse nada, se sigue monitoreando
            if entrada.strip() != "p":
                print("SOLO ingrese 'p' si quiere pausar el programa, no ingrese otros valores")  
    except:   #No pongo KeyboardInterrupt porque cuando presiona Ctrl+C sale un error mas grande en el terminal
        print("La monitorización ha sido detenida")

if __name__ == "__main__":
    asyncio.run(main())
