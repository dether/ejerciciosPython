print("Escribir un programa que pida primero un carácter por teclado y que luego pida una cadena de caracteres (una palabra o una frase). El programa debe contar cuantas veces aparece el carácter en la cadena.")

caracter = str(input("Ingrese un carácter: "))
cadena = str(input("Ingrese una cadena de caracteres: "))
contador = 0

for i in range(0, len(cadena)):
  if cadena[i] == caracter:
    contador = contador + 1
print("La letra:",caracter)
print("Aparece en la cadena:", cadena)
print(contador, "veces.")
