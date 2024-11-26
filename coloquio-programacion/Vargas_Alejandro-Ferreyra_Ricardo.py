# Constantes
NOMBRE_ARCHIVO = "F1_2024.txt"
POSICIONES_PUNTAJES = {
    "1": 25,
    "2": 18,
    "3": 15,
    "4": 12,
    "5": 10,
    "6": 8,
    "7": 6,
    "8": 4,
    "9": 2,
    "10": 1,
}


# Abrir archivo '.txt'
archivo = open(NOMBRE_ARCHIVO)


# Utilidades
def obtenerPosiciones(linea):
    posiciones = []

    i = 52
    j = 54

    while True:
        posiciones.append(int(linea[i:j]))
        i += 12
        j += 12

        if j > 294:
            break

    return posiciones


def longitud(iterable):
    cantidad = 0

    for i in iterable:
        cantidad += 1

    return cantidad


def bubbleSort(lista):
    long = longitud(lista)

    for i in range(long):
        for j in range(0, long - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


# Funcion 1
def pilotoPuntaje():
    clasificacion = []

    for indice, linea in enumerate(archivo):
        sumaPuntajes = 0

        if indice >= 1:
            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones = obtenerPosiciones(linea)

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if str(posicion) in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[str(posicion)]

            # Recuperamos el nombre del piloto
            piloto = linea[0:12].strip()

            # Agregar el competidor con su puntaje a la lista
            clasificacion.append((piloto, sumaPuntajes))

    listaOrdenada = bubbleSort(clasificacion)

    if listaOrdenada:
        print("Pilotos     -    Puntajes")

        for i in range(longitud(listaOrdenada)):
            print(f"{listaOrdenada[i][0]:11s} -      {listaOrdenada[i][1]:3n}")
    else:
        print("No hay registro de pilotos.")


# Funcion 2
def equipoPuntaje():
    clasificacion = []
    equiposPuntajes = []

    for indice, linea in enumerate(archivo):
        sumaPuntajes = 0
        posiciones = []

        if indice >= 1:
            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones = obtenerPosiciones(linea)

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if str(posicion) in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[str(posicion)]

            # Recuperamos el nombre del competidor
            equipo = linea[12:48].strip()

            # Agregar el competidor con su puntaje a la lista
            clasificacion.append((equipo, sumaPuntajes))

    # Filtrar los nombres que se repiten
    for equipo, valor in clasificacion:
        encontrado = False

        for i in range(longitud(equiposPuntajes)):
            if equiposPuntajes[i][0] == equipo:
                aux = equiposPuntajes[i][1] + valor
                equiposPuntajes[i] = (equipo, aux)
                encontrado = True
                break

        if not encontrado:
            equiposPuntajes.append((equipo, valor))

    listaOrdenada = bubbleSort(equiposPuntajes)

    if listaOrdenada:
        print("Equipos                        -    Puntajes")
        for i in range(longitud(listaOrdenada)):
            print(f"{listaOrdenada[i][0]:30s} -      {listaOrdenada[i][1]:3n}")
    else:
        print("No hay registro de equipos.")


# Función 3
def promedioPuntos():
    clasificacion = []

    for indice, linea in enumerate(archivo):
        sumaPuntajes = 0
        posiciones = []
        cantidad = 0

        if indice >= 1:
            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones = obtenerPosiciones(linea)

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if posicion > 0:
                    cantidad += 1

                if str(posicion) in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[str(posicion)]

            # Recuperamos el nombre del piloto
            piloto = linea[0:12].strip()

            # Validacion del promedio
            if cantidad > 0:
                promedio = sumaPuntajes / cantidad
            else:
                print(f"El competidor '{piloto}' no tiene ninguna cerrera registrada.")

            # Agregar el competidor con su puntaje a la lista
            clasificacion.append((piloto, promedio))

    listaOrdenada = bubbleSort(clasificacion)

    if listaOrdenada:
        print("Pilotos     -    Promedios")

        for i in range(longitud(listaOrdenada)):
            print(f"{listaOrdenada[i][0]:11s} -      {listaOrdenada[i][1]:3.2f}")
    else:
        print("No hay registro de pilotos.")


# Función 4
def mejorPosicion():
    clasificacion = []

    for indice, linea in enumerate(archivo):
        posiciones = []

        if indice >= 1:
            mayorPosicion = float("inf")

            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones = obtenerPosiciones(linea)

            # Recuperamos el nombre del piloto
            piloto = linea[0:12].strip()

            for posicion in posiciones:
                if posicion > 0 and posicion < mayorPosicion:
                    mayorPosicion = posicion

            # Agregamos el piloto con su mayor posicion
            clasificacion.append((piloto, mayorPosicion))

            long = longitud(clasificacion)

            for i in range(long):
                for j in range(0, long - i - 1):
                    if clasificacion[j][0] > clasificacion[j + 1][0]:
                        aux = clasificacion[j]
                        clasificacion[j] = clasificacion[j + 1]
                        clasificacion[j + 1] = aux

    if clasificacion:
        print("Pilotos     -    Mejor Posición")
        for i in range(longitud(clasificacion)):
            print(f"{clasificacion[i][0]:11s} -      {clasificacion[i][1]:5n}")
    else:
        print("No hay registro de pilotos.")


# Menu
while True:
    try:
        print("<------ Menu de opciones ------>")
        print("1. Listado con el total de puntos de cada piloto.")
        print("2. Listado de puntos de cada equipo, ordenado de mayor a menor.")
        print("3. Promedio de puntos de cada piloto.")
        print("4. Mejor posición obtenida por cada piloto en orden alfabético.")
        print("0. Salir.")

        opcion = int(input("Ingrese una opción: "))
        archivo.seek(0)

        if opcion == 0:
            print("Hasta luego...")
            archivo.close()
            break
        elif opcion == 1:
            pilotoPuntaje()
        elif opcion == 2:
            equipoPuntaje()
        elif opcion == 3:
            promedioPuntos()
        elif opcion == 4:
            mejorPosicion()
        else:
            print("Opción incorrecta, Debe ingresar una opción entre (0 y 4).")
    except ValueError:
        print("Opción inválida, vuelva a intentarlo.")