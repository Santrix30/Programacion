alumnos=["Santiago", "Jose", "mako", "Dylan", "Pepe", "Jefferson"] #lista de alumnos
presentes=[] #lista para presentes
ausentes=[] #lista para ausentes

print("Bueno Voy a pasar asistencia")

for alumno in alumnos: #se crea la variable alumno para que pase 1 a 1 en la lista de alumnos
    asis=input(f"esta presente {alumno} ? 1-SI / 2-NO \n ")

    if asis == "2":
        print("Perfecto va a ausentes")
        ausentes.append(alumno) #se agrega en ausentes
    elif asis == "1": 
        print("Sigamos con el resto")
        presentes.append(alumno) #se agrega en presentes

print("ESTAS SON LAS LISTAS") #por ultimo se imprime las dos listas
print("Ausentes:")
print(ausentes)
print("Presentes:")
print(presentes)








