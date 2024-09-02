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
divisiones = 1

for i in range(3,numero+2):
    #print(i)
    if i % 2 == 0:
        divisiones = divisiones + (1/i)
        #print(+1/i)
    else:
        divisiones= divisiones - (1/i)
        #print(-1/i)
print(4*divisiones) 
