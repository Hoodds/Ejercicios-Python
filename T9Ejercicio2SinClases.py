# En este ejemplo, las operaciones como agregar un libro, eliminar un libro, prestar un libro, 
# devolver un libro, buscar un libro y mostrar libros disponibles se implementan como funciones 
# que trabajan con las listas y diccionarios definidos al principio del programa. La función mostrar_menu()
# permite al usuario interactuar con el programa seleccionando diferentes opciones mediante la entrada de texto.

# Puedes expandir este programa agregando más funcionalidades, como validaciones adicionales o manejo de 
# errores, según sea necesario para simular el sistema de gestión de una biblioteca.

# Diccionario para almacenar libros disponibles
libros_disponibles = []

# Diccionario para registrar préstamos de libros
libros_prestados = {}

# Diccionario para registrar usuarios y los libros que han tomado prestados
usuarios = {}

def agregar_libro(titulo, autor):
    libro = {"titulo": titulo, "autor": autor}
    libros_disponibles.append(libro)
    print(f"Libro '{titulo}' de '{autor}' agregado a la biblioteca.")

def eliminar_libro(titulo):
    for libro in libros_disponibles:
        if libro["titulo"].lower() == titulo.lower():
            libros_disponibles.remove(libro)
            print(f"Libro '{titulo}' eliminado de la biblioteca.")
            return
    print(f"Error: No se encontró el libro '{titulo}' en la biblioteca.")

def prestar_libro(titulo, usuario):
    for libro in libros_disponibles:
        if libro["titulo"].lower() == titulo.lower():
            libros_disponibles.remove(libro)
            libros_prestados[titulo] = libro
            if usuario in usuarios:
                usuarios[usuario].append(titulo)
            else:
                usuarios[usuario] = [titulo]
            print(f"Libro '{titulo}' prestado a {usuario}.")
            return
    print(f"Error: El libro '{titulo}' no está disponible para préstamo.")

def devolver_libro(titulo, usuario):
    if usuario in usuarios and titulo in usuarios[usuario]:
        usuarios[usuario].remove(titulo)
        libros_disponibles.append(libros_prestados.pop(titulo))
        print(f"Libro '{titulo}' devuelto por {usuario}.")
    else:
        print(f"Error: El usuario {usuario} no tiene prestado el libro '{titulo}'.")

def buscar_libro(titulo):
    for libro in libros_disponibles:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Libro '{libro['titulo']}' de '{libro['autor']}' disponible en la biblioteca.")
            return
    print(f"No se encontró el libro '{titulo}' en la biblioteca.")

def mostrar_libros_disponibles():
    print("\nLibros disponibles en la biblioteca:")
    for libro in libros_disponibles:
        print(f"- '{libro['titulo']}' de '{libro['autor']}'")

def mostrar_menu():
    while True:
        print("\n----- Menú de Biblioteca -----")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Mostrar libros disponibles")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el nombre del autor: ")
            agregar_libro(titulo, autor)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro a eliminar: ")
            eliminar_libro(titulo)
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a prestar: ")
            usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(titulo, usuario)
        elif opcion == "4":
            titulo = input("Ingrese el título del libro a devolver: ")
            usuario = input("Ingrese el nombre del usuario: ")
            devolver_libro(titulo, usuario)
        elif opcion == "5":
            titulo = input("Ingrese el título del libro a buscar: ")
            buscar_libro(titulo)
        elif opcion == "6":
            mostrar_libros_disponibles()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-7).")


# Ejemplo de uso
if __name__ == "__main__":
    agregar_libro("El principito", "Antoine de Saint-Exupéry")
    agregar_libro("Cien años de soledad", "Gabriel García Márquez")
    agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes")

    mostrar_menu()
