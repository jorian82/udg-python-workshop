"""
    Escribe un programa que pida un número entero entre uno y doce e imprima el número 
    de días que tiene el mes correspondiente.
"""

# Definimos una función que recibe un número entero y devuelve el número de días del mes
def dias_mes(numero):
    if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 8 or numero == 10 or numero == 12:
        return 31
    elif numero == 2:
        return 28
    elif numero == 4 or numero == 6 or numero == 9 or numero == 11:
        return 30
    else:
        return


# Solicitamos el número al usuario
numero = int(input("Introduce un número del 1 al 12: "))
# Comprobamos el número introducido
if numero < 1 or numero > 12:
    print("ERROR: número incorrecto.")
else:
    # Mostramos el número de días del mes
    print(f"El mes {numero} tiene {dias_mes(numero)} días")