diccionario={"Juventus":"España" , "japon":"alemania"}

pais=(diccionario.get("Juventus"))

print(f"El pais donde juega la juventus es {pais}")

diccionario.pop("Juventus")
print(diccionario)

copdicc=diccionario.copy()
print(copdicc)

diccionario.clear()
print(diccionario)

