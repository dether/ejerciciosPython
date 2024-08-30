"""El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

                edad < 45      edad ≥ 45
IMC < 22.0      bajo            medio
IMC ≥ 22.0      medio           alto

El índice de masa corporal (IMC) es el cociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.
"""
peso = float(input("Ingrese su peso: "))
estatura = (float(input("Ingrese su altura: "))**2)
edad = int(input("Ingrese su edad: "))
IMC = peso//estatura

if edad < 45:
    if IMC < 22.0:
        print(f"Su condición de riesgo es: bajo\nIMC: {IMC}")
    else:
        print(f"Su condición de riesgo es: medio\nIMC: {IMC}")
elif edad > 44:
    if IMC < 22.0:
        print(f"Su condición de riesgo es: medio\nIMC: {IMC}")
    else:
        print(f"Su condición de riesgo es: alto\nIMC: {IMC}")

