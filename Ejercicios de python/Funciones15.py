"""Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.
En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola 
que es la que tienes que modificar"""

def longitudCola(cola):
    return (len(cola))
""" asd = longitudCola(["hola","asd"])
print(asd) """

def estaVaciaCola(cola):
    return len(cola) == 0
""" asd2 = estaVaciaCola([])
print(asd2) """

def estaLlenaCola(cola):
    max = 5
    if len(cola) >= max:
        return True
    return False
""" asd = estaLlenaCola(["1","2","3","4","5"])
print(asd) """

def addCola (caracter, cola):
    if estaLlenaCola(cola):
        return "Mensaje de error. La cola esta llena."
    else:
        cola.append(caracter)
        """ print(cola) """
""" asd = addCola("6",["1","2","3","4"])
print(asd) """

def sacarDeLaCola(cola):
    if estaVaciaCola(cola):
        return "Mensaje de error. La cola esta vacia."
    colaSacada = cola.pop(0) # del cola(0)
    return colaSacada
""" asd = sacarDeLaCola(["1","2","3","4","5"])
print(asd) """

def escribirCola(cola):
    return cola
""" asd = escribirCola(["1","2","3","4","5"]) """

opcion = 0
cola = []
print("🚩 Bienvenido usuario 🚩")
while True:
    try:
        print(""" 
    🤓 Seleccione una de las siguientes opciones para continuar:
            1. Añadir elemento a la cola 
            2. Sacar elemento de la cola 
            3. Longitud de la cola
            4. Mostrar cola
            5. Salir """)
        opcion = int(input("🤓 Ingrese una opción: "))
    except:
        print("💥 Opción invalida, intentelo de nuevo.")

    if opcion == 1:
        caracter = input("Ingrese un caracter o una cadena de caracter para agregar a la pila: ")
        resultado = addCola(caracter, cola)
        if resultado:
            print(resultado)
            continue
    
    elif opcion == 2:
        resultado = sacarDeLaCola(cola)
        if resultado:
            print(resultado)
            continue
    
    elif opcion == 3:
        resultado = longitudCola(cola)
        print(resultado)
        continue

    elif opcion == 4:
        resultado = escribirCola(cola)
        print(resultado)
        continue
    

    elif opcion == 5:
        print("\n😎 Que tengas un buen día, gracias por confiar en nosotros.")
        break;