"""
Un sistema de ecuaciones lineales:
        a*x + b*y = c
        d*x + e*y = f 
Se puede resolver con las siguientes formulas:
        x = (c*e-b*f)/(a*e-b*d)
        y = (a*f-c*d)/(a*e-b*d)
Diseñar un programa que lea los coeficientes (a, b, c; d, e y f) y muestre los valores de x e y
"""
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))
e = int(input("Ingrese el valor de e: "))
f = int(input("Ingrese el valor de f: "))

x = (c*e-b*f)/(a*e-b*d)
y = (a*f-c*d)/(a*e-b*d)

print(f"El valor de x: {x}")
print(f"El valor de y: {y}")