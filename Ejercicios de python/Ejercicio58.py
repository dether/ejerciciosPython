"""Escribir un programa que pregunte el correo electrónico del usuario y lo valide (debe tener @)."""
correo = input("Ingrese su correo electronico: ")
tieneArroba = False
tienePunto = False
for i in range(len(correo)):
    if correo[i] == "@":
        tieneArroba = True
    # Verificamos si hay un punto después de la primera aparición del arroba
    if tieneArroba and correo[i] == ".":
        tienePunto = True

if tieneArroba and tienePunto:
    print(f"Tu correo ingresado: {correo} cumple con las validaciones.")
else:
    print(f"El correo ingresado: {correo} no cumple con las validaciones.")