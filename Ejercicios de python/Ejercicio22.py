"""Hacer un algoritmo que permita ingresar N números y que luego calcule la suma y el promedio de los números ingresados."""
numero = 1
total = 0
cantidad = 0

while numero != 0:
  numero = int(input("Para finalizar programa ingrese 0.\nIngrese un número: "))
  if numero != 0:
    total = total + numero
    cantidad = cantidad + 1

promedio = total/cantidad
print(f"La suma de los números ingresados es: {total}, y el promedio: {promedio}")