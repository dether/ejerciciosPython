""" Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.
Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
Vamos a crear varias funciones para trabajar con la pila:
• LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene. 
• EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene 
elementos. 
• EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena. 
• AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, 
si no está llena. si esta llena muestra un mensaje de error. 
• SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo 
borra de la pila. Si la pila está vacía muestra un mensaje de error. 
• EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila. 
Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, 
con las siguientes opciones:
1. Añadir elemento a la pila 
2. Sacar elemento de la pila 
3. Longitud de la pila 
4. Mostrar pila 
5. Salir """

def longitudPila(pila):
    return (len(pila))
""" asd = longitudPila(["hola","asd"])
print(asd) """

def estaVaciaPila(pila):
    return len(pila) == 0
""" asd2 = estaVaciaPila([])
print(asd2) """

def estaLlenaPila(pila):
    max = 5
    if len(pila) >= max:
        return True
    return False
""" asd = estaLlenaPila(["1","2","3","4","5"])
print(asd) """

def addPila (caracter, pila):
    if estaLlenaPila(pila):
        return "Mensaje de error. La pila esta llena."
    else:
        pila.append(caracter)
        """ print(pila) """
""" asd = addPila("6",["1","2","3","4"])
print(asd) """

def sacarDeLaPila(pila):
    if estaVaciaPila(pila):
        return "Mensaje de error. La pila esta vacia."
    pilaSacada = pila.pop()
    return pilaSacada
""" asd = sacarDeLaPila(["1","2","3","4","5"])
print(asd) """

def escribirPila(pila):
    return pila
""" asd = escribirPila(["1","2","3","4","5"]) """

opcion = 0
pila = []
print("🚩 Bienvenido usuario 🚩")
while True:
    try:
        print(""" 
    🤓 Seleccione una de las siguientes opciones para continuar:
            1. Añadir elemento a la pila 
            2. Sacar elemento de la pila 
            3. Longitud de la pila 
            4. Mostrar pila 
            5. Salir """)
        opcion = int(input("🤓 Ingrese una opción: "))
    except:
        print("💥 Opción invalida, intentelo de nuevo.")

    if opcion == 1:
        caracter = input("Ingrese un caracter o una cadena de caracter para agregar a la pila: ")
        resultado = addPila(caracter, pila)
        if resultado:
            print(resultado)
            continue
    
    elif opcion == 2:
        resultado = sacarDeLaPila(pila)
        if resultado:
            print(resultado)
            continue
    
    elif opcion == 3:
        resultado = longitudPila(pila)
        print(resultado)
        continue

    elif opcion == 4:
        resultado = escribirPila(pila)
        print(resultado)
        continue
    

    elif opcion == 5:
        print("\n😎 Que tengas un buen día, gracias por confiar en nosotros.")
        break;
