"""Escriba un programa que permita determinar el número mayor perteneciente a un conjunto de n números, donde tanto el valor de n como el de los números deben ser ingresados por el usuario.
    Ingrese n: 4
    Ingrese número: 23
    Ingrese número: -34
    Ingrese número: 0
    Ingrese número: 1
    El mayor es 23"""

cantidad = int(input("Ingrese la cantidad de números que va a ingresar: "))
numero = 0
mayor = numero

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero > mayor:
        mayor = numero

print(f"El mayor es {mayor}")