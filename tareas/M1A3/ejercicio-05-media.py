"""
    Dados 3 numeros, calcule la media. 
    Una variante de éste programa puede ser preguntar primero una cantidad de datos a introducir, 
    de éstaforma el programa será dinámico y permitirá calcular la media de cualquier serie de datos
"""
datos = []

for n in range(3):
    datos.append(int(input("Ingrese número: ")))

media=0

for n in datos:
    media += n

print(f"La media es: {media/3}")

print("Fin de programa")
