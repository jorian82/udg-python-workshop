"""
    Pida al usuario crear una lista de palabras y al finalizar
    Permita que seleccione una opción de una lista
    1. Contar palabras
    2. Modificar palabra, modifica todas las ocurrencias de una palabra
    3. Eliminar palabra, elimina todas las ocurrencias de una palabra
    4. Mostrar palabras, muestra todas las palabras
    5. Salir

    Si elige una opcion inválida, muestre un mensaje de error y vuelva a mostrar el menú.
    Si elige salir, muestre un mensaje de despedida.
"""


"""
    Muestra el menú de opciones al usuario.
"""
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Contar palabras")
    print("2. Modificar palabra")
    print("3. Eliminar palabra")
    print("4. Mostrar palabras")
    print("5. Salir")


"""
    Cuenta el número de palabras en la lista.

    Args:
        palabras (list): Lista de palabras.
        
    Returns:
        int: Número de palabras en la lista.
"""
def contar_palabras(palabras):
    return len(palabras)


"""
    Modifica todas las ocurrencias de una palabra en la lista.
    
    Args:
        palabras (list): Lista de palabras.
        palabra_original (str): Palabra a modificar.
        palabra_nueva (str): Nueva palabra.
        
    Returns:
        list: Lista de palabras modificada.
"""
def modificar_palabra(palabras, original, nueva):
    return [nueva if palabra == original else palabra for palabra in palabras]


"""
    Elimina todas las ocurrencias de una palabra en la lista.

    Args:
        palabras (list): Lista de palabras.
        palabra (str): Palabra a eliminar.
        
    Returns:
        list: Lista de palabras modificada.
"""
def eliminar_palabra(palabras, palabra):
    return [p for p in palabras if p != palabra]


"""
    Muestra todas las palabras en la lista.

    Args:
        palabras (list): Lista de palabras.
"""
def mostrar_palabras(palabras):
    print("Palabras:", ", ".join(palabras))


palabras = []

# Solicitar al usuario que ingrese palabras
print("Ingrese palabras (escriba 'fin' para terminar):")
while True:
    palabra = input("Palabra: ")
    if palabra.lower() == 'fin':
        break
    palabras.append(palabra)

# Mostrar el menú y procesar las opciones
while True:
    mostrar_menu()
    opcion = input("Opción: ")
    
    if opcion == '1':
        print("Número de palabras:", contar_palabras(palabras))
    elif opcion == '2':
        original = input("Ingrese la palabra a modificar: ")
        nueva = input("Ingrese la nueva palabra: ")
        palabras = modificar_palabra(palabras, original, nueva)
        print(f"Palabra '{original}' modificada a '{nueva}'.")
    elif opcion == '3':
        eliminar = input("Ingrese la palabra a eliminar: ")
        palabras = eliminar_palabra(palabras, eliminar)
        print(f"Palabra '{eliminar}' eliminada.")
    elif opcion == '4':
        mostrar_palabras(palabras)
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

