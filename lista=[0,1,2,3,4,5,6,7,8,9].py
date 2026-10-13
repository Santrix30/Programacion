lista=[0,1,2,3,4,5,6,7,8,9]

import random
 
lista=[1,2,3,4,5,6,7,8,9]
dias=["lunes","martes", "miercoles", "jueves", "viernes"]
meses=["enero", "febrero", "marzo"]
privado=(10,20,30,40)
 
 
print(" recorrer una lista ")
 
def correr(lista):   
    for i in lista:
        print(i)
 
def temperaturas():
    return random.randint(1,40)
 
correr(lista)
print(temperaturas())
correr(dias)
correr(privado)
correr(meses)
print(temperaturas())