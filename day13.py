class Student:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career

    def present(self):
        return f"Hola {self.name}, tengo {self.age} años y estudio {self.career}"
    
if __name__ == "__main__":

    student1 = Student("Marco", 21, "Ing de Minas")
    student2 = Student("Mauricio", 19, "Ing Civil")
    print(student1.present())
    print(student2.present())