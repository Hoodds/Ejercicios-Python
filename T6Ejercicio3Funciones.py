# -*- coding: utf-8 -*-
nombres=[""]*5
notas=[0.0]*5
for i in range(0, 5):
    print("Introduce el nombre del alumno ",i+1)
    nombres[i]=input()
    print("Introduce nota del alumno ",i+1)
    notas[i]=input()    
print("La nota más alta de clase es ",max(notas))
print("La nota más baja de clase es ",min(notas))
print("La nota media de clase es ",(sum(notas)/5))
#no funciona la media ni el numero mayor