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


archivo = open(NOMBRE_ARCHIVO)


# Utilidades
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
        posiciones = []
        if indice >= 1:
            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones.append(linea[48:61].strip())  # Bahréin
            posiciones.append(linea[61:70].strip())  # Arabia
            posiciones.append(linea[70:86].strip())  # Australia
            posiciones.append(linea[86:98].strip())  # Japón
            posiciones.append(linea[98:110].strip())  # China
            posiciones.append(linea[110:122].strip())  # Miami
            posiciones.append(linea[122:133].strip())  # Imola
            posiciones.append(linea[133:145].strip())  # Mónaco
            posiciones.append(linea[145:154].strip())  # Canadá
            posiciones.append(linea[154:168].strip())  # Barcelona
            posiciones.append(linea[168:177].strip())  # Austria
            posiciones.append(linea[177:192].strip())  # Inglaterra
            posiciones.append(linea[192:204].strip())  # Hungria
            posiciones.append(linea[204:215].strip())  # Bélgica
            posiciones.append(linea[215:229].strip())  # P. Bajos
            posiciones.append(linea[229:237].strip())  # Italia
            posiciones.append(linea[237:251].strip())  # Aserbajian
            posiciones.append(linea[251:265].strip())  # Singapur
            posiciones.append(linea[265:277].strip())  # EE.UU
            posiciones.append(linea[277:289].strip())  # México
            posiciones.append(linea[289:296].strip())  # Brasil

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if posicion in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[posicion]

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
            posiciones.append(linea[48:61].strip())  # Bahréin
            posiciones.append(linea[61:70].strip())  # Arabia
            posiciones.append(linea[70:86].strip())  # Australia
            posiciones.append(linea[86:98].strip())  # Japón
            posiciones.append(linea[98:110].strip())  # China
            posiciones.append(linea[110:122].strip())  # Miami
            posiciones.append(linea[122:133].strip())  # Imola
            posiciones.append(linea[133:145].strip())  # Mónaco
            posiciones.append(linea[145:154].strip())  # Canadá
            posiciones.append(linea[154:168].strip())  # Barcelona
            posiciones.append(linea[168:177].strip())  # Austria
            posiciones.append(linea[177:192].strip())  # Inglaterra
            posiciones.append(linea[192:204].strip())  # Hungria
            posiciones.append(linea[204:215].strip())  # Bélgica
            posiciones.append(linea[215:229].strip())  # P. Bajos
            posiciones.append(linea[229:237].strip())  # Italia
            posiciones.append(linea[237:251].strip())  # Aserbajian
            posiciones.append(linea[251:265].strip())  # Singapur
            posiciones.append(linea[265:277].strip())  # EE.UU
            posiciones.append(linea[277:289].strip())  # México
            posiciones.append(linea[289:296].strip())  # Brasil

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if posicion in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[posicion]

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
            posiciones.append(linea[48:61].strip())  # Bahréin
            posiciones.append(linea[61:70].strip())  # Arabia
            posiciones.append(linea[70:86].strip())  # Australia
            posiciones.append(linea[86:98].strip())  # Japón
            posiciones.append(linea[98:110].strip())  # China
            posiciones.append(linea[110:122].strip())  # Miami
            posiciones.append(linea[122:133].strip())  # Imola
            posiciones.append(linea[133:145].strip())  # Mónaco
            posiciones.append(linea[145:154].strip())  # Canadá
            posiciones.append(linea[154:168].strip())  # Barcelona
            posiciones.append(linea[168:177].strip())  # Austria
            posiciones.append(linea[177:192].strip())  # Inglaterra
            posiciones.append(linea[192:204].strip())  # Hungria
            posiciones.append(linea[204:215].strip())  # Bélgica
            posiciones.append(linea[215:229].strip())  # P. Bajos
            posiciones.append(linea[229:237].strip())  # Italia
            posiciones.append(linea[237:251].strip())  # Aserbajian
            posiciones.append(linea[251:265].strip())  # Singapur
            posiciones.append(linea[265:277].strip())  # EE.UU
            posiciones.append(linea[277:289].strip())  # México
            posiciones.append(linea[289:296].strip())  # Brasil

            # Sumar todas las posiciones de un comeptidor
            for posicion in posiciones:
                if int(posicion) > 0:
                    cantidad += 1

                if posicion in POSICIONES_PUNTAJES:
                    sumaPuntajes += POSICIONES_PUNTAJES[posicion]

            # Recuperamos el nombre del piloto
            piloto = linea[0:12].strip()

            # Promedio
            promedio = sumaPuntajes / cantidad
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
            # Recuperamos todas las posiciones de un competidor en los diferentes paises
            posiciones.append(linea[48:61].strip())  # Bahréin
            posiciones.append(linea[61:70].strip())  # Arabia
            posiciones.append(linea[70:86].strip())  # Australia
            posiciones.append(linea[86:98].strip())  # Japón
            posiciones.append(linea[98:110].strip())  # China
            posiciones.append(linea[110:122].strip())  # Miami
            posiciones.append(linea[122:133].strip())  # Imola
            posiciones.append(linea[133:145].strip())  # Mónaco
            posiciones.append(linea[145:154].strip())  # Canadá
            posiciones.append(linea[154:168].strip())  # Barcelona
            posiciones.append(linea[168:177].strip())  # Austria
            posiciones.append(linea[177:192].strip())  # Inglaterra
            posiciones.append(linea[192:204].strip())  # Hungria
            posiciones.append(linea[204:215].strip())  # Bélgica
            posiciones.append(linea[215:229].strip())  # P. Bajos
            posiciones.append(linea[229:237].strip())  # Italia
            posiciones.append(linea[237:251].strip())  # Aserbajian
            posiciones.append(linea[251:265].strip())  # Singapur
            posiciones.append(linea[265:277].strip())  # EE.UU
            posiciones.append(linea[277:289].strip())  # México
            posiciones.append(linea[289:296].strip())  # Brasil
            mayorPosicion = float("inf")

            # Recuperamos el nombre del piloto
            piloto = linea[0:12].strip()

            for posicion in posiciones:
                if int(posicion) > 0 and int(posicion) < mayorPosicion:
                    mayorPosicion = int(posicion)

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
        print("4. Mejor posicion obtenida por cada piloto en orden alfabético.")
        print("0. Salir.")

        opcion = int(input("Ingrese una opción: "))
        archivo.seek(0)
        if opcion == 0:
            print("Hasta luego...")
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
            print("Opción incorrecta, Debe ingresar una opcion entre (0 y 4).")
    except ValueError:
        print("Opción inválida, vuelva a intentarlo.")
