print("Crear un programa que pida una cadena de caracteres (una frase) y devuelva la misma cadena pero sin espacios.")

cadena = str(input("Ingrese una cadena de caracteres: "))
sinEspacio = ""
for i in range (0, len(cadena)):
  if cadena[i] != " ":
    sinEspacio = sinEspacio + cadena[i]

print(sinEspacio)