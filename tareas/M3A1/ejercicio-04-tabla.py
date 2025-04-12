"""
    Cree una tabla bidimensional de 5x15
    Llene la tabla con 0 al centro y 1 en los bordes
    Muestre la tabla
"""

"""
    Crea una tabla bidimensional de tamaño filas x columnas.
    
    Args:
        filas (int): Número de filas de la tabla.
        columnas (int): Número de columnas de la tabla.
        
    Returns:
        list: Tabla bidimensional llena de ceros y unos.
"""
def crear_tabla_bidimensional(filas=5, columnas=15):
    # Crear la tabla inicializada con ceros
    tabla = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    # Llenar los bordes con unos
    for i in range(filas):
        for j in range(columnas):
            if i == 0 or i == filas - 1 or j == 0 or j == columnas - 1:
                tabla[i][j] = 1
    
    return tabla


"""
    Muestra la tabla bidimensional en consola.
    
    Args:
        tabla (list): Tabla bidimensional a mostrar.
"""
def mostrar_tabla(tabla):
    for fila in tabla:
        print("".join(str(x) for x in fila))


# Crear la tabla
tabla = crear_tabla_bidimensional()

# Mostrar la tabla
mostrar_tabla(tabla)

"""
    Salida esperada:
    111111111111111
    100000000000001
    100000000000001
    100000000000001
    111111111111111
"""
