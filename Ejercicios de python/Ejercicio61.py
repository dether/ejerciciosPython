"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

import math

def esPrimo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(math.isqrt(numero)) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Ingrese un numero entero: "))

if esPrimo(numero):
    print(f"El {numero} es primo.")
else:
    print(f"El {numero} no es primo.")