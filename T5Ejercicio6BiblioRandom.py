# -*- coding: utf-8 -*-
# Aquellos años que son divisibles entre 4, pero no entre 100, son bisiestos. 
# Los años que son divisibles entre 100, pero no entre 400, no son bisiestos.
import random
num=random.randint(1, 2024)
if (num%4==0) and (num%100!=0):
    print(num," es bisiesto.")
else:
    print(num," no es bisiesto.")