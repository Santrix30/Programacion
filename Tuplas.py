print("TUPLAS!")

price=(1000, 2000, 5000, 10000, 20000)
art=("camisa", "pantalon", "saco", "vestido")

print(price)
print(price[2])

preciolis=list(price) #list es para pasar de tupla a lista
preciolis.insert(2, 34200)

print(preciolis)

price=tuple(preciolis) #la tupla es para actualizar la lista que se le da por la otra actualizada (el contraio de list)

print(price)
print(f"La tupla actualizada contiene estos valores: {price}") #f de formato

validar=(20000 in price) #verificar si hay un valor en la tupla
print(validar)

print(price.count(20000))#ver cuantas veces se repite un valor en una tupla o tambien en lista str

print(f"la tupla contiene la cantidad de elementos que tiene {len(price)}") #contar la  cantidad de datos

datos=(18, "diciembre", 100000)#forma de desemapquetar la tupla / poder usar los datos de mejor manera
edad,ms,salario=datos 

print(f"la edad de la persona es {edad}")
print(f"el mes de cumpleaños es {ms}")
print(f"el salario es {salario}")