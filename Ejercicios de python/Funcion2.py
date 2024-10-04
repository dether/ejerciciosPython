""" Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

def esMultiplo (num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")


def pedirNumeros ():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2= int(input("Ingrese el segundo número: "))

        if num1 == 0 or num2 == 0:
            print("Ninguno de los números debe ser cero.")
    except:
        print("El valor ingresado no es un número entero o es cero.")
        return
    
    esMultiplo(num1, num2)

pedirNumeros()