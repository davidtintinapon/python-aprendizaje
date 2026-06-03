#Ejercicio 04
def contar_palabras(frase):
    diccionario = {}
    palabras = frase.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


frase = input("Ingrese una frase: ")
print(contar_palabras(frase))

#Ejercicio 05
contactos = {}

while True:
 
    print("\n1. Agregar")
    print("2. Buscar")
    print("3. Mostrar")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")

        contactos[nombre] = telefono

    elif opcion == "2":

        nombre = input("Buscar nombre: ")

        if nombre in contactos:
            print(contactos[nombre])
        else:
            print("Contacto no encontrado")

    elif opcion == "3":

        for nombre in contactos:
            print(nombre, ":", contactos[nombre])

    elif opcion == "4":
        break

    else:
        print("Opción inválida")

#Ejercicio 06
def poco_stock(productos):
    lista = []
    for producto in productos:
        if productos[producto] < 5:
            lista.append(producto)
    return lista

inventario = {
    "Arroz": 10,
    "Leche": 3,
    "Azúcar": 2,
    "Aceite": 8
}

print(poco_stock(inventario))