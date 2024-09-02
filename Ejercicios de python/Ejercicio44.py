"""Desarrolle un programa que tenga la siguiente entrada:
     primero, el usuario ingresa un número entero n, que indica cuántas palabras ingresará a continuación; 
     después el usuario ingresa n palabras. 
La salida del programa debe mostrar la palabra más larga y la más corta que fueron ingresadas por el usuario.
Recuerde que la función len entrega el largo de un string:
len('amarillo') -> 8
La ejecución del programa debe verse así:
    Cantidad de palabras: 5
    Palabra 1: negro
    Palabra 2: amarillo
    Palabra 3: naranjo
    Palabra 4: azul
    Palabra 5: blanco
    La palabra mas larga es amarillo
    La palabra mas corta es azul"""

cantidad = int(input("Cantidad de palabras: "))
numeroMayor = -9999
palabraLarga = ""

numeroMenor = 9999
palabraCorta = ""

for i in range(1,cantidad+1):
    palabra= input(f"Palabra {i}: ")
    if len(palabra) > numeroMayor:
        numeroMayor = len(palabra)
        palabraLarga = palabra
    elif len(palabra) < numeroMenor:
        numeroMenor = len(palabra)
        palabraCorta = palabra

print(f"La palabra mas larga es {palabraLarga}")
print(f"La palabra mas corta es {palabraCorta}")
