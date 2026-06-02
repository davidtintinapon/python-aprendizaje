#Ejercicio 01
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("David"))

#Ejercicio 02
def area_rectangulo(b,a):
    if b > 0 and a > 0:
        return f"El área de un rectangulo es {b*a} metros cuadrados"
    else:
        return f"Ingreso no válido"

base = int(input("Ingrese la base de un rectangulo: "))
altura = int(input("Ingrese la altura de un rectangulo: "))

print(area_rectangulo(base,altura))

#Ejercicio 03
def es_par(numero):
    if numero == 0:
        return f"El número es {numero}"
    elif numero % 2 == 0:
        return f"El número {numero} es par"
    else:
        return f"El número es impar"

user = int(input("Ingrese un número: "))
print(es_par(user))

#Ejercicio 04
def mayor_de_3(numeros):
    mayor = numeros[0]
    for x in numeros:
        if x > mayor:
            mayor = x
    return f"El mayor es {mayor}"

lista = []

for x in range(3):
    user = int(input("Ingrese un número: "))
    lista.append(user)

print(mayor_de_3(lista))