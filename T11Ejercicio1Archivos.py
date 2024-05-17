# Solicitar al usuario introducir una lista de nombres separados por comas
nombres_input = input("Introduce una lista de nombres separados por comas: ")

# Guardar los nombres en un archivo de texto
with open("nombres.txt", "w") as archivo:
    archivo.write(nombres_input)

# Leer el contenido del archivo y mostrar los nombres en la consola
with open("nombres.txt", "r") as archivo:
    contenido = archivo.read()

# Imprimir los nombres leídos del archivo
print("Los nombres en el archivo son:")
nombres = contenido.split(',')
for nombre in nombres:
    print(nombre.strip())