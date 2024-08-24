print("Escribir un programa que convierta un número decimal a binario. ")

numero = int(input("Ingrese un número: "))
binario = ""
while numero > 0:
  div = numero % 2
  binario = str(div) + binario

  numero = int(numero / 2)

print("El número binario es:", binario)
