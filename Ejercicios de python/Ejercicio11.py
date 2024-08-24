import math
print("Escribir un programa que lea las longitudes de los dos lados perpendiculares de un triángulo rectángulo y calcule el área y el perímetro del triangulo. Usar el teorema de Pitágoras para calcular la longitud del tercer lado.")

a = float(input("Ingrese el valor del lado a: "))
b = float(input("Ingrese el valor del lado b: "))
c = math.sqrt((a**2) + (b**2))

perimetro = a + b + c
area = (a * b) / 2

print(f"El área del triángulo rectángulo es: {area}")
print(f"El perímetro del triángulo rectángulo es: {perimetro}")