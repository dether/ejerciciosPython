"""Escribir un programa que introduzca el número de un mes (1 a 12) y visualice el número de días de ese mes."""

numeroMes = int(input("Ingrese el número de un mes (1 a 12): "))
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12
diasMes = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if numeroMes < 1 or numeroMes > 12:
    print("El número ingresado es invalido, ingrese un número del (1 a 12)")
else:
    print(f"En el mes {numeroMes} hay {diasMes[numeroMes]} días.")
