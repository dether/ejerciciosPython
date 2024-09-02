"""Así como hay números palíndromos, también hay palabras palíndromas, que son las que no cambian al invertir el orden de sus letras.
Por ejemplo, «reconocer», «Neuquén» y «acurruca» son palíndromos.
    1. Escriba un programa que reciba como entrada una palabra e indique si es palíndromo o no. 
    Para simplificar, suponga que la palabra no tiene acentos y todas sus letras son minúsculas:
    
    Ingrese palabra: sometemos
    Es palindromo
    
    Ingrese palabra: rascar
    No es palindromo

    2. Modifique su programa para que reconozca oraciones palíndromas. La dificultad radica en que hay que ignorar los espacios:

    Ingrese oracion: dabale arroz a la zorra el abad
    Es palindromo

    Ingrese oracion: eva usaba rimel y le miraba suave
    Es palindromo

    Ingrese oracion: puro chile es tu cielo azulado
    No es palindromo"""

oracion = input("Ingrese una oracion: ")
oracion = oracion.lower()
reverseSinEspacio = ""
palabraSinEspacio = ""
for i in range(len(oracion)):

    if (oracion[i] != " "):
        reverseSinEspacio = oracion[i] + reverseSinEspacio
        palabraSinEspacio = palabraSinEspacio + oracion[i]

if reverseSinEspacio == palabraSinEspacio:
    print("Es palindromo")
else:
    print("No es palindromo")




""" palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
reverse = ""
for i in range(len(palabra)):
    reverse = palabra[i] + reverse

if reverse == palabra:
    print("Es palindromo")
else:
    print("No es palindromo") """