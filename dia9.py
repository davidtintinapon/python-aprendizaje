#Ejercicio 01
student = {
    "nombre": "David",
    "edad": 21,
    "carrera": "Ing de Sistemas",
    "promedio": 17
}

student["promedio"] = 20
for x,y in student.items():
    print(x,y)

#Ejercicio 02
def mas_caro(productos):
    producto_mayor = ""
    precio_mayor = 0
    for nombre, precio in productos.items():
        if precio > precio_mayor:
            precio_mayor = precio
            producto_mayor = nombre
    return f"Producto mayor: {producto_mayor} y su precio es {precio_mayor} soles"

productos = {"radio": 10, "tv": 100, "lapiz": 2, "laptop": 2000}
print(mas_caro(productos))

#Ejercicio 03
estudiantes = [
    {"nombre": "Jorge", "nota": 12},
    {"nombre": "Samuel", "nota": 14},
    {"nombre": "José", "nota": 10}
]
print("Estudiantes que aprobaron:")
for estudiante in estudiantes:
    if estudiante["nota"] >= 11:
        print(estudiante["nombre"], estudiante["nota"])