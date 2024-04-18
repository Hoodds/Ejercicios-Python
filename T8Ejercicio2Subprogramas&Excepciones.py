# -*- coding: utf-8 -*-
# Realizar un programa que utilice una función para realizar 
# la media de tres números cualesquiera, visualizar el resultado
# en el programa principal. Hacer control de errores.
def media(a,b,c):
    return (a+b+c)/3
num1=0.0
num2=0.0
num3=0.0
print("Introduce el primer número:")
num1=float(input())
print("Introduce el segundo número:")
num2=float(input())
print("Introduce el tercer número:")
num3=float(input())
print(media(num1, num2, num3))

#VERSION TRATANDO EXCEPCIONES

def media(a, b, c):
    try:
        resultado = (a + b + c) / 3
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede calcular la media con divisor igual a cero.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))

    resultado_media = media(num1, num2, num3)

    if resultado_media is not None:
        print(f"La media de {num1}, {num2} y {num3} es: {resultado_media}")

except ValueError:
    print("Error: Introduce valores numéricos válidos.")
except Exception as e:
    print(f"Error inesperado: {e}")
