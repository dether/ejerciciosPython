""" Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no puede ser más largo que la suma de los otros dos.
Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
si acaso el triángulo es inválido; y si no lo es, qué tipo de triángulo es 
    Ingrese a: 3.9
    Ingrese b: 6.0
    Ingrese c: 1.2
    No es un triangulo valido.
    Ingrese a: 1.9
    Ingrese b: 2
    Ingrese c: 2
    El triangulo es isósceles.
    Ingrese a: 3.0
    Ingrese b: 5.0
    Ingrese c: 4.0
    El triangulo es escaleno."""

lado1 = float(input("Ingrese un lado: "))
lado2 = float(input("Ingrese un lado: "))
lado3 = float(input("Ingrese un lado: "))

if ((lado1 + lado2) < lado3) or ((lado2 + lado3) < lado1) or ((lado1 + lado3) < lado2):
    print(lado1 + lado2)
    print("No es un triangulo valido.")
else:
    if lado1 == lado2 and lado2 == lado3:
        print("El triangulo es equilatero.")
    elif (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado1 == lado3 and lado3 != lado2):
        print("El triangulo es isósceles.")
    else:
        print("El triangulo es escaleno.")