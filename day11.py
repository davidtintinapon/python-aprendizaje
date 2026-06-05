with open("notas.txt", "w") as archivo:

    nombre = input("Ingrese su nombre: ")
    ciudad = input("Ingrese su ciudad: ")

    archivo.write(nombre + "\n")
    archivo.write(ciudad + "\n")

try:
    with open("notas.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe")