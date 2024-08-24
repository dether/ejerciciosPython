print("Diseñar un algoritmo que calcule el volumen de un cilindro dados su radio y altura (primero el programa deberá verificar si son positivas). ")
#! Volumen = pi * (r*r) * h
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
pi = 3.14159
if (radio > 0) & (altura > 0):
  volumen = pi * (radio*radio) * altura
else:
  volumen = "Los valores de radio y altura, deben ser positivos!"

print("El volumen del cilindro es:", volumen)