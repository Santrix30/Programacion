materias=("matematias", "ingles" , "espanol" , "estudios sociales" , "ciencias")

print("hola")
materia= str(input("digite su materia \n "))

busqueda= materia.lower() #para poner todo lo escrito en minuscula
#busqueda= MATERIA.upper() #PARA QUE LO ESCRITO SEA EN MAYUCULA

if busqueda in materias[:]: #[:] HACE UNA BUSQUEDA EN TODA LA LISTA
    print("su materia ya esta en la lista")
else:
    print("su materia no esta")