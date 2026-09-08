print("Buenas tarde señor/a \n ")
correo= str(input("digite su correo para la verficacion \n "))

simbolo="@"
for i in correo:
    if i== simbolo:
        email=True

    else:
        email=False

if email== True:
    print("correo correcto")
else:
    print("correo incorrecto")



