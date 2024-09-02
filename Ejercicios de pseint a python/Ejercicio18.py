import math
"""Crear un algoritmo que muestre las raices de una ecuación cuadrática del tipo  P( x) = ax2 + bx + c = 0 (usando Bhaskara) ,a partir del ingreso de los valores de los coeficientes del polinomio. Puede tener dos soluciones posibles (x1 y x2, cuando b 2 -4ac es mayor a 0), una solución (x1, cuando b 2 - 4ac es igual a 0) o no tener solución en los reales (cuando b 2 -4ac es menor a 0). Probar con: a) P(x) = x2+3x+2 Respuesta: Tiene dos raíces x1 = -2 y x2 = -1 b) P(x) = 2 x2 +4x+2 Respuesta: Tiene una raíz x = -1 c) P(x) = 3 x2+2 Respuesta: No tiene solución en los Reales """

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
discriminante = b * b - 4 * a * c
x1 = 0
x2 = 0

if discriminante > 0:
  x1 = (-b - math.sqrt(discriminante)) / (2 * a)
  x2 = (-b + math.sqrt(discriminante)) / (2 * a)
  print("Dos soluciones:")
  print("x1 =",x1," x2 =",x2)
elif discriminante == 0:
  x1 = (-b + math.sqrt(discriminante)) / (2 * a)
  x2 = (-b - math.sqrt(discriminante)) / (2 * a)
  print("Una solución")
  print("x =",x2)
else:
  print("No tiene solución en los reales")
