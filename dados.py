import os
from random import randint

def dado():
    dado_uno = randint (1, 6)
    dado_dos = randint (1, 6)
    suma = dado_uno + dado_dos
    sumatotal = 0
    return [dado_uno, dado_dos, suma]

suma_total = []
cont_pares = 0
cont_impares = 0
os.system("cls")

lanzamientos=int(input("::: Introducir el numero de lanzamientos: "))
i = 1
if (lanzamientos>=1):
    while i <= lanzamientos :
        print("-----------------------------------")
        print("Lanzamiento Número: ", i)
        dd = dado()
        suma_total.append(dd[2])
        print("-----------------------------------")
        print("El primer dado ha caido en: ", dd[0])
        print("-----------------------------------")
        print("El primer dado ha caido en: ", dd[1])

        print("===================================")
        print("La suma de los dados es: ", dd[2])
        print("===================================")
        i = i + 1
        if dd[2] % 2 == 0:
            cont_pares +=1
        else:
            cont_impares +=1
        
        key = input("::: Lanzar nuevamente :::")
        print("la suma total es: ", sum(suma_total))
        print(f"La cantidad de pares es: {cont_pares}")
        print(f"La cantidad de impares es: {cont_impares}")
        if(dd[0] and dd[1]==6):
           print("El resultado es un par de 6, el juego finalizo")
           break 

else:
    print("El juego finalizo")
