# -*- coding: utf-8 -*-
import random
texto1="Bilbo Frodo Sam Aragorn y Gandalf"
texto2="Bilbo Frodo Sam Aragorn y Gandalf"
texto3="Porthos Aramis Athos y Dartagnan"
texto4="Luke Leia Han Obi-Wan y Anakin"
texto5="Luke Leia Han Obi-Wan y Anakin"
nombre="Lander"
esta=False

print("Tenemos 5 textos con tres listas de nombres, algunos son de Star Wars, otros de El Señor de los Anillos y otro con los nombres de los Mosqueteros")
print("Introduce un nombre para comprobar si esta en el texto que se ha escogido aleatoriamente:")
nombre=input()
listadeltextoelegido=(random.choice([texto1,texto2,texto3,texto4,texto5])).split()
for i in range (len(listadeltextoelegido)):
    if (nombre==listadeltextoelegido[i]):
        esta=True
if (esta==True):
    print("El nombre elegido, "+nombre+", está en el texto. Enhorabuena.")
else:
    print("El nombre elegido, "+nombre+", no está en el texto.")
#falta la repetitiva si se quiere seguir o no.