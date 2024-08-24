print(""" Escribir un programa que realice la descomposición en factores 
primos de un número introducido por teclado. El programa deberá ir 
escribiendo la tabla de los factores primos, a medida que los va
calculando, tal como muestra el ejemplo siguiente: 
Introduce un Nº entero -> 84 
Nº | Factores primos
-- | --------------- 
84 | 2 
42 | 2 
21 | 3 
 7 | 7 
 1 | 
""")

numero = int(input("Ingrese un número: "))
divisor = 2
print("Nº | Factores primos")
print("-- | --------------- ")
while numero > 1:
  if numero % divisor == 0:
    print(numero,"|", divisor)
    numero = int(numero / divisor)
  else:
    divisor = divisor + 1

print(" 1 |")