from random import randrange
""" Escriba un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine.
El programa puede obtener un número al azar entre 0 y 100 de la siguiente manera (¡haga la prueba!):
    >>> from random import randrange
    >>> n = randrange(101)
    >>> print n
    72

El usuario debe ingresar su intento, y el programa debe decir si el número pensado es mayor, menor, o el correcto:
    Adivine el numero.
    Intento 1: 32
    Es mayor que 32
    Intento 2: 80
    Es menor que 80
    Intento 3: 70
    Es mayor que 70
    Intento 4: 72
    Correcto. Adivinaste en 4 intentos.

Una vez que complete ese ejercicio, es hora de invertir los roles: ahora usted pensará un número y el computador lo adivinará.
Escriba un programa que intente adivinar el número pensado por el usuario. Cada vez que el computador haga un intento, el usuario debe ingresar <, > o =, dependiendo si el intento es menor, mayor o correcto.
La estrategia que debe seguir el programa es recordar siempre cuáles son el menor y el mayor valor posibles, y siempre probar con el valor que está en la mitad. Por ejemplo, si usted piensa el número 82, y no hace trampa al jugar, la ejecución del programa se verá así:
    Intento 1: 50
    >
    Intento 2: 75
    >
    Intento 3: 88
    <
    Intento 4: 81
    >
    Intento 5: 84
    <
    Intento 6: 82
    =
    Adivine en 6 intentos"""
#!Que adivine la maquina 3>:)

minimo = 0
maximo = 100
contador = 0
valor = False

while not valor:
    numero = (minimo + maximo) // 2
    contador = contador + 1
    print(f"Intento {contador}: {numero}")

    respuesta = input(" ")

    if respuesta == "=":
        valor = True
        print(f"Adivine en {contador} intentos.")

    elif respuesta == "<":
        maximo = numero - 1

    elif respuesta == ">":
        minimo = numero + 1

    else:
        print("Respuesta no válida. Por favor, ingresa '<', '>' o '='.")

    

#?que adivine el usuario.
""" numeroSecreto = randrange(101)
valor = True
print("Adivine el número.")
numero = 1
contador = 1
while valor:
    numero = int(input(f"Intento {contador}: "))
    if (numero < 0 or numero > 100):
        print("Número invalido. Ingrese un número del 0 al 100.")
    else:
        if numero == numeroSecreto:
            valor = False
            print(f"Correcto. Adivinaste en {contador} intentos.")
        elif numero < numeroSecreto:
            contador = contador + 1
            print(f"Es mayor que {numero}")
        elif numero > numeroSecreto:
            contador = contador + 1
            print(f"Es menor que {numero}") """
