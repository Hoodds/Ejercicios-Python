def longitud_mes(mes):
    return (len(mes), registros_lluvia[mes])

registros_lluvia = {}

for mes in ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"):
    lluvia = float(input(f"Ingrese los registros de lluvia para {mes}: "))
    lluvia_redondeada = round(lluvia)
    registros_lluvia[mes] = lluvia_redondeada

mes_mas_lluvioso = max(registros_lluvia, key=registros_lluvia.get)
mes_menos_lluvioso = min(registros_lluvia, key=registros_lluvia.get)

registros_ordenados = sorted(registros_lluvia.keys(), key=longitud_mes)

print("\nMeses y registros de lluvia:")
for mes in registros_ordenados:
    print(f"{mes}: {registros_lluvia[mes]} litros")

print(f"\nEl mes más lluvioso fue {mes_mas_lluvioso} con {registros_lluvia[mes_mas_lluvioso]} litros.")
print(f"El mes menos lluvioso fue {mes_menos_lluvioso} con {registros_lluvia[mes_menos_lluvioso]} litros.")
