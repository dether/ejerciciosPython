"""Escribir un programa que pregunte el nombre completo del usuario y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con  todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

nombre = input("Ingrese su nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title()) #.capitalize() solo funciona con la primer letra "A"