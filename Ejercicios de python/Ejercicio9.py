"""Escribir un programa para convertir una medida dada en pies a sus equivalentes en: 
a) yardas; 
b) pulgadas; 
c) centímetros 
d) metros 
(1 pie = 12 pulgadas, 
1 yarda = 3 pies, 
1 pulgada = 2.54 centímetros,
1 metro = 100 centímetros). 
Leer el numero de pies e imprimir el número de yardas, pies, pulgadas, centímetros y metros."""

pies = int(input("Ingrese un valor en pies: "))

pulgadas = pies * 12
yardas = pies / 3
centimetro = pulgadas * 2.54
metro = centimetro/100

print(f"pulgadas: {pulgadas} yardas: {yardas:.2f} centimetro: {centimetro} metro: {metro}")