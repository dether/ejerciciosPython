print("Diseñar un algoritmo que permita ingresar 10 números y luego muestre cuantos son; pares, impares, negativos, positivos, pares y positivos, impares y positivos, nulos. ")

positivos = 0
negativos = 0
pares = 0
paresPositivos = 0
impares = 0
imparesPositivos = 0
nulos = 0

for i in range(10):
  num = int(input("Ingrese un numero: "))
  if num % 2 == 0:
    pares = pares + 1
    if num > 0:
      positivos = positivos + 1
      paresPositivos = paresPositivos + 1
    elif num < 0:
      negativos = negativos + 1
    else:
      nulos = nulos + 1

  else:
    impares = impares + 1
    if num > 0:
      positivos = positivos + 1
      imparesPositivos = imparesPositivos + 1
    elif num < 0:
      negativos = negativos + 1
    else:
      nulos = nulos + 1

print("La cantidad total de números positivos:", positivos)
print("La cantidad total de números negativos:", negativos)
print("La cantidad total de números nulos:", nulos)
print("La cantidad total de números pares:", pares)
print("La cantidad total de números impares:", impares)
print("La cantidad total de números pares y positvos:", paresPositivos)
print("La cantidad total de números impares y positivos:", imparesPositivos)
