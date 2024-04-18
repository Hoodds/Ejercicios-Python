# -*- coding: utf-8 -*-
import random
nummayores=[0]*10
edadmayores=[0]*10
horamayores=[0]*10
nummenores=[0]*5
edadmenores=[0]*5
horamenores=[0]*5
for i in range(0, 10):
    edadmayores[i]=random.randint(18, 100)
for i in range(0, 5):
    edadmenores[i]=random.randint(6, 17)

for i in range(0, 10):
    nummayores[i]=random.randint(1001, 2000)
for i in range(0, 5):
    nummenores[i]=random.randint(1, 1000)

for i in range(0, 10):
    horamayores[i]=random.choice(["9:30 am","11:00 am"])
for i in range(0, 5):
    horamenores[i]="12:30 am"

for i in range(0, 10):
    print("El corredor ",i+1," tiene ",edadmayores[i]," años, el dorsal ",nummayores[i]," y corre a las ",horamayores[i])
for i in range(0, 5):
    print("El corredor ",i+1," tiene ",edadmenores[i]," años, el dorsal ",nummenores[i]," y corre a las ",horamenores[i])