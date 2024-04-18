# -*- coding: utf-8 -*-
import random
lista=[0]*10
for i in range (len(lista)):
    lista[i]=random.randrange(100)
print("Lista original:", lista)

# for i in range (len(lista)): #empieza en cero porque no se le pone inicio.
#     if (lista[i]%2==0):
#         lista.pop(i)
#no se puede usar un for porque al quitar un elemento el array pasa a tener un
#elemento menos y se sale de rango.

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        lista.pop(i)
    else:
        i += 1

print("Lista después de quitar elementos pares:", lista)