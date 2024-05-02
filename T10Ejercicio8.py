def contar_vocales(texto):
    """Función para contar el número de vocales en una cadena de texto."""
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

def contar_digitos(numero):
    """Función para contar el número de dígitos en un número entero."""
    if not isinstance(numero, int):
        raise ValueError("El argumento debe ser un número entero.")
    
    if numero == 0:
        return 1  # El único dígito de 0 es el propio 0

    contador = 0
    numero = abs(numero)  # Convertir el número a positivo para contar los dígitos
    while numero > 0:
        numero //= 10
        contador += 1
    return contador

def contar_vocales_y_digitos():
    """Función principal para contar vocales y dígitos según la entrada del usuario."""
    entrada = input("Ingrese un texto o un número entero: ")

    try:
        numero = int(entrada)  # Intentar convertir la entrada a un número entero
        # Si se puede convertir a un número entero, llamar a contar_digitos
        resultado_digitos = contar_digitos(numero)
        print(f"El número de dígitos en {numero} es: {resultado_digitos}")

    except ValueError:
        # Si la conversión a un número entero falla, asumir que es una cadena de texto
        resultado_vocales = contar_vocales(entrada)
        print(f"El número de vocales en '{entrada}' es: {resultado_vocales}")

def main():
    contar_vocales_y_digitos()

if __name__ == "__main__":
    main()
