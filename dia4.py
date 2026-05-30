edad = int(input("¿Cuantos años tienes?: "))

if edad < 18 and edad > 0:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 65:
    print("Eres adulto")
elif edad >= 65 and edad <= 110:
    print("Eres adulto mayor")
else:
    print("Edad no válida")