# -*- coding: utf-8 -*-
texto=""
palabra=""
palabranueva=""
textomodificado=""
print("Introduzca un texto:")
texto=input()
print("Ahora cambiemos una palabra del texto por otra, elija la palabra que quiera cambiar:")
palabra=input()
print("Elija la nueva palabra:")
palabranueva=input()
print("El texto original es: ", texto)
print("El nuevo texto es: ", (texto.replace(palabra, palabranueva)))