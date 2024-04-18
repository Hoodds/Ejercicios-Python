# -*- coding: utf-8 -*-
import random
edadhum = 1
edadper = 1
print("Introduce tu edad")
edadhum=(int)(input())
if (edadhum<3):
    edadper=edadhum*10.5
else:
    edadper=(21+((edadhum-2)*4))
print("Tu edad en edad perruna es ",edadper," años")