# -*- coding: utf-8 -*-
array=[0]*10
num=0
for i in range(0, 10):
    print("Introduce un número para la posición ",(i+1)," del array:")
    num=input()
    array[i]=int(num)
print(array)
array.sort()
array.reverse()
print(array)