"""
    Genere 10 numeros aleatorios y los ordene de menor a mayor.
    Muestre la lista ordenada y la lista original. 
"""

import random

"""
    Genera una lista de números aleatorios y los ordena de menor a mayor.
    
    Args:
        cantidad (int): Número de elementos en la lista.
        rango (tuple): Rango de los números aleatorios.
        
    Returns:
        tuple: Lista original y lista ordenada.
"""
def ordenar_numeros_aleatorios(cantidad=10, rango=(0, 100)):
    # Generar lista de números aleatorios
    numeros_aleatorios = [random.randint(rango[0], rango[1]) for _ in range(cantidad)]
    
    # Ordenar la lista
    numeros_ordenados = sorted(numeros_aleatorios)
    
    return numeros_aleatorios, numeros_ordenados


# Llamar a la función y obtener las listas
numeros_originales, numeros_ordenados = ordenar_numeros_aleatorios()

# Mostrar resultados
print("Lista original:", numeros_originales)
print("Lista ordenada:", numeros_ordenados)
