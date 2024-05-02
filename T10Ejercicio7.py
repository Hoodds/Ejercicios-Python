def celsius_a_fahrenheit(celsius):
    """Función para convertir grados Celsius a grados Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Función para convertir grados Fahrenheit a grados Celsius."""
    return (fahrenheit - 32) * 5/9

def convertir_temperatura():
    """Función principal para realizar la conversión de temperatura."""
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = input("¿Qué conversión desea realizar?\n"
                           "1. Celsius a Fahrenheit\n"
                           "2. Fahrenheit a Celsius\n"
                           "Ingrese el número de opción (1 o 2): ")

            if opcion not in ['1', '2']:
                raise ValueError("Opción no válida. Por favor, ingrese '1' o '2'.")

            temperatura = float(input("Ingrese la temperatura a convertir: "))

            if opcion == '1':
                resultado = celsius_a_fahrenheit(temperatura)
                print(f"{temperatura} grados Celsius son equivalentes a {resultado:.2f} grados Fahrenheit.")
            elif opcion == '2':
                resultado = fahrenheit_a_celsius(temperatura)
                print(f"{temperatura} grados Fahrenheit son equivalentes a {resultado:.2f} grados Celsius.")

            opcion_valida = True

        except ValueError as error:
            print(f"Error: {error}. Intente nuevamente.")

def main():
    convertir_temperatura()

if __name__ == "__main__":
    main()
