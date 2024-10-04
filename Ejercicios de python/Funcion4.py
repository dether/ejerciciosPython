""" Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el 
mínimo, sin utilizar los métodos de listas."""

def calcularMaxMin (lista):
    if len(lista) == 0:
        return "Lista vacia. Debe ingresar una lista con números enteros."
    max = -9999999
    min = 9999999
    for i in lista:
        if i > max:
            max = i
        if i < min:
            min = i
    print (f"Según la lista = {lista}, el minimo es {min} y el maximo es {max}.")

def pedirNumeros ():
    lista = []
    print("Ingrese números para agregarlo a una lista. Ingrese 0 para salir.")
    while True:
        try:
            num = int(input("Ingrese un número: "))
            if num == 0:
                break;
            lista.append(num)
        except:
            print(f"El valor ingresado es invalido. Ingrese un número entero.")
            continue
    calcularMaxMin(lista)

pedirNumeros()
