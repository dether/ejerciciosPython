""" El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
• LeerFecha: Nos permite leer por teclado una fecha (día, mes y año). 
• DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año. 
• EsBisiesto: Recibe un año y nos dice si es bisiesto. 
• Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano."""

#n° juliano = divisible entre 4 y entre 400.
# .5 si es mediodia y .6 si es medianoche.

def LeerFecha ():
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
    elif mes in tresCero and dia == 31:
        return"El mes ingresado solo puede tener 30 días como maximo. Inténtalo de nuevo. ❌"
    
    return dia, mes, anio

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
                resultado = LeerFecha()
                if type(resultado) == str:
                    print(resultado)
                    continue

                dia_juliano = Calcular_Dia_Juliano(resultado[0], resultado[1], resultado[2])
                print(f"El día juliano de la fecha: {resultado[0]}/{resultado[1]}/{resultado[2]} es: {dia_juliano}. ✔️")
                break
            except ValueError:
                print("Valores incorrectos, ingrese un número entero o una fecha valida por favor. 🤯")
    else:
        print("Opcion ingresa incorrecta. 🤯")