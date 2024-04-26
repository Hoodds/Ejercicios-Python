# Este programa define una clase Biblioteca que tiene métodos para realizar diversas operaciones 
# relacionadas con la gestión de la biblioteca. El método mostrar_menu() ofrece un menú interactivo 
# que permite al usuario seleccionar diferentes acciones para administrar los libros y las operaciones 
# de préstamo. Cada acción se implementa como un método de la clase Biblioteca.

# El ejemplo de uso al final del script crea una instancia de Biblioteca, agrega algunos libros de 
# ejemplo y luego muestra el menú para interactuar con la biblioteca. Puedes expandir este programa 
# según tus necesidades, como agregar validaciones adicionales o funcionalidades específicas para los 
# préstamos y devoluciones.
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = []  # Lista de libros disponibles
        self.libros_prestados = {}    # Diccionario de libros prestados
        self.usuarios = {}            # Diccionario de usuarios y libros prestados

    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor}
        self.libros_disponibles.append(libro)
        print(f"Libro '{titulo}' de '{autor}' agregado a la biblioteca.")

    def eliminar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro["titulo"].lower() == titulo.lower():
                self.libros_disponibles.remove(libro)
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
        print(f"Error: No se encontró el libro '{titulo}' en la biblioteca.")

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros_disponibles:
            if libro["titulo"].lower() == titulo.lower():
                self.libros_disponibles.remove(libro)
                self.libros_prestados[titulo] = libro
                if usuario in self.usuarios:
                    self.usuarios[usuario].append(titulo)
                else:
                    self.usuarios[usuario] = [titulo]
                print(f"Libro '{titulo}' prestado a {usuario}.")
                return
        print(f"Error: El libro '{titulo}' no está disponible para préstamo.")

    def devolver_libro(self, titulo, usuario):
        if usuario in self.usuarios and titulo in self.usuarios[usuario]:
            self.usuarios[usuario].remove(titulo)
            self.libros_disponibles.append(self.libros_prestados.pop(titulo))
            print(f"Libro '{titulo}' devuelto por {usuario}.")
        else:
            print(f"Error: El usuario {usuario} no tiene prestado el libro '{titulo}'.")

    def buscar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro["titulo"].lower() == titulo.lower():
                print(f"Libro '{libro['titulo']}' de '{libro['autor']}' disponible en la biblioteca.")
                return
        print(f"No se encontró el libro '{titulo}' en la biblioteca.")

    def mostrar_libros_disponibles(self):
        print("\nLibros disponibles en la biblioteca:")
        for libro in self.libros_disponibles:
            print(f"- '{libro['titulo']}' de '{libro['autor']}'")

    def mostrar_menu(self):
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
                self.agregar_libro(titulo, autor)
            elif opcion == "2":
                titulo = input("Ingrese el título del libro a eliminar: ")
                self.eliminar_libro(titulo)
            elif opcion == "3":
                titulo = input("Ingrese el título del libro a prestar: ")
                usuario = input("Ingrese el nombre del usuario: ")
                self.prestar_libro(titulo, usuario)
            elif opcion == "4":
                titulo = input("Ingrese el título del libro a devolver: ")
                usuario = input("Ingrese el nombre del usuario: ")
                self.devolver_libro(titulo, usuario)
            elif opcion == "5":
                titulo = input("Ingrese el título del libro a buscar: ")
                self.buscar_libro(titulo)
            elif opcion == "6":
                self.mostrar_libros_disponibles()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida (1-7).")


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("El principito", "Antoine de Saint-Exupéry")
    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez")
    biblioteca.agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes")

    biblioteca.mostrar_menu()
