alumnos10_3=["TAMARA", "MATIAS", "ALLISON", "DARIO", 40] # con el * se puede multiplicar la lista
alumnos10_4=[1,2,3,4,5,6]
print(alumnos10_3) #ESTO ES PARA MOSTRAR TODAS LA LISTA
print(alumnos10_4)

print("ahora se va a ver algo especifico" )
print(alumnos10_3[1]) #el [ ] es para en una lista mostrar el campo especifico
print(alumnos10_3[-1]) #si es de atras para adelante empieza en -1 , -2 ...
print(alumnos10_3[0:3]) #para traer una lista deseada, pero se le quita 1 / o tambie se abrevia como :3 y funcioa igual

alumnos10_3.append("derek") #agrega un dato a la ultima posicion
print(alumnos10_3)

alumnos10_3.insert(2, "miguel") #agregar a una posicion especifica
print(alumnos10_3)

alumnos10_3.extend(["dylan", "valeska", "Jose"]) #agregar varios datos a la lista, pero se agregan de ultimo
print(alumnos10_3)

#print(alumnos10_3.index("dylan")) 
#index es para ver una posicion de un valor en una lista exacta
posicion=(alumnos10_3.index("dylan"))

alumnos10_3.insert(posicion, "daniel") 
print(alumnos10_3) 

print("dylan" in alumnos10_3) #ver si ese dato esta en la lista
print("ronald" in alumnos10_3) #sino esta sale false ya que no esta

alumnos10_3.remove("miguel") #quitar algun valor de la lista
print(alumnos10_3)

alumnos10_3.pop() #borra al ultimo 
print(alumnos10_3)

alumnos10_3.pop(2) #borra una posicion / tambien se puede borrar sin saber la posicion
print(alumnos10_3)


print(len(alumnos10_3)) #nos da la cantidad de datos no las posiciones

print(alumnos10_3.sort()) # se usa para ordenar alfabeticamente

