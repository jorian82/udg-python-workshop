"""
    Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día 
    correspondiente. Si introducimos otro número nos da un error.
"""

# Definimos una función que recibe un número entero y devuelve el día de la semana
def dia_semana(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return
    
# Solicitamos el número al usuario
numero = int(input("Introduce un número del 1 al 7: "))
# Comprobamos el número introducido
if numero < 1 or numero > 7:
    print("ERROR: número incorrecto.")
else:
    # Mostramos el día de la semana
    print(f"El día de la semana correspondiente al {numero} es el {dia_semana(numero)}")

# Fin del programa
