#Ejercicio 01
try:
    num1 = float(input("Ingrese un número: "))
    num2 = float(input("Ingrese un número: "))
    print(f"La división entre {num1} y {num2} es {num1/num2}")
except ValueError:
    print("Debe ingresar un número")
except ZeroDivisionError:
    print("No se puede dividir entrer cero")

#Ejercicio 02
def indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
            print("Ese indice no existe")
            return ""

listado = ["Manzana", "Pera", "Uva"]
try: 
    ingreso = int(input("Ingrese el indice: "))
    print(indice(listado,ingreso))
except ValueError:
    print("Debe ingresar un número")

#Ejercicio 03
while True:

    print("CALCULADORA BÁSICA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    try:
        opcion = int((input("Seleccione una opción: ")))
    except ValueError:
        print("Debe ingresar un número")
        continue
    
    if opcion == 1:
        try:
            a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
            print(f"La suma de {a} y {b} es {a+b}")
        except ValueError:
            print("Debe ingresar un número")
    
    elif opcion == 2:
        try:
            a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
            print(f"La resta de {a} y {b} es {a-b}")
        except ValueError:
            print("Debe ingresar un número")

    elif opcion == 3:
        try:
            a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
            print(f"La multiplicación de {a} y {b} es {a*b}")
        except ValueError:
            print("Debe ingresar un número")
    
    elif opcion == 4:
        try:
            a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
            print(f"La división de {a} y {b} es {a/b}")
        except ValueError:
            print("Debe ingresar un número")
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
    
    elif opcion == 5:
        break

    else:
        print("Opción no válida")