"""Según el teorema de Pitágoras, la relación entre los lados (a, b) de un triángulo rectángulo y la hipotenusa (h) viene dada por la fórmula.       
      a**2 + b**2 = h**2 
Escribir un programa que lea la longitud de los lados y calcule la hipotenusa"""
import math

a = float(input("Ingrese el valor del lado a: "))
b = float(input("Ingrese el valor del lado b: "))

h = math.sqrt((a**2) + (b**2))

print(f"La hipotenusa según el Teorema de Pitágoras es: {h:.4f}")