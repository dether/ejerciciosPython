"""1 Crea una función llamada InvertirCadena que reciba un string y devuelva el mismo string pero con el orden de los caracteres invertido. No uses métodos de string avanzados."""

def invertirCadena(string: str):
    inverso = ""
    for i in string:
        inverso = i + inverso
    return inverso
asd = invertirCadena("hola asd")
print(asd)

"""2 Crea una función llamada ContarVocales que reciba una cadena y devuelva la cantidad de vocales que tiene. Evita utilizar métodos específicos de strings."""

def contarVocales(cadena):
    contador = 0
    for i in cadena:
        contador += 1
    return contador
asd2 = invertirCadena("hola")
print(asd2)

"""3 Diseña una función BuscarPalabra que reciba una lista de palabras y una palabra a buscar, y devuelva la posición en la que se encuentra la palabra. Si no está presente, retorna -1. No utilices el método index."""

def buscarPalabra(lista, palabra):
    if len(lista) != 0:
        for i in range(len(lista)):
            if lista[i] == palabra:
                return f"El indice del elemento que buscas es: {i}."
            else:
                return -1
asd3 = buscarPalabra(["ale","hola","chau","recreo"], "chau")
print(asd3)

"""4 Crea una función llamada EsPalindromo que reciba una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda). No utilices métodos avanzados."""

def esPalindromo(cadena):
    inverso = ""
    for i in cadena:
        inverso = i + inverso
    return "Es palindromo" if inverso == cadena else "No es palindromo"
asd4= esPalindromo("hooh")
print(asd4)

"""5 Escribe una función EliminarDuplicados que reciba una lista de enteros y elimine los elementos duplicados, devolviendo una nueva lista sin ellos. No utilices métodos como set()."""

def eliminarDuplicados(lista):
    listaSinRepeticiones = []
    for elemento in lista:
        if elemento not in listaSinRepeticiones:
            listaSinRepeticiones.append(elemento)
    return listaSinRepeticiones
asd5 = eliminarDuplicados([1,2,3,4,5,1,2,6,1,5])
print(asd5)

"""6 Desarrolla una función ContarPalabras que reciba un string y devuelva la cantidad de palabras que contiene. Se considera una palabra a cualquier secuencia de caracteres separados por espacios."""

def contarPalabras(string):
    """ contador = 0
    for letra in string:
        contador = contador +1
    return contador """
    return len(string)
asd6 = contarPalabras("holaaaaa")
print(asd6)

"""7 Crea una función CompararListas que reciba dos listas de enteros y devuelva True si tienen los mismos elementos, independientemente del orden, y False en caso contrario."""

def compararListas(lista1, lista2):
    if len(lista1) == len(lista2):
        for elemento in lista1:
            if elemento not in lista2:
                return False
        for elemento in lista2:
            if elemento not in lista1:
                return False
        return True
    else:
        return False
asd7 = compararListas([1,2,3,4], [2,4,1,3])
print(asd7)

"""8 Escribe una función OrdenarSeleccion que implemente el algoritmo de ordenamiento por selección para una lista de números y devuelva la lista ordenada de menor a mayor."""

def ordenarSeleccion(lista):
    nuevaLista = []
    #listaVieja = lista
    while lista:
        menor = lista[0]
        for elemento in lista:
            if elemento < menor:
                menor = elemento
        nuevaLista.append(menor)
        lista.remove(menor)
    return nuevaLista
asd8 = ordenarSeleccion([1,5,7,3,4,2,3,5,1,1,0,-1])
print(asd8)

"""9 Desarrolla una función EsPerfecto que reciba un número entero y determine si es un número perfecto (un número que es igual a la suma de sus divisores propios)."""

def esPerfecto(numero):
    divisores = []
    total = 0
    for i in range(1,numero):
        if numero % i == 0:
            divisores.append(i)
    for elementos in divisores:
        total = total + elementos
    if total == numero:
        return True
    else:
        return False
asd9 = esPerfecto(6) #28 496
print(asd9)

"""10 Crea una función ContarCaracteres que reciba una cadena y devuelva un diccionario con el conteo de cada carácter en la cadena, ignorando espacios en blanco."""

def contarCaracteres(cadena):
    diccionario = {}
    for letra in cadena:
        if not letra == " ":
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return diccionario
asd10 = contarCaracteres("h o l a c o m o e s t a s ?")
print(asd10)

"""11 Crea una función MultiplicarElementos que reciba una lista de números y devuelva una nueva lista donde cada elemento sea el resultado de multiplicar el elemento original por 2."""

def multiplicarElementos(lista):
    nuevaLista = []
    for elemento in lista:
        nuevaLista.append(elemento * 2)
    return f"Antes:{lista} y después:{nuevaLista}"
asd11 = multiplicarElementos([1,2,3,4,5,6])
print(asd11)

"""12 Desarrolla una función FiltrarPares que reciba una lista de enteros y devuelva una nueva lista que contenga solo los números pares."""

def filtrarPares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return f"lista:{lista} listaPares:{pares}"
asd12 = filtrarPares([1,2,3,4,5,6,7,8,9,10])
print(asd12)

"""13 Crea una función SumarElementos que reciba una lista de números y devuelva la suma de todos los elementos. No uses la función sum()."""

def sumarElementos(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma
asd13 = sumarElementos([1,2,3,4,5])
print(asd13)

"""14 Escribe una función BuscarElemento que reciba una lista y un elemento, y devuelva True si el elemento está en la lista y False si no lo está. No uses el operador in."""

def buscarElemento(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False
asd14 = buscarElemento([1,2,3,4,5], 3)
print("eje14: ",asd14)

"""15 Crea una función ContarConsonantes que reciba una cadena y devuelva la cantidad de consonantes que contiene, ignorando espacios y vocales."""

def contarConsonantes(cadena):
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    contador = 0
    for letra in cadena:
        for consonante in consonantes:
            if letra == consonante:
                contador = contador + 1
    return contador
asd15 = contarConsonantes("hola como estas corazon uwu?")
print(asd15)

"""16 Desarrolla una función EliminarNulos que reciba una lista que puede contener elementos nulos (None) y devuelva una nueva lista sin esos elementos."""

def eliminarNulos(lista):
    nuevaLista = []
    for elemento in lista:
        if elemento is not None:
            nuevaLista.append(elemento)
    return nuevaLista
asd16 = eliminarNulos([None, "", "Null", "algo", 2, 3.3, None])
print(asd16)

"""17 Crea una función GenerarFibonacci que reciba un número entero n y devuelva una lista con los n primeros números de la secuencia de Fibonacci."""

def generarFibonacci(numero):
    lista = []
    ultimo = 0
    penultimo = 1
    valor = 0
    for i in range(numero):
        """ print(f"{i+1}: Fn = {ultimo} + {penultimo}") """
        valor =  ultimo + penultimo
        penultimo = ultimo 
        ultimo = valor
        """ print(f"{i+1}: Fn = {valor}") """
        lista.append(valor)
    return lista
asd17 = generarFibonacci(10)
print(asd17)

"""18 Escribe una función CrearTablaMultiplicar que reciba un número entero n y devuelva una lista que contenga las multiplicaciones del número n del 1 al 10."""

def crearTablaMultiplicar(numero):
    """ lista = []
    for i in range(1, numero+1):
        lista.append(i*numero) """
    lista = [i*numero for i in range(1,numero+1)]
    return lista
asd18 = crearTablaMultiplicar(10)
print(asd18)

"""19 Desarrolla una función RotarLista que reciba una lista y un número entero n, y devuelva una nueva lista con los elementos rotados n posiciones a la derecha."""

def rotarLista(lista, numero):
    nuevaLista = []
    num = numero % len(lista)
    nuevaLista = lista[-num:] + lista[:-num]
    #"-numero": obtiene los últimos numero elementos.
    #":-numero": obtiene todos los elementos hasta el final menos los últimos numero
    return nuevaLista
asd19 = rotarLista([1,2,3,4,5,6], 3)
print(asd19)

"""20 Crea una función EncontrarMayorMenor que reciba una lista de números y devuelva una tupla con el valor máximo y el mínimo de la lista, sin usar los métodos max() y min()."""

def encontrarMayorMenor(lista):
    max = lista[0]
    min = lista[0]
    for elemento in lista:
        if elemento > max:
            max = elemento
        elif elemento < min:
            min = elemento
    return (max,min)
asd20 = encontrarMayorMenor([1,2,3,4,5])
print(asd20)