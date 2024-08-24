print("Escribir un programa que lea dos enteros de dos dígitos y calcule e imprima su producto, cociente y el resto cuando el primero se divide por el segundo.")

num1 = 1
num2 = 1

valor = True

while valor:
  num1 = int(input("Ingrese el primer número: "))
  num2 = int(input("Ingrese el segundo número: "))
  if (10 <= abs(num1) < 100) & (10 <= abs(num2) < 100):
    valor = False
  else:
    print("Ambos números deben ser enteros de dos dígitos.")

producto = num1 * num2
division = num1 / num2
cociente = num1 // num2
resto = num1 % num2 


print(f"El producto es: {producto}.")
print(f"Su división es: {division}.")
print(f"Su cociente es: {cociente}.")
print(f"Su resto es: {resto}.")
    
