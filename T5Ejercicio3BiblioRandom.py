# -*- coding: utf-8 -*-
import random
#num=random.randint(1, 400)
num=3930
horas=num//3600
restohoras=num%3600
minutos=restohoras//60
restominutos=restohoras%60
segundos=restominutos
print(num," segundos, son ",horas," horas, ",minutos," minutos y ",segundos," segundos.")