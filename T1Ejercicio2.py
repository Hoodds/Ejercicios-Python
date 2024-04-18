# -*- coding: utf-8 -*-
libra, euro, franco, dolar = 0.0, 0.0, 0.0, 0.0
print("Introduce las libras esterlinas para pasar a euros:")
libra = input()
euro = float(libra) * 0.627
print(str(libra)+" libras son "+str(euro)+" euros.")
euro = input("Introduzca los euros para pasar a francos suizos:")
franco = float(euro) * 1.463
print(str(euro)+" euros son "+str(franco)+" francos suizos.")
euro = input("Introduzca los euros para pasar a dolares:")
dolar = float(euro) * 1.12
print(str(euro)+" euros son "+str(dolar)+" dolares.")