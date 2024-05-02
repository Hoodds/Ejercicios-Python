def calcular_media(num1, num2, num3):
    # Verificar si todos los argumentos son números
    if not (isinstance(num1, (int, float)) and
            isinstance(num2, (int, float)) and
            isinstance(num3, (int, float))):
        raise ValueError("Todos los argumentos deben ser números.")

    # Calcular la media de los tres números
    media = (num1 + num2 + num3) / 3
    return media

def main():
    try:
        # Solicitar al usuario que ingrese tres números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        # Calcular la media utilizando la función calcular_media
        resultado = calcular_media(num1, num2, num3)

        # Mostrar el resultado al usuario
        print(f"La media de {num1}, {num2} y {num3} es: {resultado}")

    except ValueError as error:
        print(f"Error: {error}. Por favor, asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    main()
