#Diccionarios

#!Crear un Diccionario:
diccionarioVacio = {}
#print(diccionarioVacio) #{}
diccionarioLleno = {'clave1': 'valor1', 'clave2': 'valor2'} 
#print(diccionarioLleno) #{'clave1': 'valor1', 'clave2': 'valor2'}

#!Acceder a un Valor:
valor = diccionarioLleno['clave1']
#print(valor) #valor1

#!Agregar o Modificar un Elemento:
diccionarioLleno['clave3'] = 'valor3' #Crea una nueva clave con valor "valor3"
diccionarioLleno['clave1'] = 'nuevo_valor1' #Modifica
#print(diccionarioLleno) 

#!Eliminar un Elemento:
del diccionarioLleno['clave2'] #borra la clave y su valor.
#print(diccionarioLleno)

#!Verificar si una Clave Existe:
existe = 'clave3' in diccionarioLleno #True o False
#print(diccionarioLleno)
#print(existe)

#!Obtener Todas las Claves:
claves = diccionarioLleno.keys()
#print(claves)
#print(claves) = dict_keys(['clave1', 'clave3'])

#!Obtener Todos los Valores:
valores = diccionarioLleno.values()
#print(valores) 
#print(valores) = dict_values(['nuevo_valor1', 'valor3'])

#!Obtener Todos los Elementos (pares clave-valor):
items = diccionarioLleno.items()
#print(f"items: {items}") #items: dict_items([('clave1', 'nuevo_valor1'), ('clave3', 'valor3')])

#!Eliminar el Último Elemento (popitem):
#print(diccionarioLleno)
#clave, valor = diccionarioLleno.popitem()
#print(diccionarioLleno)

#!Limpiar el Diccionario:
#diccionarioLleno.clear()
#print(diccionarioLleno) # {}

#!Actualizar Diccionario con Otro Diccionario:
otro_diccionario = {'clave4': 'valor4'}
diccionarioLleno.update(otro_diccionario)
#print(diccionarioLleno)

#!Obtener un Valor con Valor Predeterminado (get):
#si colocalas solo la clave, te trae el valor y visceverza 
valor = diccionarioLleno.get('clave_inexistente', 'valor_predeterminado')
#print(diccionarioLleno)
print("valor", valor)



#*************************************************************************
#*Avanzado
#!Combinar Diccionarios (Python 3.9+):
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
combinado = diccionario1 | diccionario2
#print(combinado)

#!Creación de Diccionarios con Comprehensions:

diccionario = {x: x**2 for x in range(5)} #Crea un diccionario con formato
#print(diccionario) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

for clave, valor in diccionario.items():
    print(clave, valor)
""" 0 0
    1 1
    2 4
    3 9
    4 16 """

#!Invertir un Diccionario:
diccionario = {'a': 1, 'b': 2}
invertido = {valor: clave for clave, valor in diccionario.items()}
#print(diccionario) {'a': 1, 'b': 2}
#print(invertido) {1: 'a', 2: 'b'}

#!Diccionario Anidado:
diccionario_anidado = {
    'persona1': {
        'nombre': 'Juan',
        'edad': 30,
        'direccion': {
            'calle': 'Primera',
            'numero': 123
        }
    },
    'persona2': {
        'nombre': 'Ana',
        'edad': 25,
        'direccion': {
            'calle': 'Segunda',
            'numero': 456
        }
    }
}
#print(diccionario_anidado)

#!Acceder a Valores en un Diccionario Anidado:
nombre_persona1 = diccionario_anidado['persona1']['nombre']
numero_persona2 = diccionario_anidado['persona2']['direccion']['numero']
#print(nombre_persona1)
#print(numero_persona2)

#!Modificar Valores en un Diccionario Anidado:
#print(diccionario_anidado)
diccionario_anidado['persona1']['edad'] = 31
diccionario_anidado['persona2']['direccion']['numero'] = 789
#print(diccionario_anidado)

#!Agregar Nuevos Elementos

diccionario_anidado['persona3'] = {
    'nombre': 'Luis',
    'edad': 28,
    'direccion': {
        'calle': 'Tercera',
        'numero': 789
    }
}
#print(diccionario_anidado)

#!Eliminar Elementos:
del diccionario_anidado['persona2']['direccion']['numero']
del diccionario_anidado['persona1']
#print(diccionario_anidado)

#!Iterar Sobre un Diccionario Anidado
""" for persona, datos in diccionario_anidado.items():
    print(f"Datos de {persona}:")
    for clave, valor in datos.items():
        if isinstance(valor, dict):
            print(f"  {clave}:")
            for subclave, subvalor in valor.items():
                print(f"    {subclave}: {subvalor}")
        else:
            print(f"  {clave}: {valor}") """
""" print =
Datos de persona2:
  nombre: Ana
  edad: 25
  direccion:
    calle: Segunda
Datos de persona3:
  nombre: Luis
  edad: 28
  direccion:
    calle: Tercera
    numero: 789 """