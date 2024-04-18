'''meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
        "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
lluvias = (0)*12
for i in range [0,12]:
    print("Introduzca las lluvias de ", meses[i])
    lluvias[i]=input()'''

# obtiene la longitud de un mes
def longitud_mes(mes):
    return (len(mes), registros_lluvia[mes])

registros_lluvia = {} #esto es un diccionario. te permite almacenar pares de datos, por ejemplo: enero, 20; febrero, 15;etc..

# se piden los datos
for mes in ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"):
    lluvia = float(input(f"Ingrese los registros de lluvia para {mes}: "))
    lluvia_redondeada = round(lluvia)
    registros_lluvia[mes] = lluvia_redondeada

# Calcular el mes más lluvioso y el mes menos lluvioso
mes_mas_lluvioso = max(registros_lluvia, key=registros_lluvia.get) #es un argumento opcional de max() que especifica una función de clave para determinar el valor que se utilizará para comparar los elementos del diccionario. En este caso, registros_lluvia.get es una referencia al método .get() del diccionario registros_lluvia.
mes_menos_lluvioso = min(registros_lluvia, key=registros_lluvia.get)

# Ordenar los registros de lluvia por el número de letras del mes y la cantidad de lluvia
registros_ordenados = sorted(registros_lluvia.keys(), key=longitud_mes)

# Mostrar resultados
print("\nMeses y registros de lluvia:")
for mes in registros_ordenados:
    print(f"{mes}: {registros_lluvia[mes]} litros")

print(f"\nEl mes más lluvioso fue {mes_mas_lluvioso} con {registros_lluvia[mes_mas_lluvioso]} litros.")
print(f"El mes menos lluvioso fue {mes_menos_lluvioso} con {registros_lluvia[mes_menos_lluvioso]} litros.")

