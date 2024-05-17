import os  # Importa el módulo os para trabajar con archivos y directorios

FILENAME = "tareas.txt"  # Nombre del archivo donde se guardarán las tareas

def cargar_tareas():
    """Carga las tareas desde el archivo de texto."""
    if not os.path.exists(FILENAME):  # Verifica si el archivo de tareas existe
        return []  # Si no existe, devuelve una lista vacía
    
    with open(FILENAME, 'r') as file:  # Abre el archivo en modo lectura
        # Lee cada línea del archivo, elimina los espacios en blanco alrededor y crea una lista de tareas
        tareas = [line.strip() for line in file.readlines()]
    return tareas  # Devuelve la lista de tareas

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo de texto."""
    with open(FILENAME, 'w') as file:  # Abre el archivo en modo escritura
        for tarea in tareas:  # Itera sobre cada tarea en la lista de tareas
            file.write(f"{tarea}\n")  # Escribe la tarea en el archivo seguida de un salto de línea

def mostrar_menu():
    """Muestra el menú de opciones disponibles."""
    print("\nGestión de Tareas")
    print("1. Añadir tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como realizada")
    print("4. Guardar y salir")

def añadir_tarea(tareas):
    """Permite al usuario añadir una nueva tarea."""
    tarea = input("Introduce el nombre de la tarea: ")  # Solicita al usuario ingresar el nombre de la tarea
    tareas.append(tarea)  # Agrega la nueva tarea a la lista de tareas
    print(f"Tarea '{tarea}' añadida.")  # Muestra un mensaje indicando que la tarea se añadió correctamente

def ver_tareas(tareas):
    """Muestra todas las tareas numeradas."""
    if not tareas:  # Verifica si la lista de tareas está vacía
        print("No hay tareas pendientes.")  # Si está vacía, muestra un mensaje indicando que no hay tareas
    else:
        for idx, tarea in enumerate(tareas, start=1):  # Itera sobre cada tarea en la lista de tareas, empezando desde 1
            print(f"{idx}. {tarea}")  # Muestra el número de tarea y su nombre

def marcar_tarea_realizada(tareas):
    """Permite al usuario marcar una tarea como realizada."""
    ver_tareas(tareas)  # Muestra todas las tareas para que el usuario pueda elegir cuál marcar como realizada
    try:
        num = int(input("Introduce el número de la tarea a marcar como realizada: "))  # Solicita al usuario ingresar el número de la tarea a marcar
        if 1 <= num <= len(tareas):  # Verifica si el número de tarea está dentro del rango válido
            tarea_realizada = tareas.pop(num-1)  # Elimina la tarea de la lista de tareas y la guarda en una variable
            print(f"Tarea '{tarea_realizada}' marcada como realizada.")  # Muestra un mensaje indicando que la tarea se marcó como realizada
        else:
            print("Número de tarea inválido.")  # Si el número de tarea no es válido, muestra un mensaje de error
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")  # Maneja el caso en que se ingrese una entrada no numérica

def main():
    """Función principal del programa."""
    tareas = cargar_tareas()  # Carga las tareas existentes desde el archivo
    
    while True:  # Bucle principal del programa
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Selecciona una opción (1-4): ")  # Solicita al usuario seleccionar una opción del menú

        if opcion == '1':
            añadir_tarea(tareas)  # Si la opción es 1, permite al usuario añadir una nueva tarea
        elif opcion == '2':
            ver_tareas(tareas)  # Si la opción es 2, muestra todas las tareas
        elif opcion == '3':
            marcar_tarea_realizada(tareas)  # Si la opción es 3, permite al usuario marcar una tarea como realizada
        elif opcion == '4':
            guardar_tareas(tareas)  # Si la opción es 4, guarda las tareas en el archivo y sale del programa
            print("Tareas guardadas. ¡Adiós!")  # Muestra un mensaje de despedida
            break  # Sale del bucle principal
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")  # Maneja el caso en que se ingrese una opción no válida

if __name__ == "__main__":
    main()  # Llama a la función principal si el script se ejecuta directamente
