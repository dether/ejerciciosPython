#Listas

#!Crear una Lista
listaVacia = []
mi_lista = [1, 2, 3, 4, 5]

#!Acceder a Elementos:
primer_elemento = mi_lista[0]  # Accede al primer elemento (1)

#!Modificar Elementos:
mi_lista[0] = 10  # Cambia el primer elemento a 10

#*Agregar Elementos: 
#!append(): Agrega al final de la lista.
mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)  # [10, 2, 3, 4, 5, 6]

#!insert(): Agrega en una posición específica.
mi_lista.insert(1, 15)  # [10, 15, 2, 3, 4, 5, 6]

#*Eliminar Elementos:
#!remove(): Elimina el primer elemento con el valor especificado.
mi_lista.remove(15)  # [10, 2, 3, 4, 5, 6]

#!pop(): Elimina y retorna el elemento en una posición específica.
ultimo_elemento = mi_lista.pop()  # [10, 2, 3, 4, 5], ultimo_elemento = 6

#!del: Elimina el elemento en una posición específica.
del mi_lista[0]  # [2, 3, 4, 5]

#!Obtener un Subconjunto:
#print(mi_lista) #[2, 3, 4, 5]
sub_lista = mi_lista[1:3]  # [4, 3, 2]
#print(sub_lista) #[3, 4]

#!Pasos en el Slicing:
#mi_lista = [1, 2, 3, 4, 5, 6, 7]
#print(mi_lista) 
sub_lista = mi_lista[::2]  
#print(sub_lista) #[1, 3, 5, 7]

#*List Comprehensions:
#!Crear una Nueva Lista Basada en una Existente:
cuadrados = [x**2 for x in mi_lista]  
#print(cuadrados) #[4, 9, 16, 25]

#!Con Condiciones:
#print(mi_lista) #[2, 3, 4, 5]
pares = [x for x in mi_lista if x % 2 == 0] 
#print(pares) # [2, 4]

#*Métodos de Listas:
#!extend(): Agrega elementos de una lista a otra
mi_lista.extend([7, 8])  # [5, 4, 3, 2, 7, 8]

#!count(): Cuenta el número de veces que un elemento aparece.
cantidad = mi_lista.count(2)  # 1

#!index(): Retorna el índice del primer elemento con el valor especificado.
indice = mi_lista.index(3)  # 2

#*Listas de Listas (Matrices):
#!Acceso a Elementos en una Matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
elemento = matriz[1][2]  # 6

#!Lista de Comprensión con Condiciones y Anidamientos:
lista = [[x, x**2] for x in range(5) if x % 2 == 0]
# [[0, 0], [2, 4], [4, 16]]
