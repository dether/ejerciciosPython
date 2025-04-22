"""1. Cree un decorador para registrar los argumentos de la función y el valor devuelto

Escriba un programa de Python para crear un decorador que registre los argumentos y devuelva el valor de una función.

Haga clic en mí para ver la solución de ejemplo"""

def registro(func):
    def proceso(*args, **kwargs):
        print(f"Llamando a la función {func.__name__} con argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} devolvió: {resultado}")
        return resultado
    return proceso

@registro
def suma(a, b):
  return a + b

suma(3, 4)


"""2. Crear un decorador para medir el tiempo de ejecución de la función

Escriba un programa de Python para crear una función decoradora para medir el tiempo de ejecución de una función.

Haga clic en mí para ver la solución de ejemplo"""

import time #es un modulo de la libreria de python

def medirTiempo(func):
    def cronometro(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"La función {func.__name__} tardó {fin - inicio:.2f} segundos")
    return cronometro

@medirTiempo
def simulacion():
    time.sleep(3)
    return "Listo"
#def suma():
#    resultado = 100 + 500 // 2 
#    return resultado

simulacion()


"""4. Implemente un decorador para almacenar en caché los resultados de la función

Escriba un programa de Python que implemente un decorador para almacenar en caché el resultado de una función."""

def cachear(func):
    cache = {}

    def almacenando(*args):
        if args in cache:
            print(f"Operación ya guardada en caché. {args[0]} - {args[1]} = {cache[args]}")
            return cache[args]
        else:
            print(f"Operación nueva, calculando y guardando en caché. {args[0]} - {args[1]} = {args[0] - args[1]}")
            resultado = func(*args)
            cache[args] = resultado
            return resultado
    return almacenando

@cachear
def resta(a,b):
    return a - b

resta(10,5)
resta(10,5)
resta(2, 1)


"""KWARGS: Sirve cuando querés que tu función pueda aceptar cualquier cantidad de argumentos con nombre, sin saberlos de antemano. DICCIONARIOS"""
def mostrar_info(**kwargs): #{nombre:lucia, edad:30, ciudad: resistencia}
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Lucía", edad=30, ciudad="Resistencia")

