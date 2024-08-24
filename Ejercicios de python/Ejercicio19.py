"""
Hacer un algoritmo que haga lo siguiente:
Pida dos números al usuario, y que los multiplique. Si la multiplicación da un valor menor a 150, se 
volverán a pedir los números hasta que la multiplicación de ambos tengan una respuesta mayor a 
150. Mostrar la respuesta en cada intento.
"""
num1 = 0
num2 = 0
valor = True

while valor:
  num1 = float(input("Ingresa el primer número: "))
  num2 = float(input("Ingrese el segundo número: "))
  producto = num1 * num2
  if not producto < 150:
    print(f"El producto no es menor a 150. El producto es: {producto}")
    valor = False
  else:
    print(f"El producto es menor a 150. Producto = {producto}")