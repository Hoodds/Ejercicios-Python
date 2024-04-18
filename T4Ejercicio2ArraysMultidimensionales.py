# -*- coding: utf-8 -*-
acol1=[7]*4 #columna 1 de la matriz a
acol2=[7]*4
acol3=[7]*4
acol4=[7]*4
amatriz=[acol1, acol2, acol3, acol4] # primera matriz 4*4 (a)
bcol1=[11]*4 #columna 1 de la matriz b
bcol2=[11]*4
bcol3=[11]*4
bcol4=[11]*4
bmatriz=[bcol1, bcol2, bcol3, bcol4] # segunda matriz 4*4 (b)
ccol1=[0]*4 #columna 1 de la matriz c
ccol2=[0]*4
ccol3=[0]*4
ccol4=[0]*4
cmatriz=[ccol1, ccol2, ccol3, ccol4] # tercera matriz 4*4 (c)

for i in range(0, 4): # la matriz c se rellena con la suma de la matriz a y la matriz b
    for j in range(0, 4):
        cmatriz[i][j]=amatriz[i][j]+bmatriz[i][j]

for i in range(0, 4): # visualizacion de la matriz c
    for j in range(0, 4):
        print(cmatriz[i][j])
print(cmatriz)   #meter un for para hacer salto de linea     