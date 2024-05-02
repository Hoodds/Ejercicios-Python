def convertir_mayusculas(texto):
    """Función para convertir un texto a mayúsculas."""
    if isinstance(texto, str):
        return texto.upper()
    else:
        raise ValueError("El argumento debe ser una cadena de texto.")

def contar_caracteres(texto):
    """Función para contar la cantidad de caracteres en un texto."""
    if isinstance(texto, str):
        return len(texto)
    else:
        raise ValueError("El argumento debe ser una cadena de texto.")

def invertir_palabras(texto):
    """Función para invertir el orden de las palabras en un texto."""
    if isinstance(texto, str):
        palabras = texto.split()  # Dividir el texto en una lista de palabras
        palabras_invertidas = palabras[::-1]  # Invertir la lista de palabras
        texto_invertido = ' '.join(palabras_invertidas)  # Unir las palabras invertidas en un texto
        return texto_invertido
    else:
        raise ValueError("El argumento debe ser una cadena de texto.")

def main():
    texto = input("Ingrese un texto: ")

    try:
        # Operación 1: Convertir texto a mayúsculas
        texto_mayusculas = convertir_mayusculas(texto)
        print(f"Texto en mayúsculas: {texto_mayusculas}")

        # Operación 2: Contar la cantidad de caracteres en el texto
        cantidad_caracteres = contar_caracteres(texto)
        print(f"Cantidad de caracteres: {cantidad_caracteres}")

        # Operación 3: Invertir el orden de las palabras en el texto
        texto_invertido = invertir_palabras(texto)
        print(f"Texto con palabras invertidas: {texto_invertido}")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()