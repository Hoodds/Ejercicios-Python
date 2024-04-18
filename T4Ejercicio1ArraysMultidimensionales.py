# -*- coding: utf-8 -*-
columna1=[0]*4
columna2=[0]*4
columna3=[0]*4
columna4=[0]*4
matriz=[columna1, columna2, columna3, columna4]
for i in range(0, 4):
    for j in range(0,4):
        matriz[i][j]=(i*20)+(j+1)*5
for i in range(0, 4):
    for j in range(0,4):
        print(matriz[i][j])