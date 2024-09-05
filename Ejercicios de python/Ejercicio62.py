"""Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""

frase = input("Ingrese una frase: ").lower()
letra = input("Ingrese una letra: ").lower()
cantidad = 0

for i in range(len(frase)):
    if frase[i] == letra:
        cantidad = cantidad + 1
print(f"El número de veces que se repitio la letra: {letra}\nen la frase: {frase}\nes:{cantidad}")