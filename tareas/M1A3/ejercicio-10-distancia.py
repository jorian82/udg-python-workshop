"""
    Pida dos coordenadas bidimensionales y en base a ellas calcule la distancia de dichos puntos
"""

import math

x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y1: "))

x= x2-x1
y= y2-y1

print(f"La distancia entre los dos puntos es: {math.sqrt(math.pow(x,2)+math.pow(y,2))}")

print("Fin del programa")
