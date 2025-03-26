"""
    Programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta S o s 
    (en mayúsculas o en minúsculas)
"""

# Mensaje de bienvenida
print("Bienvenido al programa") 
respuesta = "N"

while respuesta != "S" and respuesta != "s":
    print("Quieres terminar el programa?")
    respuesta = input("S/N: ")

print("Has decidido terminar el programa. Hasta la próxima")
