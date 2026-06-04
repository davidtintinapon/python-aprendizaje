#Ejercicio 13
notas = {
    "Ana": 18,
    "Luis": 9,
    "María": 15,
    "Pedro": 7
}

for x,y in notas.items():
    print(f"{x} : {y}")

#Ejercicio 14
notas2 = {
    "Ana": 18,
    "Luis": 9,
    "María": 15,
    "Pedro": 7
}

nota_baja = notas2["Ana"]
nombre = "Ana"

for nt in notas2:
    if notas2[nt] < nota_baja:
        nota_baja = notas2[nt]
        nombre = nt
print(f"Alumno con menor nota: {nombre}")
print(f"Nota: {nota_baja}")

#Ejercicio 15
personas = {}

for x in range(4):
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese la edad: "))
    personas[nombre] = edad

mayor = 0
for edad_mayor in personas.values():
    if edad_mayor >= 18:
        mayor += 1

print(f"Hay {mayor} personas mayores de edad.")