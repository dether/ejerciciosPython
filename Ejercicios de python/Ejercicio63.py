"""Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""

valor = True
while valor:
    eco = str(input(""))
    if eco == "salir":
        valor = False
    else:
        print(eco)