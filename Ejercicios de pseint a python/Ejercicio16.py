import random
print("Diseñar un algoritmo que imprima con un cartel el numero de docena ( primera , segunda o tercera ) dado el resultado de una jugada de ruleta (del 0 al 36). ")

numero = random.randint(0, 36)

if numero == 0:
  print("El número es 0 y no pertenece a ninguna docena.")
elif 1 <= numero <= 12:
  print("El número es",numero,"y pertenece a la primer docena.")
elif 13 <= numero <= 24:
  print("El número es",numero,"y pertenece a la segunda docena.")
else:
  print("El número es", numero, "y pertenece a la tercera docena.")