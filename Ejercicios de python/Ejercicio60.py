"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

contraseña = "asdasd123"

valor = True
while valor:
    intento = input("Ingrese de nuevo su contraseña: ")
    if contraseña != intento:
        print("La contraseña ingresada es incorrecta.")
        print("Ingrese su contraseña de nuevo: ")
    else:
        valor = False
        print("La contraseña ingresada es correcta.")


