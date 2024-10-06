""" Crear una función que calcule el MCD de dos número por el método de Euclides. El método de 
Euclides es el siguiente:
• Se divide el número mayor entre el menor. 
• Si la división es exacta, el divisor es el MCD. 
• Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD. 
Crea un programa principal que lea dos números enteros y muestre el MCD."""

#metodo: a mayor que b
#si el resto es == 0 entonces MCD = b
#si el resto es != entonces a = b y b = resto

def metodoEuclides (a, b):
    if (type(a) != int) or (type(b) != int):
        return "Los argumentos ingresados no son números enteros."
        
    if (a == 0) or (b == 0):
        return 0
        
    if a > b:
        max = a
        min  = b
    else:
        max = b
        min = a

    while True:
        resto = max % min

        if resto == 0:
            mcd = min
            return mcd
        else:
            max = min
            min = resto



""" x = metodoEuclides(18, 12)
print(x) """

def pedirNumeros ():
    while True:
        try:
            a = int(input("Ingrese el primer número entero: "))
            b = int(input("Ingrese el segundo número entero: "))
        except:
            print("El valor ingresado es invalido, por favor ingrese números enteros.")
            continue
        if a and b or (a == 0) or (b == 0):
            mcd = metodoEuclides(a, b)
            break

    print(f"El MCD de los números ingresados, es {mcd}.")

pedirNumeros()
