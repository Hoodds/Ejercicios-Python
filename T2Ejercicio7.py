# -*- coding: utf-8 -*-
esprimo=True
num=input("Introduce un número: ")
i=2
while i<int(num):
    if (int(num)%int(i)==0):
        esprimo=False
    i+=1
if esprimo==True:
    print("El número es primo.")
else:
    print("El número no es primo.")