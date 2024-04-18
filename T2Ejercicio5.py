# -*- coding: utf-8 -*-
num=input("Introduce un número para mostrar su tabla de multiplicar:")
for i in range(1, 11):
    print(num+" * "+str(i)+" = "+str(int(num)*int(i)))