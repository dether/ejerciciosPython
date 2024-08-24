print("Escribir un programa que compare dos cadenas de caracteres indicando si son iguales o son distintas. Comparar letra por letra.")

cadena1 = (str(input("Ingrese la primer cadena de caracteres: "))).lower()
cadena2 = (str(input("Ingrese la segunda cadena de caracteres: "))).lower()

iguales = True

if len(cadena1) != len(cadena2):
  iguales = False
else:

  for i in range(0, len(cadena1)):
    if cadena1[i] != cadena2[i]:
      iguales = False

if iguales:
  print("Son iguales.")
else:
  print("No son iguales.")
