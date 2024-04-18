# -*- coding: utf-8 -*-
suma=0
for i in range(1, 6):
    edad=input("Introduce la edad del niño número "+str(i)+": ")
    suma=suma+int(edad)
media=0
media=suma/5
print("La media de edad de los 5 niños es "+str(media))