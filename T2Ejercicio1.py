# -*- coding: utf-8 -*-
saldo = input("Introduce el saldo:")
retirada = input("Introduce el importe que desea retirar:")
if retirada>saldo:
    print("Lo siento, saldo insuficiente.")
    print("Saldo: "+saldo)
else:    
    saldo=int(saldo)-int(retirada)
    print("Retirada: "+str(retirada))
    print("Nuevo saldo: "+str(saldo))