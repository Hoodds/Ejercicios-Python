# -*- coding: utf-8 -*-
num = input("Introduce un numero:") #lo coge como string no se pueden hacer operaciones aritmeticas
print("Cuadrado="+str(int(num)*int(num))) #para concatenar hay que pasar a string
print("Doble="+str(int(num)*2))
print("Triple="+str(int(num)*3))
print("Cubo="+str(int(num)**3))

num=int(num)
print("Cuadrado=", num*num)