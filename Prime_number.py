def nombre_premier(nombre):
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True

print(nombre_premier(1))
print(nombre_premier(2))
print(nombre_premier(3))
print(nombre_premier(4))
print(nombre_premier(5))
print(nombre_premier(6))
print(nombre_premier(7))
print(nombre_premier(8))
print(nombre_premier(9))
 


Run:
True
True
True
False
True
False
True
False
False
