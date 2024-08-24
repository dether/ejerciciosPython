print("""Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.
Ingrese caracter: 9
Es numero.
Ingrese caracter: A
Es letra mayúscula.
Ingrese caracter: f
Es letra minúscula.
Ingrese caracter: #
No es letra ni número.""")

desconocido = input("Ingrese un caracter para analizarlo y dar información: ")

if "0" <= desconocido <= "9":
  print("El caracter es un número.")
elif "a" <= desconocido <= "z":
  print("Es letra minúscula. ")
elif "A" <= desconocido <= "Z":
  print("Es letra mayuscula.")
else:
  print("El caracter no es un número y una cadena.")