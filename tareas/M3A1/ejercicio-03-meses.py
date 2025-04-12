"""
    Solicite un número de mes (1-12) y muestre el nombre del mes correspondiente y el número de días que tiene.
"""


"""
    Devuelve el nombre del mes y el número de días en ese mes.
    
    Args:
        mes (int): Número del mes (1-12).
        
    Returns:
        tuple: Nombre del mes y número de días.
"""
def obtener_mes_y_dias(mes):
    meses = {
        1: ("Enero", 31),
        2: ("Febrero", 28),  # Considerando años no bisiestos
        3: ("Marzo", 31),
        4: ("Abril", 30),
        5: ("Mayo", 31),
        6: ("Junio", 30),
        7: ("Julio", 31),
        8: ("Agosto", 31),
        9: ("Septiembre", 30),
        10: ("Octubre", 31),
        11: ("Noviembre", 30),
        12: ("Diciembre", 31)
    }
    
    return meses.get(mes, ("Mes inválido", None))


# Solicitar al usuario que ingrese un número de mes
while True:
    try:
        mes = int(input("Ingrese el número del mes (1-12): "))
        if 1 <= mes <= 12:
            break
        else:
            print("El número del mes debe estar entre 1 y 12.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

# Obtener el nombre del mes y el número de días
mes_nombre, dias = obtener_mes_y_dias(mes)

# Mostrar resultados
print(f"El mes es {mes_nombre} y tiene {dias} días.")
