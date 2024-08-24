print("Realizar un programa que lea 20 números (entre el 1 y el 10) y muestre aquel o aquellos que hayan aparecido más veces. ")

# Con esta lista vamos a contar las cantidades y dependiendo de la posición "i" sera el número
# 0-9 = 1-10 ... 0 = 1, 1 = 2, ..., 9 = 10.
conteo = [0,0,0,0,0,0,0,0,0,0]

#Lista vacia para almacenar los 20 números ingresados del 1 al 10.
numeros = []

# Intentos, si ingresan un número != del 1 al 10. El intento no se consume.
intentos = 20

# Cuenta las veces maxima que se repite un número!
maxApariciones = 0

while intentos > 0:
  numero = int(input("Ingrese un numero del 1 al 10: "))
  if 1 <= numero <= 10:
    numeros.append(numero)
    intentos = intentos - 1
  else:
    print("Número invalido.")

# cuenta cuantas veces se ingresa el mismo número!
for numero in numeros:
  conteo[numero - 1] = conteo[numero - 1] + 1

# maxima cantidad de repeticiones de número
for i in range(9):
  if conteo[i] > maxApariciones:
    maxApariciones = conteo[i]

# Número que más veces se repitio
print("El/los número/os que más veces aparecieron fueron:")
for i in range(9):
    if conteo[i] == maxApariciones:
        print("El número", i + 1, "aparecio", maxApariciones, "veces")

