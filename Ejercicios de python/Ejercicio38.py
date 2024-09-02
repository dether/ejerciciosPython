"""La secuencia de Collatz de un número entero se construye de la siguiente forma:
     si el número es par, se lo divide por dos; 
     si es impar, se le multiplica tres y se le suma uno; 
     la sucesión termina al llegar a uno. 
La conjetura de Collatz afirma que, al partir desde cualquier número, la secuencia siempre llegará a 1. A pesar de ser una afirmación a simple vista muy simple, no se ha podido demostrar si es cierta o no.
Usando computadores, se ha verificado que la sucesión efectivamente llega a 1 partiendo desde cualquier número natural menor que 258.

Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
    n: 18
    18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
    n: 19
    19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
    n: 20
    20 10 5 16 8 4 2 1"""

numero = int(input("Ingrese un número: "))

""" si el número es par, se lo divide por dos; 
     si es impar, se le multiplica tres y se le suma uno; 
     la sucesión termina al llegar a uno.  """

while numero > 1:
    print(numero, end=" ")
    if numero % 2 == 0:
        numero = int(numero / 2)
    else:
        numero = (numero * 3) + 1
#estuve 45 minutos renegando por el 1 de abajo xd
print(1)
