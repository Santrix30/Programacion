LISTAPROD=("TOMATE", "AGUACATE", "LIMON", "YUCA", "GUINEO", "LECHUGA", "PEPINO")
LISTAPROD2=[]
DATOS=[1000, 700, 500, 1000, 900, 1500, 1100]
DATOS2=[]


print(" BIENVENIDO A SUPER SHANTI 2 :D \n ")
print(" estos son mis productos :) ")
print(LISTAPROD)

PRODUCTO=input("DIGAME SU PRODUCTO DESEADO \n ")

if PRODUCTO in LISTAPROD:

    print(f"DE ACUERDO YA LE DOY {PRODUCTO} ")

    POSI=LISTAPROD.index(PRODUCTO)
    PRECIOF=DATOS[POSI]

    print(f"ESTE SERIA EL PRECIO {PRECIOF}")
else:
    posicionb=((len(LISTAPROD2)//2))
    LISTAPROD2.insert(posicionb, PRODUCTO)

    print("SU PRODUCTO NO ESTABA PERO LO AÑANDIRE A UNA LISTA NUEVA")

    print("SU PRECIO TAMPOCO ESTABA PERO LO AÑADIRE A UNA LISTADE PRECIOS NUEVOS")

    PREX=input("DIGAME EL PRECIO NUEVO \n ")
    PREX2=list(DATOS2)
    PREX2.insert(0,PREX)
    
    print(f"esto estara en la lista nueva {LISTAPROD2}")
    print(f"este serael precio al que se añadio {PREX2}")