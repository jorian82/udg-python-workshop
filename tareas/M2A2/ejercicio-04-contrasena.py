"""
    programa que solicite una contraseña (el texto de la contraseña no es importante) 
    y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de 
    tres peticiones
"""

print("Escriba una contraseña")
contrasena = input("Contraseña: ")
contador = 0
while contador < 3:
    print("Vuelva a escribir la contraseña")
    contrasena2 = input("Contraseña: ")
    if contrasena == contrasena2:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        contador += 1

if contador == 3:
    print("Ha superado el número de intentos permitidos")

