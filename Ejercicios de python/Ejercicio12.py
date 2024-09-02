import math

"""Escribir un programa que lea el radio de un círculo y a continuación visualice: circunferencia del círculo, área del círculo o diámetro del círculo."""

radio = float(input("Ingrese el radio de un círculo: "))
pi = math.pi
area = pi*(radio**2)
diametro = 2*radio
circunferencia = pi*diametro

print(f"Datos de un círculo: \nRadio: {radio}\nArea: {area:.2f}\nDiametro: {diametro}\nCircunferencia: {circunferencia:.2f}")