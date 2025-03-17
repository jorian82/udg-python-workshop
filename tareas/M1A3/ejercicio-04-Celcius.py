"""
    Dada una temperatura en grados Fahrenheit convertirla a grados Celcius
    F=(9*C)/5 + 32C
    C=F-32 * (5/9)
"""

F = int(input("Introduzca la temperatura: "))

print(f"La temperatura {F}ºF en ºC es: {(F-32)*(5/9)}")

print("Fin del programa")
