"""Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). 
Ejemplo: 
[("Manuel Juarez", 19823451, "Liverpool"), 
("Silvana Paredes", 22709128, "Buenos Aires"), 
("Rosa Ortiz", 15123978, "Glasgow"), 
("Luciana Hernandez", 38981374, "Lisboa")] 
Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), 
("Liverpool","Inglaterra"), ("Madrid","España")] 
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, ver a qué ciudad viaja.
-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
-Dado el DNI de un pasajero, ver a qué país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa"""

pasajeros = []
proximosDestinos = []

opcion = 1
cantidad = 0
sinRegistro = True

while opcion != "0":
    print("1-Agregar pasajeros.")
    print("2-Agregar destinos favoritos: ")
    print("3-Ver ciudad destino / DNI.")
    print("4-Ver pasajeros a bordo / CIUDAD.")
    print("5-Ver país destino / DNI.")
    print("6-Ver pasajeros a bordo / PAÍS.")
    print("7-Ver lista de pasajeros y lista de destinos")
    print("0-Salir.")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("Vamos a requerir sus datos: ")
        nombre = input("Ingrese un nombre: ").lower().title()
        dni = int(input("Ingrese su DNI: "))
        destino = input("Ingrese su destino: ").lower().title()
        pasajeros.append((nombre, dni, destino))
        print(f"Se ha agregado un nuevo pasajero: {(nombre, dni, destino)}")

    elif opcion == "2":
        print("A que ciudad/país te gustaria viajar en un futuro?: ")
        ciudad = input("Ingrese la ciudad: ").lower().title()
        pais = input("Ingrese el pais: ").lower().title()
        proximosDestinos.append((ciudad, pais))
        print(f"Se ha agregado un nuevo destino a tus favoritos: {(ciudad, pais)}")

    elif opcion == "3":
        try:
            dni = int(input("Ingrese su DNI: "))
        except ValueError:
            print("Por favor, ingrese un número válido para el DNI.")
            continue
        sinRegistro = True
        for i in pasajeros:
            if i[1] == dni:
                mensaje = print(f"Pasajero {i[0]}\nDestino {i[2]}")
                sinRegistro = False
        if sinRegistro:
            print(f"No se encuentra registrado ningun pasajero con el DNI: {dni}")

    elif opcion == "4":
        ciudad = input("Ingrese la ciudad: ").lower().title()
        cantidad = 0
        for i in pasajeros:
            if i[2] == ciudad:
                cantidad = cantidad + 1 
        if cantidad > 0:
            print(f"La cantidad de pasajeros que viajan a {ciudad} es {cantidad} personas.")
        else:
            print(f"No hay nadie viajando a {ciudad} en este momento.")

    elif opcion == "5":
        try:
            dni = int(input("Ingrese su DNI: "))
        except ValueError:
            print("Por favor, ingrese un número válido para el DNI.")
            continue
        sinRegistro = True
        for i in pasajeros:
            if i[1] == dni:
                for j in proximosDestinos:
                    if j[0] == i[2]:
                        print(f"Pasajero {i[0]}\nPaís destino: {j[1]}")
                        sinRegistro = False
        if sinRegistro:
            print(f"No se encuentra registrado ningun pasajero con el DNI: {dni}")        
    
    elif opcion == "6":
        pais = input("Ingrese el pais: ").lower().title()
        cantidad = 0
        for i in proximosDestinos:
            if i[1] == pais:
                for j in pasajeros:
                    if i[0] == j[2]:
                        cantidad = cantidad +1
        if cantidad > 0:
            print(f"La cantidad de pasajeros que viajan a {pais} es {cantidad} personas.")
        else:
            print(f"No hay nadie viajando a {pais} en este momento.")

    elif opcion == "7":
        print(f"destinos: {proximosDestinos}")
        print(f"pasajeros: {pasajeros}")

    elif opcion == "0":
        print("Que tenga un buen día.")

    else:
        print("La opción ingresada es invalida, por favor vuelva a intentarlo.")


