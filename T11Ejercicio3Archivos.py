# Función para añadir un nuevo producto al inventario
def agregar_producto(nombre, descripcion, precio, cantidad):
    with open("inventario.txt", "a") as archivo:
        archivo.write(f"{nombre}: {descripcion}: {precio}: {cantidad}\n")

# Función para actualizar la cantidad de un producto en el inventario
def actualizar_cantidad(nombre, nueva_cantidad):
    with open("inventario.txt", "r") as archivo:
        lineas = archivo.readlines()
    with open("inventario.txt", "w") as archivo:
        for linea in lineas:
            if nombre in linea:
                partes = linea.split(": ")
                partes[-1] = str(nueva_cantidad) + "\n"
                linea = ": ".join(partes)
            archivo.write(linea)

# Función para ver el inventario completo
def ver_inventario():
    with open("inventario.txt", "r") as archivo:
        print("Inventario:")
        for linea in archivo:
            print(linea.strip())

# Función para buscar un producto por su nombre y mostrar su información
def buscar_producto(nombre):
    with open("inventario.txt", "r") as archivo:
        for linea in archivo:
            if nombre in linea:
                print("Información del producto:")
                print(linea.strip())
                return
        print("Producto no encontrado.")

# Función principal que muestra el menú y maneja las operaciones
def main():
    while True:
        print("\nMenú:")
        print("1. Añadir nuevo producto al inventario")
        print("2. Actualizar cantidad de un producto")
        print("3. Ver inventario completo")
        print("4. Buscar producto por nombre")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del nuevo producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            precio = input("Ingrese el precio unitario del producto: ")
            cantidad = input("Ingrese la cantidad en stock del producto: ")
            agregar_producto(nombre, descripcion, precio, cantidad)
            print("Producto añadido al inventario.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad en stock: ")
            actualizar_cantidad(nombre, nueva_cantidad)
            print("Cantidad actualizada.")
        elif opcion == "3":
            ver_inventario()
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(nombre)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
