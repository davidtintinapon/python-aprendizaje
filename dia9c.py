#Ejercicio 07
canasta = {}

for x in range(3):
    producto = input("Ingrese un producto: ").lower()
    precio = float(input("Ingrese el precio del producto ingresado: "))
    canasta[producto] = precio

print(canasta.keys())
user = input("¿Que producto desea consultar?: ").lower()
if user in canasta:
    print(f"El precio es: {canasta[user]} soles")
else:
    print("Error de ingreso")

#Ejercicio 08
notas = {
    "Ana": 18,
    "Luis": 9,
    "María": 15,
    "Pedro": 7
}

print(notas)

aprobados = 0
desaprobados = 0

for alumno in notas:
    if notas[alumno] >= 11:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Aprobados: {aprobados}")
print(f"Desaprobados: {desaprobados}")

#Ejercicio 09
notas1 = {
    "Ana": 18,
    "Luis": 9,
    "María": 20,
    "Pedro": 15
}
print(notas1)
nota_alta = notas1["Ana"]
alumno_a = "Ana"

for alumno in notas1:
    if notas1[alumno] > nota_alta:
        nota_alta = notas1[alumno]
        alumno_a = alumno
    
print(f"Tiene mayor nota {alumno_a}")