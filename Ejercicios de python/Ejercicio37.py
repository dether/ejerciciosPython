import math
"""Desarrolle un programa para estimar el valor de π usando la siguiente suma infinita:

    Serie de Leibniz para π
    π=4*(1−1/3+1/5−1/7+…)
*El denominador aumenta en numeros impares de 1,3,5,7,9 y asi sucesivamente.
*Si ingresas n: 3, la fórmula se calcula usando los primeros 3 términos de la serie:

    π = 4*(1-(1/3)+(1/5)) = 3.466666666666667

La entrada del programa debe ser un número entero que indique cuántos términos de la suma se utilizará.
    n: 3
    3.466666666666667
    n: 1000
    3.140592653839794"""

numero = int(input("Ingrese un número: "))
suma = 1
valor = True #Bandera
for i in range(3,numero*2,2):
    #print(f"i: {(1+i)/2}")
    #Siempre va a ingresar en la primer condición y 
    if valor:
        #print(f"suma = {suma} - 1/{i} ")
        suma = suma - (1/i)
        valor = False 
        #print(f"suma = {suma}")
    else:
        #print(f"suma = {suma} + 1/{i} ")
        suma = suma + (1/i)
        valor = True
        #print(f"suma = {suma}")

#print(f"suma = {suma} * 4 = {4*suma}")
print(f"El valor de pi es: {suma*4}")

