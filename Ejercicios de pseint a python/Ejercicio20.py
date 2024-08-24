print("Escriba un programa que entregue todos los divisores de un número entero ingresado: Ingrese numero: 200 ")
#1 2 4 5 8 10 20 25 40 50 100 200

numero = int(input("Ingrese un número entero para encontrar sus divisores: "))
divisores = []

for i in numero:
  if numero % i == 0:
    divisores.append(numero)
    print("i: ", i)

print("divisores: ",divisores)