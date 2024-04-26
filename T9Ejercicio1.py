import random

# Esta función elige aleatoriamente una palabra de una lista predefinida de palabras.
def seleccionar_palabra():
    palabras = ["python", "ubuntu", "visual", "computadora", "aprendizaje"]
    return random.choice(palabras)

# Esta función genera una cadena que muestra el progreso actual del jugador en adivinar la palabra,
# usando guiones bajos para letras no adivinadas.
def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso

# Esta función ejecuta el juego principal. Muestra el progreso actual de la palabra, permite al 
# usuario ingresar letras, verifica si la letra está en la palabra secreta, y muestra mensajes según
# el resultado del intento. Además, ofrece al usuario la opción de jugar nuevamente después de que 
# se complete una partida.
def jugar_adivinanza():
    palabra_secreta = seleccionar_palabra()
    intentos_restantes = 10
    letras_adivinadas = []

    print("¡Bienvenido al juego de adivinar palabras!")
    print("Adivina la palabra. Tienes 10 intentos.")

    while intentos_restantes > 0:
        print("\n" + mostrar_progreso(palabra_secreta, letras_adivinadas))

        if "_" not in mostrar_progreso(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
            break

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya has intentado esa letra. Prueba con otra.")
            continue
        
        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos_restantes -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos_restantes} intentos.")
    
    else:
        print("\n¡Has agotado tus intentos!")
        print(f"La palabra correcta era: {palabra_secreta}")
    
    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_nuevamente == "s":
        jugar_adivinanza()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

# Iniciar el juego
jugar_adivinanza()
