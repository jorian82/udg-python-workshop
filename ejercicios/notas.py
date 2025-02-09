'''
    Notas 
    
    Recibe una nota del usiario y de acuerdo a su valor muestra si es:
    9 o 10 sobresaliente, 
    8 notable, 
    6 o 7 bien, 
    5 suficiente, 
    4, 3, 2, 1 suspendido
    otro valor imprime "Nota incorrecta"
'''
nota = int(input("Ingresa tu nota: "))

if nota>8 and nota<11:
    print("Sobresaliente")
elif nota == 8:
    print("Notable")
elif nota == 6 or nota == 7:
    print("Bien")
elif nota == 5:
    print("Suficiente")
elif nota>0 and nota<5:
    print("Suspendido")
else:
    print("Nota incorrecta")

print("Fin del programa")
