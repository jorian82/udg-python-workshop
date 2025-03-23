"""
    Se quiere calcular el costo de un viaje en autobus para un determinado numero de personas.
    El costo es de $65 por persona si el numero de personas es mayor a 100, de $70 por persona 
    si el numero de personas es 50 a 99, de $95 si son de 30 a 49 y para menos de 30 personas 
    el costo del autobus es 4000
"""
costo = 0
total = 0
autobus = 4000
personas = int(input("Ingresa el numero de personas: "))

MENSAJE = "El costo del viaje por persona es de: ${}"

if personas > 99:
    costo = 65
elif personas > 49 and personas < 100:
    costo = 70
elif personas > 29 and personas < 50:
    costo = 95
elif personas < 30 and personas > 0:
    costo = autobus/personas
else:
    print("No hay viaje")
    
if personas > 0:
    total = personas * costo
    print(MENSAJE.format(costo))
    print("Pago a compania de autobuses: ${}".format(autobus))
    print("El costo total del viaje es de: ${}".format(total))

print("Fin del programa")