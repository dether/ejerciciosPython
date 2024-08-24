print("Escribir un programa que muestre los números primos que hay entre 1 y 100. ")

primos = []

for i in range(2,101):
  primo = True;
  # Verificamos hasta la raíz cuadrada de i
  for divisor in range(2, int(i**0.5) + 1):
    # Si hay un divisor, i no es primo!
    if i % divisor == 0: 
      primo = False

  if primo:
    primos.append(i)

print(primos)