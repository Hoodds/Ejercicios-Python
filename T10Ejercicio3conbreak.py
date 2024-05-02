def es_par(numero):
    """Función para verificar si un número dado es par. Si es par devuelve True"""
    return numero % 2 == 0

def main():
    # Lista para almacenar los números positivos ingresados por el usuario
    numeros = []

    print("Ingrese una lista de números positivos (termine con un número negativo):")

    # Ciclo para ingresar números hasta que se ingrese un número negativo
    while True:
        try:
            num = float(input("Ingrese un número: "))

            if num < 0:
                break  # Salir del bucle si se ingresa un número negativo

            numeros.append(num)

        except ValueError:
            print("Error: Por favor, ingrese solo números válidos.")

    # Mostrar la lista de números ingresados y si cada número es par o impar
    print("\nLista de números ingresados:")
    for numero in numeros:
        if es_par(numero):
            print(f"{numero} es PAR.")
        else:
            print(f"{numero} es IMPAR.")

if __name__ == "__main__":
    main()
