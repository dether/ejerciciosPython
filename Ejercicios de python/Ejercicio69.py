from time import localtime
"""Crear un programa para gestionar datos de los socios de un club, permitiendo:
-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n).

El programa debe iniciar con los datos de los socios fundadores ya cargados: 
Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día. 
Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día. 
Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día. 

-Informar cantidad de socios del club. 
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeuadas. 
-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018. 
-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado). 
-Imprimir el listado de socios completo. """

socios = {
    1:{"numero": 1, "nombre" : "Amanda","apellido": "Núñez", "fecha de ingreso": "17/03/2009", "cuota al día": "s"},
    2:{"numero": 2, "nombre" : "Bárbara","apellido": "Molina", "fecha de ingreso": "17/03/2009", "cuota al día": "s"},
    3:{"numero": 3, "nombre" : "Lautaro","apellido": "Campos", "fecha de ingreso": "17/03/2009", "cuota al día": "s"}}
    #4:{"numero": 4, "nombre" : "ale","apellido": "vargas", "fecha de ingreso": "13/03/2018", "cuota al día": "s"}}
opcion = 1
numero = 0
nombre = ""
apellido = ""
fecha = ""
t = localtime()
dia = t.tm_mday
mes = t.tm_mon
anio = t.tm_year
cuota = ""
while opcion != "0":
    print("1-Agregar socio.")
    print("2-Cantidad de socios en el club. ")
    print("3-Modificar datos.")
    print("4-Dar de baja.")
    print("5-Buscar socio.")
    print("6-Mostrar todos los socios.")
    print("0-Salir.")

    opcion = input("Ingrese una opción: ")

    #Agregar socio
    if opcion == "1":
        print("Hola bienvenido al club, complete los campos para agregarlo como socio.")
        
        #Buscamos los números de socios existentes
        numerosExistentes = sorted(socios.keys())
        nuevoNumero = 1  # Empezamos desde el número 1
        for numero in numerosExistentes:
            if numero == nuevoNumero:
                nuevoNumero += 1  # Si el número ya está en uso, pasamos al siguiente

        nombre = input("Ingrese un nombre: ").lower().capitalize()
        apellido = input("Ingrese su apellido: ").lower().capitalize()
        fecha = f"{dia}/{mes}/{anio}"
        cuota = input("¿Cuota al día? (s/n): ").lower()

        nuevoSocio = {
            "numero": nuevoNumero,
            "nombre": nombre,
            "apellido": apellido,
            "fecha de ingreso": fecha,
            "cuota al día": cuota
        }

        socios[nuevoNumero] = nuevoSocio

    #Mostrar cantidad socios
    elif opcion == "2":
        cantidadMiembros = print(f"La cantidad de socios actualmente es de {len(socios)} miembros.")

    #Modificar datos de un socio
    elif opcion == "3":
        numeroSocio = int(input("Ingrese el número de socio que desea modificar: "))
        if numeroSocio in socios:
            modificar = input("Describa el campo que quiere modificar:\n1-Modificar nombre\n2-Modificar apellido\n3-Modificar fecha de ingreso\n4-Modificar cuota al día\n:")        

            if modificar == "1":
                nombre = input("Ingrese un nombre: ").lower().capitalize()
                socios[numeroSocio]["nombre"] = nombre
            elif modificar == "2":
                apellido = input("Ingrese su apellido: ").lower().capitalize()
                socios[numeroSocio]["apellido"] = apellido
            elif modificar == "3":
                dia = input("Ingrese nuevo día: ")
                mes = input("Ingrese nuevo mes: ")
                anio = input("Ingrese nuevo año: ")
                fecha = f"{dia}/{mes}/{anio}"
                socios[numeroSocio]["fecha de ingreso"] = fecha
            elif modificar == "4":
                cuota = input("¿Cuota al día? (s/n): ").lower()
                if cuota == "s":
                    print(f"Cuota registrada como pagada para el socio número {numeroSocio}.")
                socios[numeroSocio]["cuota al día"] = cuota

            print(f"Datos actualizados: {socios[numeroSocio]}")

        else:
            print(f"El socio número {numeroSocio} no está registrado en el sistema.")

    #Dar de baja eliminar
    elif opcion == "4":
        print("Para dar de baja a un socio, necesito su Nombre y Apellido.")
        nombre = input("Ingrese un nombre: ").lower().capitalize()
        apellido = input("Ingrese su apellido: ").lower().capitalize()
        encontrado = False
        for numero in socios:
            socio = socios[numero]
            if socio["nombre"] == nombre and socio["apellido"] == apellido:
                del socios[numero]
                print(f"Se dio de baja a Apellido: {socio["apellido"]}, Nombre: {socio["nombre"]}.")
                encontrado = True
                break
        if not encontrado:
            print("Socio no encontrado.")

    #Buscar socio
    elif opcion == "5":
        dato = ""
        buscar = input("Buscar socio registrado, ingresa una opción:\n1-Buscar por número de socio\n2-Buscar por nombre\n3-Buscar por apellido\n")

        if buscar == "1":
            # Buscar por número de socio
            numeroBusqueda = int(input("Ingrese el número de socio: "))
            if numeroBusqueda in socios:
                socio = socios[numeroBusqueda]
                print(f"Socio encontrado: Número {socio["numero"]}, Nombre: {socio["nombre"]}, Apellido: {socio["apellido"]}, Fecha de ingreso: {socio["fecha de ingreso"]}, Cuota al día: {socio["cuota al día"]}")
            else:
                print("No se encontró ningún socio con ese número.")

        elif buscar == "2":
            # Buscar por nombre
            nombreBusqueda = input("Ingrese el nombre del socio: ").lower().capitalize()
            encontrado = False
            for numero in socios:
                if socios[numero]["nombre"] == nombreBusqueda:
                    socio = socios[numero]
                    print(f"Socio encontrado: Número {socio["numero"]}, Nombre: {socio["nombre"]}, Apellido: {socio["apellido"]}, Fecha de ingreso: {socio["fecha de ingreso"]}, Cuota al día: {socio["cuota al día"]}")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún socio con ese nombre.")
        
        elif buscar == "3":
            # Buscar por apellido
            apellidoBusqueda = input("Ingrese el apellido del socio: ").lower().capitalize()
            encontrado = False
            for numero in socios:
                if socios[numero]["apellido"] == apellidoBusqueda:
                    socio = socios[numero]
                    print(f"Socio encontrado: Número {socio["numero"]}, Nombre: {socio["nombre"]}, Apellido: {socio["apellido"]}, Fecha de ingreso: {socio["fecha de ingreso"]}, Cuota al día: {socio["cuota al día"]}")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró ningún socio con ese apellido.")
        
        else:
            print("Opción no válida.")

    #Mostrar todos los socios
    elif opcion == "6":
        for numero in socios:
            print(f"Socio: {socios[numero]["numero"]}, Nombre: {socios[numero]["nombre"]}, Apellido: {socios[numero]["apellido"]}, Fecha de ingreso: {socios[numero]["fecha de ingreso"]}, Cuota al día: {socios[numero]["cuota al día"]}")
            print(" ")

    #Salir
    elif opcion == "0":
        print("Que tenga un buen día.")

    else:
        print("La opción ingresada es invalida, por favor vuelva a intentarlo.")
