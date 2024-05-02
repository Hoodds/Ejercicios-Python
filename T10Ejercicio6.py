def es_numero_primo(numero):
    """Función que verifica si un número es primo."""
    if not isinstance(numero, int) or numero <= 1:
        raise ValueError("Debe ingresar un número entero positivo mayor que 1.")

    # Comprobamos si el número es divisible por algún número entre 2 y su raíz cuadrada
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

def main():
    try:
        numero = int(input("Ingrese un número entero positivo mayor que 1: "))

        if es_numero_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")

    except ValueError as error:
        print(f"Error: {error}. Por favor, ingrese un número entero positivo mayor que 1.")

if __name__ == "__main__":
    main()
