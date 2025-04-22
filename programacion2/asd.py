def mi_decorador(funcion_original):
    def nueva_funcion():
        print("Antes de llamar a la función original")
        funcion_original()
        print("Después de llamar a la función original")
    return nueva_funcion

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()


def decorador(func):
    def wrapper(*args, **kwargs):
        print("Llamando a la función con argumentos:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@decorador
def sumar(a, b):
    return a + b

print(sumar(3, 4))
