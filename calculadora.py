while True:

    print("CALCULADORA BÁSICA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = (input("Seleccione una opción: "))

    if opcion == "1":
        a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
        print(f"La suma de {a} y {b} es {a+b}")
    
    elif opcion == "2":
        a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
        print(f"La resta de {a} y {b} es {a-b}")

    elif opcion == "3":
        a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
        print(f"La multiplicación de {a} y {b} es {a*b}")
    
    elif opcion == "4":
        a,b = map(float, input("Ingrese 2 números separados por espacio: ").split())
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            print(f"La división de {a} y {b} es {a/b}")
    
    elif opcion == "5":
        break

    else:
        print("Opción no válida")