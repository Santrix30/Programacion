print("Digite sus dos digitos")
num=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))
SUM1= num+num2
resultadof=0
rango= 10

for i in range(rango):
    print(f"ESTA ES LA VEZ {i}")
    print(f"Esta es la suma que llevo {SUM1}")
    resultadof= resultadof+SUM1

print(f"despues de las 10 veces esta es la suma ={resultadof}")