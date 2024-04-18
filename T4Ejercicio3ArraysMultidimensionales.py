# -*- coding: utf-8 -*-
columna1=[0]*3
columna2=[0]*3
columna3=[0]*3
matriz=[columna1, columna2, columna3]
i = 0
j = 0
for i in range(0, 3):
    for j in range(0,3):
        if i==j:
            matriz[i][j]=1

for i in range(0, 3): # visualizacion de la matriz c
    for j in range(0, 3):
        print(matriz[i][j])

print(matriz[0][0]," | ",matriz[0][1]," | ",matriz[0][2]) # visualizacion con separadores
print(matriz[1][0]," | ",matriz[1][1]," | ",matriz[0][2])
print(matriz[2][0]," | ",matriz[2][1]," | ",matriz[2][2])

for i in range(0, 3): # visualizacion con separadores con repetitiva
    print(" | ", end="") # , end="") hace que el print no salte de linea
    for j in range(0,3):
        print(matriz[i][j]," | ", end="")
    print()