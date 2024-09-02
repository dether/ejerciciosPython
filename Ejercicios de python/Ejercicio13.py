"""Hacer un algoritmo que calcule la superficie y el volumen de un prisma rectangular ortogonal, pidiendo al usuario los datos que son necesarios para calcularlos"""

a = float(input("Ingrese la longitud del prisma rectángular: "))
b = float(input("Ingrese el ancho del prisma rectángular: "))
c = float(input("Ingrese la altura del prisma rectángular: "))

superficie = 2*(a*b + a*c + b*c)
volumen = a * b * c

print(f"La superficie del prisma rectángular: {superficie} \nEl volumen del prisma rectángular: {volumen}")