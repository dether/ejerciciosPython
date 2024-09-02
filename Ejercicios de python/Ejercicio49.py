"""Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda (capicúa). Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
Escriba un programa que indique si el número ingresado es o no palíndromo:

    Ingrese un numero: 14941
    14941 es palindromo

    Ingrese un numero: 81924
    81924 no es palindromo"""

numero = input("Ingrese un número: ")
reverse = ""
for i in range(len(numero)):
    reverse = numero[i] + reverse

if reverse == numero:
    print(f"{numero} es palindromo")
else:
    print(f"{numero} no es palindromo")
