print("Crear un algoritmo que calcule si dos números son divisibles. Para ello, se piden un primer numero y un segundo numero, entonces mostrar un cartel que diga “es divisible” si el segundo numero es divisible al primero. ")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num2 % num1 == 0:
  print("Es divisible.")
else:
  print("No es divisible.")