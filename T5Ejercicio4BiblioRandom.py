# -*- coding: utf-8 -*-
import random
num=round(random.uniform(0.0, 2.0), 2)
euro = 0.0
dolar = 0.0
print("Introduzca la cantidad de Euros para pasar a Dólares:")
euro=input()
print("1 Euro equivale a ",num," Dólares")
dolar=num*int(euro)
print("Sus ",euro," Euros equivalen a ",dolar," Dólares.")