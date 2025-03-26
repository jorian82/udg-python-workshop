"""
    programa que simule una alcancía. El programa solicitará primero una cantidad, que será la 
    cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra 
    vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al 
    objetivo. El programa comprobará que las cantidades sean positivas.
"""

ahorro = int(input("Introduzca el monto total a ahorrar: "))
total = 0
while total < ahorro:
    cantidad = int(input("Introduzca la cantidad a ahorrar: "))
    if cantidad > 0:
        total += cantidad
    else:
        print("La cantidad a ahorrar debe ser positiva")

print(f"Total ahorrado: {total}")
print(f"Objetivo: {ahorro}")
