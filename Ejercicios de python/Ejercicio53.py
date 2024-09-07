"""Los números de Fibonacci F k son una sucesión de números naturales definidos de la siguiente manera:
    F0F1Fk=0,=1,=Fk-1+Fk-2,cuando k≥2.
En palabras simples, la sucesión de Fibonacci comienza con 0 y 1, y los siguientes términos siempre son la suma de los dos anteriores.
En la siguiente tabla, podemos ver los números de Fibonacci desde el 0-ésimo hasta el duodécimo.
    n   |0  |1  |2  |3   |4  |5  |6 |7   |8 |9  |10 |11 |12 |...|
    Fn  |0  |1  |1  |2  |3  |5  |8  |13 |21 |34 |55 |89 |144|...|

a. Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-ésimo número de Fibonacci:

    Ingrese n: 11
    F11 = 89

b.Escriba un programa que reciba como entrada un número entero e indique si es o no un número de Fibonacci:

    Ingrese un numero: 34
    34 es numero de Fibonacci
    Ingrese un numero: 78
    78 no es numero de Fibonacci

c. Escriba un programa que muestre los m primeros números de Fibonacci, donde m es un número ingresado por el usuario:

    Ingrese m: 7
    Los 7 primeros numeros de Fibonacci son:
    0 1 1 2 3 5 8"""
#!a
n = int(input("Ingrese n: "))

a, b = 0, 1
# no vamos a usar una variable de iteración
for _ in range(n):
    a, b = b, a + b
print(f"F{n} = {a}")
#!-----------------------------------------------
#?b
numero = int(input("Ingrese un numero: "))

a, b = 0, 1
valor = False

while a <= numero:
    if a == numero:
        valor = True
    a, b = b, a + b
if valor:
    print(f"{numero} es número de Fibonacci")
else:
    print(f"{numero} no es número de Fibonacci")
#?----------------------------------------------------------------
#!c
numero = int(input("Ingrese m: "))

a, b = 0, 1
print(f"Los {numero} primeros números de Fibonacci son:")

for _ in range(numero):
    print(a, end=" ")
    a, b = b, a + b
