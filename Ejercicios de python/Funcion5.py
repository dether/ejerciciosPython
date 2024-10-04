"""Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro."""
import math
pi = math.pi
#area = π * r²    perimetro = 2 * π * r

def calcularCircunferencia (radio):
    area = pi * radio * radio
    perimetro = 2 * pi * radio
    print (f"El area de la circunferencia es {area:.2f}.\nEl perimetro de la circunferencia es {perimetro:.2f}")

def pedirRadio():
    while True:
        try:
            radio = float(input("Ingrese el valor del radio: "))
            if (type(radio) == int or type(radio) == float):
                if radio < 0:
                    print("El radio de una circunferencia no puede ser negativo.")
                else:
                    return calcularCircunferencia(radio)
        except:
            print("El valor ingresado es invalido, por favor ingrese un número.")
            continue

pedirRadio()