"""
Hacer un algoritmo que muestre la tabla de multiplicar de un numero ingresado por el usuario. 
Y que la muestre con el formato: A x B = C
"""

numero = int(input("Ingrese un número para multiplicarlo: "))

for i in range (1,11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")