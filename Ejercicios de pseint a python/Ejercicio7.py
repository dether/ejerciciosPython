print("Diseñe un algoritmo para ingresar dos palabras y luego las muestre en orden alfabético. ")
palabra1 = str(input("Ingrese la primer palabra para ordenarla alfabeticamente: "))
palabra2 = str(input("Ingrese la segunda palabra para ordenarla alfabeticamente: "))
if palabra1 < palabra2:
  print(palabra1, "-", palabra2)
else:
  print(palabra2, "-", palabra1)