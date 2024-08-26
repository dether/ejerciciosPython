"""Escriba un programa que pida al usuario la entrada correspondiente y calcule el factorial n! de un número entero n≥0, definido como:
n!=1⋅2⋅3⋅⋯⋅n.
Además, se define 0!=1"""
valor = True
factorial = 1
orden = ""
numero = int(input("Ingrese un número: "))

while valor:
  if numero < 1:
    numero = int(input("El número no puede ser negativo o 0. Ingrese un número: "))
  else:
    valor =False

for i in range(1,(numero+1)):
  factorial = factorial * i
  
print(f"El factorial de {numero} es: {factorial}.")