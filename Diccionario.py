diccionario={"italia":"España" , "japon":"alemania"}
tupla=("ChepeCentro", "Heredia", "mako")
print(diccionario["italia"])
print(diccionario)

diccionario["Juventus"]="italia"
print(diccionario)

diccionario["Juventus"]=34
print(diccionario)

diccionario["Juventus"]="El mostro italiano"
print(diccionario)

diccionario={tupla[0]:"ChepeCentro", tupla[1]:"España", tupla[2]:"alemania"}
print(diccionario)
print(diccionario[tupla[1]])

newdiccionario={"Platos":["hondo", "dulcerita", "extendido", "jarron", "vasos"]}
print(newdiccionario["Platos"])

print(len(diccionario))

print(diccionario.keys())

print(diccionario.values())