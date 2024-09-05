"""Escribir un programa que solicite al usuario que ingrese números enteros, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse. 
- A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar. 
- Recorrer la lista para imprimir la sumatoria de todos los elementos. 
- Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]"""

numero = 1
numeros = []
valor = 1
while valor != 0:
    numero = int(input("Ingrese un número: "))
    if numero != 0:
        numeros.append(numero)
    else:
        valor = 0
    print("Ingrese 0 para salir.")


quitar = int(input("Ingrese un número para quitarlo: "))
borrar = False

for i in numeros:
    if i == quitar:
        borrar = True
if borrar:
    print(f"Borrando {quitar} de la lista n°1: {numeros}.")
    numeros.remove(quitar)
    print(f"lista: {numeros}")
else:
    print(f"No es posible eliminar {quitar}, ya que no se encuentra en la lista n°1.")
total = 0
print(f"Sumando todos los elementos de la lista n°1.")
for i in numeros:
    total = total + i

print(f"La sumatoria de todos los elementos de la lista n°1 es: {total}")

nuevoNumero = int(input("Ingrese un nuevo número: "))
nuevaLista = []
print(f"Creando lista n°2: {nuevaLista}")
for i in numeros:
    if nuevoNumero > i:
        nuevaLista.append(i)
print(f"Agregando los elementos de la lista n°1 a la nueva lista n°2, con valores menores a {nuevoNumero}")

print(f"Imprimiento lista n°2")
for i in nuevaLista:
    print(i)

print(f"Generando e imprimiendo lista n°3 que contiene como elementos a tuplas de dos elementos")
lista3 = []
print(f"lista n°3: {lista3}")
lista3 = []

for numero in nuevaLista:
    # Verificamos si el número ya está en lista3
    encontrado = False
    for tupla in lista3:
        #verificamos si ya existe una tupla con ese número ("numero", cantidad) 
        if tupla[0] == numero:
            encontrado = True
            break
    #Si no se repite, entonces
    if not encontrado:
        # Contar cuántas veces aparece el número en nuevaLista
        cantidad = 0
        for num in nuevaLista:
            if num == numero:
                cantidad += 1
        
        # Agregar la tupla (número, cantidad) a lista3
        print(f"El número {numero} se repite {cantidad} veces.")
        print(f"Agregamos la tupla: ({numero}, {cantidad}) a lista3: {lista3}")
        lista3.append((numero, cantidad))

print(f"Lista3: {lista3}")







