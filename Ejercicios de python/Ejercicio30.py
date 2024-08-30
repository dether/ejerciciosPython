"""Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
    Ingrese numero: 51
    Ingrese numero: 24
    24 51
A continuación, escriba otro programa que haga lo mismo con tres números:
    Ingrese numero: 8
    Ingrese numero: 1
    Ingrese numero: 4
    1 4 8
Finalmente, escriba un tercer programa que ordene cuatro números:
    Ingrese numero: 7
    Ingrese numero: 0
    Ingrese numero: 6
    Ingrese numero: 1
    0 1 6 7
Recuerde que su programa debe entregar la solución correcta para cualquier combinación de números, no sólo para los ejemplos mostrados aquí. Hay más de una manera de resolver cada ejercicio."""
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

if num1 < num2:
    print(num1, num2)
elif num2 < num1:
    print(num2, num1)

num3 = int(input("Ingrese un número: "))
num4 = int(input("Ingrese un número: "))
num5 = int(input("Ingrese un número: "))
#123
#345
if num3 < num4 and num4 < num5:    
    print(num3, num4, num5)
elif num3 < num5 and num5 < num4:   
    print(num3, num5, num4)
elif num4 < num3 and num3 < num5:   
    print(num4, num3, num5)
elif num4 < num5 and num5 < num3:   
    print(num4, num5, num3)
elif num5 < num4 and num4 < num3:   
    print(num5, num4, num3)
elif num5 < num3 and num3 < num4:   
    print(num5, num3, num4)

num6 = int(input("Ingrese un número: "))
num7 = int(input("Ingrese un número: "))
num8 = int(input("Ingrese un número: "))
num9 = int(input("Ingrese un número: "))
numeros = [num6, num7, num8, num9]

for i in range(len(numeros)-1):
    for j in range(0, len(numeros)-i-1):
        #cuando i = 0, j = 0,1,2
        #cuando i = 1, j = 0,1 
        #cuando i = 2, j = 0
        if numeros[j] > numeros[j+1]:
            #invertimos su ubicación si se cumple la condición.
            numeros[j], numeros[j+1] = numeros[j + 1], numeros[j]

print(numeros[0], numeros[1], numeros[2], numeros[3])
