# En este programa, utilizamos un diccionario productos para almacenar la información de 
# los productos disponibles en la tienda, donde cada clave representa el nombre del producto 
# y el valor es otro diccionario con el precio y el stock. El diccionario carrito se utiliza 
# para mantener un registro de los productos añadidos al carrito de la compra y las cantidades 
# correspondientes.

# Las funciones implementadas permiten realizar diversas operaciones, como añadir productos al
# carrito, eliminar productos del carrito, calcular el total de la compra, mostrar el carrito de
# la compra, mostrar productos disponibles, actualizar el stock de un producto y gestionar productos
# agotados. El menú interactivo permite al usuario seleccionar las acciones deseadas para simular 
# una experiencia de compra en línea.

# Diccionario para almacenar productos disponibles y su información
productos = {
    "camisa": {"precio": 20, "stock": 10},
    "pantalón": {"precio": 30, "stock": 8},
    "zapatos": {"precio": 50, "stock": 5},
    "sombrero": {"precio": 15, "stock": 12}
}

# Carrito de la compra
carrito = {}

def mostrar_productos_disponibles():
    print("\nProductos disponibles en la tienda:")
    for producto, info in productos.items():
        print(f"- {producto.capitalize()}: ${info['precio']} - Stock: {info['stock']}")

def agregar_producto_carrito(producto, cantidad):
    if producto in productos:
        if cantidad <= productos[producto]["stock"]:
            if producto in carrito:
                carrito[producto] += cantidad
            else:
                carrito[producto] = cantidad
            productos[producto]["stock"] -= cantidad
            print(f"{cantidad} {producto}(s) añadido(s) al carrito.")
        else:
            print(f"No hay suficiente stock de {producto}. Stock disponible: {productos[producto]['stock']}.")
    else:
        print(f"El producto '{producto}' no está disponible en la tienda.")

def eliminar_producto_carrito(producto, cantidad):
    if producto in carrito:
        if cantidad <= carrito[producto]:
            carrito[producto] -= cantidad
            productos[producto]["stock"] += cantidad
            if carrito[producto] == 0:
                del carrito[producto]
            print(f"{cantidad} {producto}(s) eliminado(s) del carrito.")
        else:
            print(f"No hay {cantidad} {producto}(s) en el carrito.")
    else:
        print(f"No hay {producto}(s) en el carrito.")

def calcular_total_carrito():
    total = 0
    for producto, cantidad in carrito.items():
        total += productos[producto]["precio"] * cantidad
    return total

def mostrar_carrito():
    print("\nCarrito de la compra:")
    for producto, cantidad in carrito.items():
        print(f"- {cantidad} {producto.capitalize()} - Precio unitario: ${productos[producto]['precio']}")

def actualizar_stock(producto, cantidad):
    if producto in productos:
        productos[producto]["stock"] += cantidad
        print(f"Stock de '{producto}' actualizado. Nuevo stock: {productos[producto]['stock']}.")
    else:
        print(f"El producto '{producto}' no existe en la tienda. Se añadirá como nuevo producto.")
        productos[producto] = {"precio": 0, "stock": cantidad}

def mostrar_menu():
    while True:
        print("\n----- Menú de Tienda Virtual -----")
        print("1. Mostrar productos disponibles")
        print("2. Agregar producto al carrito")
        print("3. Eliminar producto del carrito")
        print("4. Calcular total del carrito")
        print("5. Actualizar stock de un producto")
        print("6. Mostrar carrito de la compra")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            mostrar_productos_disponibles()
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto a añadir al carrito: ").lower()
            cantidad = int(input("Ingrese la cantidad a añadir: "))
            agregar_producto_carrito(producto, cantidad)
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto a eliminar del carrito: ").lower()
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_producto_carrito(producto, cantidad)
        elif opcion == "4":
            total = calcular_total_carrito()
            print(f"Total a pagar: ${total}")
        elif opcion == "5":
            producto = input("Ingrese el nombre del producto a actualizar el stock: ").lower()
            cantidad = int(input("Ingrese la cantidad a añadir al stock: "))
            actualizar_stock(producto, cantidad)
        elif opcion == "6":
            mostrar_carrito()
        elif opcion == "7":
            print("¡Gracias por su compra!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1-7).")


# Ejemplo de uso
if __name__ == "__main__":
    mostrar_menu()
