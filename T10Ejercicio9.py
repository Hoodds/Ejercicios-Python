def clasificar_triangulo(lado1, lado2, lado3):
    """Función para clasificar un triángulo según la longitud de sus lados."""
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "No es un triángulo válido. Las longitudes de los lados deben ser positivas."

    if lado1 == lado2 == lado3:
        return "El triángulo es Equilátero."  # Todos los lados son iguales
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "El triángulo es Isósceles."  # Dos lados son iguales
    else:
        return "El triángulo es Escaleno."  # Todos los lados son diferentes

def main():
    try:
        lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

        resultado = clasificar_triangulo(lado1, lado2, lado3)
        print(resultado)

    except ValueError:
        print("Error: Por favor, ingrese longitudes válidas (números positivos).")

if __name__ == "__main__":
    main()
