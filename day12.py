import operation
import random

a,b = map(float, input("Ingrese nos números separados por espacio: ").split())
print(operation.add(a,b))
print(operation.subtract(a,b))
print(random.randint(1,10))