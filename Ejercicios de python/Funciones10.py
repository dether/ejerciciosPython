""" Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al 
leer una fecha se asegura que es válida."""

def LeerFecha ():
    dia = int(input("Ingrese un número entero, para el día: "))
    mes = int(input("Ingrese un número entero, para el mes: "))
    anio = int(input("Ingrese un número entero, para el anio: "))
    return dia, mes, anio

def FechaValida(dia, mes, anio):
    tresCero = [4, 6, 9, 11]
    if dia < 1 or dia > 31 or mes < 1 or mes > 12:
        return False
    if mes == 2 and (dia == 30 or dia == 31):
        return False
    if mes == 2 and not(EsBisiesto(anio)) and dia == 29:
        return False
    if mes in tresCero and dia == 31:
        return False
    return True
    
def EsBisiesto(anio: int):
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

def DiasDelMes(mes: int, anio: int):
    tresUno = [1, 3, 5, 7, 8, 10, 12]
    tresCero = [4, 6, 9, 11]
    if mes == 2: 
        if EsBisiesto(anio):
            return (f"En el año {anio} y mes {mes}, hay 29 días. ✅")
        return (f"En el año {anio} y mes {mes}, hay 28 días. ✅")
    elif mes in tresCero:
        return (f"En el año {anio} y mes {mes}, hay 30 días. ✅")
    elif mes in tresUno:
        return (f"En el año {anio} y mes {mes}, hay 31 días. ✅")

def Calcular_Dia_Juliano (dia:int, mes:int, anio:int):
    if mes == 1 or mes == 2:
        mes = mes + 12
        anio = anio - 1
    juliano = (dia + (13 * (mes + 1)) // 5 + 365 * anio + anio // 4 - anio // 100 + anio // 400 + 1721119)
    return juliano

opcion = 0
print("Bienvendio usuario 🤓")
while True:
    print("""Seleccione una de las siguientes opciones: 🤔
        opcion 0: Salir
        opcion 1: Averiguar dias que tiene un mes en ese año.
        opcion 2: Averiguar si un año es bisiesto.
        opcion 3: Averiguar el día juliano de una fecha.""")
    try:
        opcion = int(input("Ingrese una opción para continuar: "))
    except ValueError:
        print("Opción incorrecta, intentelo de nuevo. 🤯")
        continue

    if opcion == 0:
        print("Que tenga un buen día! 👋")
        break

    elif opcion == 1:
        while True:
            try:
                mes = int(input("Ingrese el número entero del mes: "))
                if mes < 1 or mes > 12:
                    print("El mes debe ser un número entre 1 y 12. Inténtalo de nuevo. ❌")
                    continue
                anio = int(input("Ingrese el número entero del año: "))
            
                resultado = DiasDelMes(mes, anio)
                print(resultado)
                break
            except ValueError:
                print("Valores incorrectos, ingrese un número entero, por favor. 🤯")

    elif opcion == 2:
        while True:
            try:
                anio = int(input("Ingrese el año: "))
                if EsBisiesto(anio):
                    print(f"El año {anio} es bisiesto.")
                else:
                    print(f"El año {anio} no es bisiesto.")
                break
            except ValueError:
                print("Valores incorrectos, ingrese un número entero, por favor. 🤯")

    elif opcion == 3:
        while True:
            try:
                dia, mes, anio = LeerFecha()
                resultado = FechaValida(dia, mes, anio)
                if not resultado:
                    print("Fecha ingresada no valida.")
                    continue


                dia_juliano = Calcular_Dia_Juliano(dia, mes, anio)
                print(f"El día juliano de la fecha: {dia}/{mes}/{anio} es: {dia_juliano}. ✔️")
                break
            except ValueError:
                print("Valores incorrectos, ingrese un número entero o una fecha valida por favor. 🤯")
    else:
        print("Opcion ingresa incorrecta. 🤯")