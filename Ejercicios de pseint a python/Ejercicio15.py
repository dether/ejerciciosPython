print("Realice un algoritmo que indique si un triangulo es escaleno , equilátero o isósceles ingresando sus lados. ")
# 3 lados iguales = escaleno
# 2 lados iguales = isósceles
# 3 lados desiguales = equilátero

lado1 = float(input("Ingrese la medida del primer lado: "))
lado2 = float(input("Ingrese la medida del segundo lado: "))
lado3 = float(input("Ingrese la medida del tercer lado: "))

if (lado1 == lado2) & (lado2 == lado3):
  print("El triángulo es Escaleno")
elif (lado1 == lado2) | (lado1 == lado3) | (lado2 == lado3):
  print("El triángulo es Isósceles")
else:
  print("El triángulo es Equilátero")