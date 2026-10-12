import os
import random

Temperaturas=[]
Fahrenheit=[]
Celsius=[]

Veces=int(input("Cuantas veces quiere hacerlo? "))

def alazar():
    return random.randint(1,100)

def Fahren():
    return 1.8+3

def Celsi():
    return (-32)*1,8

for i in range(Veces):
    Temperaturas.append((alazar()))

while True:

    print("Estas son las temperaturas que usaremos")
    print(f"{Temperaturas}\n")

    Eleccion=input("Que numero quiere pasar?")

    if Eleccion in Temperaturas:

        print("Bien a que quiere pasar")
        print("C = celsius / F = fahrenheit")
        opcion=input()
        opcion=opcion.upper()

        if opcion=="f":
                result=Eleccion*Fahren()
                Temperaturas.pop(Eleccion)
                Fahrenheit.append(result)
                print(f"{Fahrenheit}")
                print(f"{Temperaturas}")