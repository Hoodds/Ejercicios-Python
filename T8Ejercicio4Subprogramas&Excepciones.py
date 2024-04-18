# Realizar un programa calculadora. Las operaciones suma, resta, 
# multiplicación y división se realizaran por funciones. Hacer 
# un menú indicando las operaciones disponibles y mediante un 
# input, recoger lo que el usuario quiere operar.
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
try:
    print("CALCULADORA")
    print("Elija una opción:")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    opcion=int(input())
    print("Introduzca el primer número:")
    numero1=float(input())
    print("Introduzca el segundo número:")
    numero2=float(input())
except ValueError:
    print("Dato no válido")

if (opcion==1):
    print("La suma de ",numero1," más ",numero2," es ",suma(numero1,numero2))
if (opcion==2):
    print("La resta de ",numero1," menos ",numero2," es ",resta(numero1,numero2))
if (opcion==3):
    print("La multiplicación de ",numero1," por ",numero2," es ",multiplicacion(numero1,numero2))
if (opcion==4):
    if (numero2==0):
        print("No se puede dividir entre 0")
    else:
        print("La division de ",numero1," entre ",numero2," es ",division(numero1,numero2))