"""Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
Palabra 1: edificio
Palabra 2: tren
La palabra edificio tiene 4 letras mas que tren.
Palabra 1: sol
Palabra 2: paralelepipedo
La palabra paralelepipedo tiene 11 letras mas que sol
Palabra 1: plancha
Palabra 2: lapices
Las dos palabras tienen el mismo largo"""

palabra1 = input("Ingrese la primer palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
diferencia = 0
if len(palabra1) > len(palabra2):
    diferencia = len(palabra1) - len(palabra2)
    print(f"La palabra {palabra1} tiene {diferencia} letras mas que {palabra2}.")
elif len(palabra2) > len(palabra1):
    diferencia = len(palabra2) - len(palabra1)
    print(f"La palabra {palabra2} tiene {diferencia} letras mas que {palabra1}.")
else:
    print("Las dos palabras tienen el mismo largo")