"""Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
    Ingrese num: 1
    Ingrese num: 7
    La suma es 20"""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
menor = 0
mayor = 0
suma = 0
#Determinamos cual es menor y mayor
if num1 < num2:
    menor = num1
    mayor = num2
elif num2 < num1:
    menor = num2
    mayor = num1
else:
    print("0")

# mientras que sean números distintos
if mayor - menor > 0:
    #tomamos los valores desde el menor + 1 hasta un número anterior al mayor
    for i in range(menor+1, mayor):
        suma = suma + i

    print(f"La suma es {suma}")
