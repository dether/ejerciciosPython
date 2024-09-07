"""Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan ingresado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
Ejemplo: "r":5, "%":3, "a":8, "9":1.
¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?"""

strings = ["a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m","q","w","e","r","t","y","u","i","o","p","1","2","3","4","5","6","7","8","9","0","38","a","a","a","l","l","l","e","e","e","hola como estas lalo?","linda"," "]
""" 
for i in range(50):
    string = input(f"Ingrese el caracter {i+1}: ")
    strings.append(string) """

caracteres = []
cantidades = []
alfabeto = []
#ord() función para obtener los valores ASCII de las letras
#chr() para convertir de nuevo a caracteres
for c in range(ord('a'), ord('z') + 1):
    # Creamos una lista que contienen listas de alfabeto y cantidad.
    alfabeto.append([chr(c), 0])

for string in strings:
    for caracter in string:
        if "A" <= caracter <= "Z":
            caracter = chr(ord(caracter) + 32) #Convertirmos en minuscula a travez del codigo ASCII.
        # Verificamos si el caracter es una letra del alfabeto
        if 'a' <= caracter <= 'z':
            # Actualizamos el conteo para el caracter en alfabeto
            for i in range(len(alfabeto)):
                if alfabeto[i][0] == caracter:
                    alfabeto[i][1] += 1
                    break  # Salimos del bucle cuando encontramos el caracter

# Mostrar el conteo de las letras del alfabeto
print("\nOcurrencias de cada letra del alfabeto:")
for letra, cantidad in alfabeto:
    print(f'"{letra}": {cantidad}')