import random

print("Diseñar un algoritmo que genere un número secreto aleatorio entre 1 y 100 (usar numero = Aleatorio(1,100)). El usuario debe tener 7 intentos para adivinarlo. Luego de cada intento se le debe indicar si el número secreto es mayor o menor al ingresado. El usuario gana cuando el número ingresado es igual al secreto. ")

secreto = random.randint(1,100)
numero = 1
intentos = 7

print("Bienvenido al juego del número secreto, tiene",intentos,"intentos para ganar un premio!")

while intentos > 0:
  print("Tiene", intentos,"intentos.")
  numero = int(input("Ingrese un número: "))
  if numero == secreto:
    print("Felicidades ha ganado, el número secreto era:", secreto,"!")
    intentos = 0
  elif numero < secreto:
    intentos = intentos - 1
    if intentos == 0:
      print("Lo siento, te has quedado sin intentos, el número secreto era:",secreto)
    else:
      print("El número secreto es mayor al ingresado. Su número ingresado es:", numero)
  elif numero > secreto:
    intentos = intentos - 1
    if intentos == 0:
      print("Lo siento, te has quedado sin intentos, el número secreto era:",secreto)
    else:
      print("El número secreto es menor al ingresado. Su número ingresado es:", numero)
