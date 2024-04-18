# -*- coding: utf-8 -*-
a, b, c = 1, 1, 1
a = input("Introduzca el valor de a: ")
b = input("Introduzca el valor de b: ")
c = input("Introduzca el valor de c: ")
if a<b and a<c:
    print("a es el menor")
elif b<c:
    print("b es el menor")
else:
    print("c es el menor")