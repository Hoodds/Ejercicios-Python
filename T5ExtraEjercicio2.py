# -*- coding: utf-8 -*-
import random
pregunta=""
#print("Introduzca su pregunta: (SALIR para finalizar)")
#pregunta=input()
while (pregunta != "SALIR"):
    print("Introduzca su pregunta: (SALIR para finalizar)")
    pregunta=input()
    if (pregunta!="SALIR"):
        print(random.choice(["Sí", "No", "Puede ser", "No en esta vida", "Igual", "Claro que sí guapi", "Fijo"]))