"""
    Lea 5 calificaciones de un alumno (entre 0 y 10). Muestre todas las notas, la media, la más alta y la más baja.
"""

# Solicitar al usuario que ingrese 5 calificaciones
calificaciones = []

for i in range(5):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación {i + 1} (entre 0 y 10): "))
            if 0 <= calificacion <= 10:
                calificaciones.append(calificacion)
                break
            else:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


# Calcular la media
media = sum(calificaciones) / len(calificaciones)

# Calcular la calificación más alta
max_calificacion = max(calificaciones)

# Calcular la calificación más baja
min_calificacion = min(calificaciones)

# Mostrar resultados
print("Calificaciones:", calificaciones)
print("Media:", media)
print("Calificación más alta:", max_calificacion)
print("Calificación más baja:", min_calificacion)
