# -*- coding: utf-8 -*-
salariototal=0
salariomensual=0
for i in range(1, 6):
    salariomensual=input("Introduce el salario mensual del trabajador "+str(i)+": ")
    salariototal=salariototal+int(salariomensual)
print("El salario total de los 5 trabajadores es "+str(salariototal)+" euros mensuales.")
mediasalarial=0
mediasalarial=salariototal/5
print("La media salarial de los 5 trabajadores es "+str(mediasalarial)+" euros mensuales.")