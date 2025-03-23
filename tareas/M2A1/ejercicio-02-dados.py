"""
    Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un 
    dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta 
    al resultado obtenido.
    
    Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
    Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: 
            “ERROR: número incorrecto.”.
"""

# Definimos una función que recibe un número entero y devuelve el número opuesto
def numero_opuesto(numero):
    if numero == 1:
        return 6
    elif numero == 2:
        return 5
    elif numero == 3:
        return 4
    elif numero == 4:
        return 3
    elif numero == 5:
        return 2
    elif numero == 6:
        return 1
    else:
        return
    

# Solicitamos el número al usuario
numero = int(input("Introduce un número del 1 al 6: "))
# Comprobamos si el número introducido
if numero < 1 or numero > 6:
    print("ERROR: número incorrecto.")
else:
    # Mostramos el número opuesto
    print(f"El número opuesto al {numero} es el {numero_opuesto(numero)}")

# Fin del programa