# -*- coding: utf-8 -*-
lista=["Pera", "Manzana", "Plátano", "Fresa", "Melón", "Piña", "Limón", "Mandarina", "Sandía", "Naranja"]
nombre="xx"
opcion="xx"
print(lista)
lista.sort()
print(lista)
# print("Introduce el nombre de una fruta para ponerlo en mayúsculas.")
# nombre=input()
# print(nombre, " en mayúsculas es ",nombre.upper())
# print("Introduce el nombre de una fruta para ponerlo en minúsculas.")
# nombre=input()
# print(nombre, " en minúsculas es ",nombre.lower())
for i in range(10):
    print("¿Si quiere poner ",lista[i]," en mayúsculas pulse 'M', si lo quiere en minúsculas pulse 'm'")
    opcion=input()
    if (opcion=="M"):
        lista[i]=lista[i].upper()
    elif (opcion=="m"):
        lista[i]=lista[i].lower()
print(lista)    