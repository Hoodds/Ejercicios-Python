# -*- coding: utf-8 -*-
import random
num1=random.randint(1, 100)
num2=random.randint(1, 100)
if (num1%num2==0):
    print(num1," es multiplo de ",num2)
elif (num2%num1==0):
    print(num2," es multiplo de ",num1)
else:
    print("Los números ",num1," y ",num2," no son múltiplos uno de otro")