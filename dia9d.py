#Ejercicio 10
grupo = {"Juan": 18, "Martin": 14, "Marco": 15}
total = 0
for notas in grupo.values():
    total += notas

print(grupo)
promedio = total / len(grupo)
print(f"El promedio de las notas es: {promedio:.2f}")

#Ejercicio 11
productos = {
    "Arroz": 5,
    "Leche": 4,
    "Azúcar": 3,
    "Aceite": 8
}
mas_caro = productos["Arroz"]
nombre = "Arroz"
for valor in productos:
    if productos[valor] > mas_caro:
        mas_caro = productos[valor]
        nombre = valor
print(productos)
print(f"El producto más caro es {nombre} y su precio es {mas_caro} soles.")

#Ejercicio 12

agenda = {}

for x in range(4):
    nombre = input("Ingrese nombre de contacto: ").lower()
    telefono = input("Ingrese teléfono de contacto: ")

    agenda[nombre] = telefono

while True:

    print("AGENDA DE CONTACTOS")
    print("1. Buscar contacto.")
    print("2. Salir.")
    usuario = input("Ingrese una opción: ")

    if usuario == "1":
        busqueda = input("Ingrese nombre de contacto: ").lower()
        if busqueda in agenda:
            print(f"Contacto existente, su número es: {agenda[busqueda]}")
        else:
            print("No se encuentra en la agenda")
    elif usuario == "2":
        break
    else:
        print("Ingreso no válido")


    