"""Hacer un algoritmo que pida 10 números y luego indique cuantos fueron pares y cuantos impares. """

pares = 0
impares = 0
for i in range(1,11):
    numero = int(input(f"Ingresa el {i}° número: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(f"Ingresaste {pares} números pares y {impares} números impares.")