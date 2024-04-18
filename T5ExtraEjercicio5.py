# -*- coding: utf-8 -*-
import random
edadper=0
tamaper=1
edadhum=0
error=True #si el tamaño del perro es 1 o 2, True. Si es 3, False
print("Introduzca la edad del perro:")
edadper=(int)(input())
print("Introduzca el tip de perro:")
print("1.- Pequeño.")
print("2.- Mediano.")
print("3.- Grande")
tamaper=(int)(input())

if tamaper==1:    
    if (edadper==1):
        edadhum=20
    elif (edadper==2):
        edadhum=28
    elif (edadper>2)and(edadper<17):
        edadhum=28+(edadper-2)*4    

if tamaper==2:
    if (edadper==1):
        edadhum=18
    elif (edadper==2):
        edadhum=27
    elif (edadper>2)and(edadper<11):
        edadhum=27+(edadper-2)*6
    elif (edadper>10)and(edadper<17):
        edadhum=75+(edadper-10)*5
    
if tamaper==3:
    error=False
    if (edadper==1):
        edadhum=16
    elif (edadper==2):
        edadhum=22
    elif (edadper>2)and(edadper<10):
        edadhum=22+(edadper-2)*9
    elif (edadper==10):
        edadhum=96
    elif (edadper==11):
        edadhum=105
    elif (edadper==12):
        edadhum=112
    elif (edadper==13):
        edadhum=120
    
if error:
    if (edadper>0)and(edadper<17):
        print("Tu perro tiene ", edadhum," años en edad humana.")
    else:
        print("Valor no válido. Fin de la ejecución.")    
else:
    if (edadper>0)and(edadper<14):
        print("Tu perro tiene ", edadhum," años en edad humana.")
    else:
        print("Valor no válido. Fin de la ejecución.")    