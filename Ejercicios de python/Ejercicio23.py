"""Hacer un algoritmo que analice si en dos números ingresados: cual es mayor, cual es menor, o si son iguales."""

num1 = float(input("Ingrese el primer número: "))
num2 =float(input("Ingrese el segundo número para compararlo: "))

if num1 > num2:
  print(f"El primer número {num1} es mayor que el segundo número {num2} que resulta ser el menor. No son iguales.")
elif num2 > num1:
  print(f"El segundo número {num2} es mayor que el primer número {num1} que resulta ser el menor. No son iguales.")
else:
  print(f"Son iguales.")
