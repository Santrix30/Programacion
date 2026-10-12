import os
import random

Temperaturas=[]
Fahrenheit=[]
Celsius=[]

Veces=int(input("Cuantas veces quiere hacerlo? "))

def alazar():
    return random.randint(1,100)

def Fahren():
    return (1.8+3)

def Celsi():
    return (Eleccion-32)*1,8


for i in range(Veces):
    Temperaturas.append((alazar()))

while True:

    print("Estas son las temperaturas que usaremos")
    print(f"{Temperaturas}\n")
    print("Si se queda sin temperaturas, presione -1 para salir \n" )

    Eleccion=int(input("Que numero quiere pasar? "))

    if Eleccion==-1:
        print("Gracias, adios \n")
        break

    if Eleccion in Temperaturas:

        print("Bien a que quiere pasar")
        print("C = celsius / F = fahrenheit")
        opcion=input()
        opcion=opcion.upper()

        if opcion=="F":
            result=Eleccion*Fahren()
            Temperaturas.remove(Eleccion)
            Fahrenheit.append(result)
            print("Ahora es temperatura la pasamos a otra lista")
            print(f"{Fahrenheit}")
            print("Y la quitamos de las temperaturas\n")
            print(f"{Temperaturas}")
            os.system("pause")
            os.system("cls")

        if opcion=="C":
            result=Celsi()
            Temperaturas.remove(Eleccion)
            Celsius.append(result)
            print("Ahora es temperatura la pasamos a otra lista")
            print(f"{Celsius}")
            print("Y la quitamos de las temperaturas\n")
            print(f"{Temperaturas}")
            os.system("pause")
            os.system("cls")


print("Al final quedo asi")
print(f"Temperaturas dadas {Temperaturas}")
print(f"Estas son las temperaturas Celsius {Celsius}")
print(f"Estas son las temperaturas Fahrenheit {Fahrenheit}")
os.system("pause")
os.system("cls")