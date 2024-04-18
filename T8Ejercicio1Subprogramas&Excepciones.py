# -*- coding: utf-8 -*-
# Diseñar un programa que cree una función para realizar la división 
# de dos números enteros, comprobar que sean enteros antes de operar 
# con ellos, y obtener el cociente. Hacer varias llamadas a esa función 
# desde el programa principal.
numero1=0
numero2=0
def division(num1, num2):
    cociente=0
    try:
        cociente=num1//num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
    return cociente
print("Introduce el primer número:")
numero1=float(input())
while numero1%1!=0:
    print("Número no válido. Introduce un valor entero:")
    numero1=float(input())
print("Introduce el segundo número:")
numero2=float(input())
while numero2%1!=0:
    print("Número no válido. Introduce un valor entero:")
    numero2=float(input())

print("El cociente resultante de dividir ",int(numero1)," entre ",int(numero2)," es ",int(division(numero1, numero2)))

#PRINTEA EL RESULTADO AUNQUE ENTRE EN LA EXCEPCION.
#VERSION CORREGIDA
# -*- coding: utf-8 -*-

numero1 = 0
numero2 = 0

def division(num1, num2):
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    else:
        return num1 // num2

print("Introduce el primer número:")
numero1 = float(input())

while numero1 % 1 != 0:
    print("Número no válido. Introduce un valor entero:")
    numero1 = float(input())

print("Introduce el segundo número:")
numero2 = float(input())

while numero2 % 1 != 0:
    print("Número no válido. Introduce un valor entero:")
    numero2 = float(input())

resultado = division(numero1, numero2)

if resultado is not None:
    print("El cociente resultante de dividir", int(numero1), "entre", int(numero2), "es", int(resultado))
