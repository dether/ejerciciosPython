#Funciones

#!Funciones sin Parámetros
def saludar():
    print("¡Hola, mundo!")
    
saludar()  # Salida: ¡Hola, mundo!

#!Funciones con Parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")  # Salida: ¡Hola, Ana!

#!Funciones con Valores por Defecto
def saludar(nombre="Mundo"):
    print(f"¡Hola, {nombre}!")

saludar()         # Salida: ¡Hola, Mundo!
saludar("Luis")  # Salida: ¡Hola, Luis!

#!Funciones con Valores de Retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Salida: 8

#!Funciones con Múltiples Valores de Retorno
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operaciones(10, 5)
print(resultado_suma)  # Salida: 15
print(resultado_resta)  # Salida: 5

#!Funciones con Argumentos Variables
def mostrar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

mostrar_nombres("Ana", "Luis", "Pedro")

def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25)

#!Funciones Anidadas

def externa(x):
    print(f"x: {x}")
    def interna(y):
        print(f"y: {y}")
        print(f"return: {y+1}")
        return y + 1
    print(f"{interna(x) * 2}")
    return interna(x) * 2

print(externa(5))  # Salida: 12

#!Decoradores
def decorador(func):
    def envoltura():
        print("Algo está sucediendo antes de llamar a la función.")
        func()
        print("Algo está sucediendo después de llamar a la función.")
    return envoltura

@decorador
def decir_hola():
    print("¡Hola!")

decir_hola()

#!Funciones Generadoras
def contar_hasta_ten():
    for i in range(1, 11):
        yield i #no se puede iterar con return

for numero in contar_hasta_ten():
    print(numero)

#!Funciones Recursivas 
# (Una función puede llamarse a sí misma, lo que se conoce como recursión.)
def factorial(n):
    print(f"Entrando a factorial({n})")
    if n == 0:
        print(f"factorial({n}) = 1 (caso base)")
        return 1
    else:
        resultado = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) = {resultado}")
        return resultado

print(factorial(5))  # Salida: 120

#!Funciones con Anotaciones
def multiplicar(a: int, b: int) -> int:
    return a * b

print(multiplicar(4, 5))  # Salida: 20





