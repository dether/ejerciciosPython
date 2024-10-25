""" segundos = 14550 #3hrs
horas = 0
minutos = 0
if segundos:
    minutos = int(segundos / 60)
    segundos = segundos - (minutos * 60)
    horas = int(minutos / 60)
    minutos =  minutos - (horas * 60)
print(horas)
print(minutos)
print(segundos)

mensaje = "a"
if mensaje:
    print("no hay mensaje")
    print(mensaje.upper())












x = 12
if type(x) == int:
    print(x, "es un número.") # 12 es un número.
else:
    print(x, "no es un número.")


diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario:
    print(clave, diccionario[clave]) """

""" x = 15.5

if type(x) == float:
    print(x, "si")
else:
    print(x, "no") """
""" y = 10
x= 10
x = 0

while True:
    try:
        n= int(input("Ingresa un número: "))
        break
    except ValueError:
        print("Por favor, ingresa un número valido.")

for char in "Python":
    print(char)


lista = [1, 2, 3, 4]
for elemento in lista:
    print(elemento) # 1 2 3 4

lista = [1, "dos", 3.0, True]
diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario:
    print(clave, diccionario[clave]) #a 1  b 2  c 3

tupla = (1, 2, 3)

for numero in tupla:
    print(numero) # 1 2 3

print(lista[1]) #dos

lista[1] = "nuevo valor"

del lista[2]

lista.append("nuevo")

print(tupla[0]) #1

diccionario = {"clave1": "valor1", "clave2": "valor2"}

print(diccionario["clave1"]) #valor1

diccionario = {"nombre": "Juan", "edad": 30}
#Verificamos si la clave existe antes de acceder a su valor
if "direccion" in diccionario:
    print(diccionario["diccionario"])
else:
    print("La clave direccion no existe en el diccionario.")

diccionario["clave3"] = "nuevo valor"

del diccionario["clave2"] """
""" mes = 5
tresUno = [1, 3, 5, 7, 8, 10, 12]
tresCero = [4, 6, 9, 11]
if mes in tresUno:
    print("si")
else:
    print("no") """

""" def EsBisiesto(anio):
    if anio % 4 == 0:  
        if anio % 100 == 0:  
            if anio % 400 == 0: 
                return True
            else: 
                return False
        else: 
            return True
    else: 
        return False
 """

""" def LeerFecha ():
    tresUno = [1, 3, 5, 7, 8, 10, 12]
    tresCero = [4, 6, 9, 11]
    dia = int(input("Ingrese un número entero, para el día: "))
    mes = int(input("Ingrese un número entero, para el mes: "))
    anio = int(input("Ingrese un número entero, para el anio: "))
    if dia > 31 or dia < 1:
        return"Valor incorrecto, ingrese un número entero entre 1-31. ❌"
    if mes < 1 or mes > 12:
        return "El mes debe ser un número entre 1 y 12. Inténtalo de nuevo. ❌"
    elif mes == 2 and (dia == 30 or dia == 31):
        return"El mes 2 solo puede tener 28 o 29 días. Inténtalo de nuevo. ❌"
    
    
    return dia, mes, anio
resultado = LeerFecha()
if type(resultado) == str:
    print(resultado)
else:
    print("numeros",resultado, resultado[0]) """

""" asd = "2"

print(f"{"es entero" if type(asd) == int else "es string"}") """

inverso = []
""" longitud = len(lista)
num = len(lista) - 1
if longitud > 0: # 4 > 0
    while num > -1 : # num = 3 2 1 0
        inverso.append(lista[num]) # accedemos a la lista tomando a num como indice
        num = num - 1 # vamos moviendonos
print(inverso) """
""" lista = [1,2,3,4]
inverso = ""
for i in lista:
    # str(transformamos cada numero en string)
    inverso = str(i) + inverso
print(inverso) #"4321" los inverti pero son string entonces
inversoListaString = []
inversoListaEntero = []
for i in inverso:
    inversoListaString.append(i)
print(inversoListaString) # ['4', '3', '2', '1'] si queremos que sean numeros 
#hacemos lo mismo pero agregamos int(lo que queremos transformar en entero.)
for i in inverso:
    inversoListaEntero.append(int(i))
print(inversoListaEntero) # [4, 3, 2, 1] ahora es una lista de numeros """

list2 = [1,2,3,4,5]
""" list2[0]
print(list2[1]) """
""" diccionario = { "a": 1, "b":2} """
""" print(diccionario.object.key("a")) """

print(len("holaa"))
print(list2[-3])