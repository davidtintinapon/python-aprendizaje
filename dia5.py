#Ejer01 Números del 1 al 20
for x in range(1,21):
    print(x)

#Ejer02 suma de los números del 1 al 100
suma = 0
for x in range(1,101):
    suma += x

print(f"La suma total de números del 1 al 100 es: {suma}")

#Ejer03 Números pares del 1 al 50
for x in range(1,51):

    if x % 2 == 0:
        print(x)