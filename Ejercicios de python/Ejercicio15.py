print(""""
Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división. El programa debe recibir como entrada 2 números reales y un operador, que puede ser 
+, -, * o /.
La salida del programa debe ser el resultado de la operación.
Operando: 3
Operador: +
Operando: 2
3 + 2 = 5
      
Operando: 6
Operador: -
Operando: 7
6 - 7 = -1
      
Operando: 4
Operador: *
Operando: 5
4 * 5 = 20
      
Operando: 10
Operador: /
Operando: 4
10 / 4 = 2.5
      
Operando: -1
Operador: **
Operando: 4
-1 ** 4 = 1""")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese un operador:")
valor = True

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
elif operador == "**":
    resultado = num1 ** num2
else: 
    print(f"El operador ingresado, no es valido: {operador}")
    valor= False

if valor:
    print(f"Operando: {num1}\nOperador: {operador}\nOperando: {num2}\n{num1} {operador} {num2} = {resultado}")