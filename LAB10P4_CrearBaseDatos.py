import random

if __name__ == "__main__":
    contenido = "paciente, edad, estado: \n"
    paciente_p=1
    for i in range(10):
        pacientes= f"{paciente_p+i}"
        edad=random.randint(5,60)
        estado=random.randint(0,1)
        for _ in range(1):
           pacientes += f"{edad},{estado},"
        contenido += f"{pacientes[:-1]}\n"

    with open("base_datos.csv","w", encoding= "utf-8") as f:
        
        f.write(contenido)
