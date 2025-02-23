'''
    pares.py
    Determina si un numero es par o impar
'''


n = int(input("Ingresa un numero: "))

print("El resultado del programa utilizando condicional: \n")

if n % 2 == 0:
    print("El numero {} es par\n".format(n))
else:
    print("El numero {} es impar\n".format(n))    

print("El resultado del programa utilizando operdor ternario: \n")

print("El numero {} es par\n".format(n) if n % 2 == 0 else "El numero {} es impar\n".format(n))

print("Fin del programa")
