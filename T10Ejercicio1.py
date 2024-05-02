def dividir_numeros_enteros(dividendo, divisor):
    # Verificar si ambos números son enteros
    # isinstance recibe como argumentos un objeto y una clase y devuelve True si el objeto es una instancia de dicha clase o de una subclase de ella
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise ValueError("Ambos argumentos deben ser números enteros.")

    # Verificar si el divisor no es cero
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")

    # Realizar la división y devolver el cociente
    cociente = dividendo // divisor
    return cociente

# Función principal para probar la función de división
def main():
    try:
        # Llamadas a la función dividir_numeros_enteros con diferentes valores
        resultado1 = dividir_numeros_enteros(20, 4)
        print(f"División 20 / 4 = {resultado1}")

        resultado2 = dividir_numeros_enteros(15, 7)
        print(f"División 15 / 7 = {resultado2}")

        resultado3 = dividir_numeros_enteros(100, 0)  # Intentar dividir por cero
        print(f"División 100 / 0 = {resultado3}")  # Esta línea no se imprimirá debido a la excepción

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
