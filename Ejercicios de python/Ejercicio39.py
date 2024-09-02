""" Escriba un programa que muestre los números naturales menores o iguales que un número n determinado, que no sean múltiplos ni de 3 ni de 7.
    Ingrese numero: 24
    1
    2
    4
    5
    8
    10
    11
    13
    16
    17
    19
    20
    22
    23 """

numero = int(input("Ingrese un número: "))
for i in range(1,numero+1):
    if (not(i % 3 == 0)and not( i % 7 == 0)):
        print(i, end=" ")