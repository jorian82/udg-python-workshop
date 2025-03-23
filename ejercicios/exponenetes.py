'''
    Recibe una base y un exponente y calcula la potencia
'''

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

MENSAJE = "El resultado es: {}"

if exponente < 0:
    print(MENSAJE.format(1/base**(exponente * -1)))
elif exponente > 0:
    print(MENSAJE.format(base**exponente))
else:
    print(MENSAJE.format(1))

print("Fin del programa")
