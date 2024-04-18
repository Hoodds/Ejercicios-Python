# -*- coding: utf-8 -*-
import random
num=random.randint(20, 60)
uni=0
print(num)
if (num==20):
    print("Veinte")
    uni=0
elif (num>20)and(num<30):
    print("Veinti", end="") # , end="") hace que el print no salte de linea
    uni=num-20
    if (uni==0):
        print("")
    elif (uni==1):
        print("uno")
    elif (uni==2):
        print("dos")
    elif (uni==3):
        print("tres")
    elif (uni==4):
        print("cuatro")
    elif (uni==5):
        print("cinco")
    elif (uni==6):
        print("seis")
    elif (uni==7):
        print("siete")
    elif (uni==8):
        print("ocho")
    elif (uni==9):
        print("nueve")
    uni=0    
elif (num>=30)and(num<40):
    print("Treinta", end="") # , end="") hace que el print no salte de linea
    uni=num-30
elif (num>=40)and(num<50):
    print("Cuarenta", end="") # , end="") hace que el print no salte de linea
    uni=num-40
elif (num>=50)and(num<60):
    print("Cincuenta", end="") # , end="") hace que el print no salte de linea
    uni=num-50
else:
    print("Sesenta")
    uni=0
if (uni==0):
    print("")
elif (uni==1):
    print(" y uno")
elif (uni==2):
    print(" y dos")
elif (uni==3):
    print(" y tres")
elif (uni==4):
    print(" y cuatro")
elif (uni==5):
    print(" y cinco")
elif (uni==6):
    print(" y seis")
elif (uni==7):
    print(" y siete")
elif (uni==8):
    print(" y ocho")
elif (uni==9):
    print(" y nueve")