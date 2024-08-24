print("Escribir un programa que convierta un número ingresado de segundos en el equivalente de minutos y segundos.")

segundos = int(input("Ingrese un número: "))
minutos = 0
time = True
while time:
  if segundos > 59:
    minutos = minutos + 1
    segundos = segundos - 60
  else:
    time = False

print(f"Equivalencia de minutos y segundos: {minutos} minutos y {segundos} segundos.")