"""Escribir dos funciones que permitan calcular:
• La cantidad de segundos en un tiempo dado en horas, minutos y segundos. 
• La cantidad de horas, minutos y segundos de un tiempo dado en segundos. 
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, 
convertir a horas,minutos y segundos o salir del programa."""

def convertirSegundos (horas,minutos,segundos):
    """ if type(horas) != int or type(minutos) != int or type(segundos) != int:
        return f"Los valores del argumento no son enteros, horas:{horas}, minutos:{minutos}, segundos:{segundos}."  """
    if horas or minutos:
        horas = horas * 60 * 60
        segundos = segundos + horas
        horas = 0
        minutos = minutos * 60
        segundos = segundos + minutos
        minutos = 0
    return f"{segundos} segundos."

""" x = convertirSegundos(2,0,0)
print(x) """

def convertirHoras (segundos):
    """ if type(segundos) != int:
        return f"El valor del argumento no es entero, segundos:{segundos}." """
    if segundos:
        minutos = int(segundos / 60)
        segundos = segundos - (minutos * 60)
        horas = int(minutos / 60)
        minutos =  minutos - (horas * 60)
    return f"{horas}:{minutos}:{segundos} horas, minutos y segundos."

""" y = convertirHoras(11000)
print(y) """

print("¡Bienvenido a la calculadora de conversión entre segundos, minutos y horas, y viceversa!")

mensaje = ""
while True:
    print("A) Convertir de segundos a horas, minutos y segundos.\nB) Convertir de horas, minutos y segundos a segundos.\nC) Salir del programa.")
    opcion = input("Ingrese una opción: ").upper()
    
    if opcion == "A":
        try:
            segundos = int(input("Ingrese los segundos a convertir: "))
            mensaje = convertirHoras(segundos)
        except:
            print("Por favor ingrese un número entero.")
            print("Volviendo al menu principal.")
            continue
    elif opcion == "B":
        try:
            horas = int(input("Ingrese las horas a convertir: "))
            minutos = int(input("Ingrese los minutos a convertir: "))
            segundos = int(input("Ingrese los segundos a convertir: "))
            mensaje = convertirSegundos(horas, minutos, segundos)
        except:
            print("Por favor ingrese un número entero.")
            print("Volviendo al menu principal.")
            continue
    elif opcion == "C":
        print("Has elegido salir del programa. ¡Gracias por usar la calculadora!")
        break
    else:
        print("La opción ingresada es inválida. Por favor, ingrese 'A' o 'B'.")

    if mensaje:
        print(mensaje)
        print 
        continue