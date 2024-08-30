"""Hacer un algoritmo que permita ingresar un número hasta el cual se mostrarán los números impares que le anteponían, ejemplo: 
usuario ingresa: 19 
algoritmo muestra: 1,3,5,7,9,11,13,15,17"""

numero = int(input("Ingresa un número: "))
muestra = "algoritmo muestra:"

for i in range(0,numero,1):
    if not i % 2 == 0: 
        muestra = muestra + f" {i}"

        if not i == (numero-2):
            muestra = muestra + f","
        else:
            muestra = muestra + f"."

print(muestra)