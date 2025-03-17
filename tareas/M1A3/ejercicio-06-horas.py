"""
    Dada una cantidad de minutos, calcule cuantas horas y minutos corresponden
"""

minutos = int(input("Ingrese los minutos a convertir: "))

hrs = int(minutos/60)
min = int((minutos-(hrs*60)))

print(f"{minutos} minutos equivalen a {hrs} horas y {min} minutos")

print("Fin de programa")
