#si tenemos un arreglo escrito code=("1,2,3,4"), podemos transformarlo a un arreglo
arr= code.split(",")



  
#transformar de caracter a numero 
t = "1,2,3,4,5"
t = t.split(",")
#t
#['1', '2', '3', '4', '5']
números = map(int, t)
#números
#[1, 2, 3, 4, 5]



  
#uso de * en listas(uso en *tasks de asyncio)
t="1,2,3,4,5"
t=t.split(",")
#t
#['1', '2', '3', '4', '5']
l=[1,2,3,4]
m=(*t,*l) 
#m
#('1', '2', '3', '4', '5', 1, 2, 3, 4)



  





  
#Uso de memory_profiler

  from memory_profiler import profile

@profile
def main_func():
    import random
    arr1 = [random.randint(1,10) for i in range(100000)]
    arr2 = [random.randint(1,10) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    tot = sum(arr3)
    print(tot)

if __name__ == "__main__":
    main_func()

#ejecutando memory_profiler
python(3) -m memory_profiler my_code.py
