"""1. Generador de cubos

Escribe un programa de Python que cree una función generadora que produzca cubos de números del 1 al n. Acepte n del usuario."""

def generadorCubos(n):
    for i in range(1, n + 1):
        yield i ** 3  # usamos yield para devolver uno por uno

# Pedimos n al usuario
n = int(input("Ingrese un número: "))

# Recorremos el generador
for cubo in generadorCubos(n):
    print(cubo)


"""2. Generador de números aleatorios

Escriba un programa de Python para implementar un generador que genere números aleatorios dentro de un rango dado."""

import random

def generadorAleatorio(inicio, fin, cantidad):
    for i in range(cantidad):
        yield random.randint(inicio, fin)

# Pedimos los datos al usuario
inicio = int(input("Número inicial del rango: "))
fin = int(input("Número final del rango: "))
cantidad = int(input("Cuántos números aleatorios generar: "))

for numero in generadorAleatorio(inicio, fin, cantidad):
    print(numero)


"""3. Generador principal (rango)

Escribe un programa de Python que cree una función generadora que genere todos los números primos entre dos números dados."""

def numerosPrimos(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def generarPrimos(desde, hasta):
    for num in range(desde, hasta + 1):
        if numerosPrimos(num):
            yield num

# Entrada de usuario
desde = int(input("Desde qué número: "))
hasta = int(input("Hasta qué número: "))

for primo in generarPrimos(desde, hasta):
    print(primo)
