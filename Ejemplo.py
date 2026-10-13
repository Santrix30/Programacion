import os
import random

lista=[1,2,3,4,5,6,7,8,9]
dias=["lunes","martes", "miercoles", "jueves", "viernes"]
meses=["enero", "febrero", "marzo"]
privado=(10,20,30,40)

def correr(lista):
    i=0
    while i<len(lista):
        print(lista[i])
        i=i+1

correr(lista)
correr(dias)
correr(meses)
correr(privado)

os.system("pause")
os.system("cls")

