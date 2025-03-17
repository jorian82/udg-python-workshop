"""
    Dados dos catetos de un triángulo rectángulo, calcule su hipotenusa
    h^2 = a^2 + b^2

"""

import math

a = int(input("Introduzca medida de lado a: "))
b = int(input("introduzca medida de lado b: "))

h = math.pow(a,2) + math.pow(b,2)

print(f"La medida de la hipotenusa es: {math.sqrt(h)}")

print("Fin de programa")
