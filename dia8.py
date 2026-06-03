#Ejercicio 01
canasta = ["Manzana", "Pera", "Banana", "Mango", "Fresa"]
user = input("Ingrese el nombre de una fruta: ")
canasta.append(user)
canasta.remove("Pera")
print(canasta)

#Ejercicio 02
numeros = [4,9,1,7,8]
print(f"Lista desordenada: {numeros}")
numeros.sort()
print(f"Lista ordenada {numeros}")

#Ejercicio 03
def promedio(lista):
    promedio = sum(lista) / len(lista)
    return f"El promedio es {promedio}"

numeros = []
for x in range(5):
    ingreso = float(input("Ingrese un número: "))
    numeros.append(ingreso)

print(promedio(numeros))

#Ejercicio 04
def es_par(lista):
    mostrar_par = []
    for x in lista:
        if x % 2 == 0:
            mostrar_par.append(x)
    return f"Son números pares: {mostrar_par}"

ingreso = []
for x in range(5):
    usuario = float(input("Ingrese un número: "))
    ingreso.append(usuario)

print(es_par(ingreso))