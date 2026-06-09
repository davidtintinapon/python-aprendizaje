from day13 import Student

students = []

while True:

    print("REGISTRO DE ESTUDIANTE")
    print("1. Registrar estudiante.")
    print("2. Listar estudiantes registrados.")
    print("3. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        
        try: 
            name = input("Ingrese su nombre: ")
            age = int(input("Ingrese su edad: "))
            career = input("Ingrese su carrera: ")
            new_student =  Student(name, age, career)
            students.append(new_student)
            print("Estudiante registrado con éxito")
    
        except ValueError:
            print("La edad debe ser un número")

    elif option == "2":
        
        if len(students) == 0:
            print("No hay estudiantes registrados")
        else:
            for student in students:
                print(student.present())

    elif option == "3":
        break
    
    else:
        print("Opción no válida")
                