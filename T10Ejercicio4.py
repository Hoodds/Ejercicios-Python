def suma(a, b):
    """Función para sumar dos números."""
    return a + b

def resta(a, b):
    """Función para restar dos números."""
    return a - b

def multiplicacion(a, b):
    """Función para multiplicar dos números."""
    return a * b

def division(a, b):
    """Función para dividir dos números. Maneja la división por cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def menu_operaciones():
    """Función para mostrar el menú de operaciones y obtener la selección del usuario."""
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        opcion = input("Seleccione la operación (1/2/3/4): ")

        if opcion in ['1', '2', '3', '4']:
            return opcion
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def obtener_numeros():
    """Función para obtener dos números del usuario."""
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")

def main():
    while True:
        # Mostrar el menú de operaciones y obtener la selección del usuario
        opcion = menu_operaciones()

        # Obtener dos números del usuario
        num1, num2 = obtener_numeros()

        try:
            if opcion == '1':
                resultado = suma(num1, num2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == '2':
                resultado = resta(num1, num2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"Resultado de la división: {resultado}")

        except ValueError as error:
            print(f"Error: {error}")

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
