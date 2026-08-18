LISTAPROD=["TOMATE", "AGUACATE", "LIMON", "YUCA", "GUINEO", "LECHUGA", "PEPINO"]
print("HOLA BIENVENIDO A SUPER SHANTI")
print(" shanti: estos son mis productos :) ")
print(LISTAPROD)
PRODUCTO=input("DIGAME SU PRODUCTO DESEADO \n ")


if PRODUCTO in LISTAPROD:
    print("DE ACUERDO, YA SE LO DOY")
else:
    posicionb=((len(LISTAPROD)//2))
   
    #POSICIONPRO=(LISTAPROD.index("YUCA"))
    LISTAPROD.insert(posicionb, PRODUCTO)
    print("su producto no estaba pero lo pondre :) ")
    print(LISTAPROD)
