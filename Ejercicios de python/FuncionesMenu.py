"""Ejercicio 1:
Desarrolle un programa que permita cargar los nombres y edades de n personas (dejando de ingresar datos cuando se ingrese un nombre en blanco). Los nombres se deben cargar en una lista y las edades en otra. Las edades solo deben permitir números enteros mayores o iguales a 0.
Una vez cargados los datos, debe mostrar el siguiente menú:
MENÚ DE OPCIONES----------------
1- Cantidad de personas mayores de edad (18 años o más).
2- Edad promedio.
3- Listado de nombre y edad de las personas menores de edad.
0- Salir.
Ingrese la opción:

Realice una función para cada opción que deben realizar lo siguiente:
Cantidad de personas mayores de edad. Muestra la cantidad de personas que tienen 18 años o más.
Edad promedio. Calcula y muestra el promedio de las edades ingresadas.
Listado de nombre y edad de las personas menores de edad.
Luego de ejecutar cada opción (excepto la 0), debe volver al menú.
"""
def cantidadMayores(edades:list[int]) ->int:
    cantidad = 0
    for elemento in edades:
        if elemento > 17:
            cantidad += 1
    return cantidad

def promedioEdad(edades:list[int]) -> float:
    cantidad  = 0
    suma = 0
    for i in edades:
        suma = suma + i
        cantidad = cantidad + 1
    return suma / cantidad

def listadoMenores(nombres:list[str], edades:list[int]):
    cantidad = 0
    for elemento in edades:
        cantidad += 1
    print("Nombres y edades de los menores de edad:")
    for i in range(cantidad):
        if edades[i] < 18:
            print(f"{nombres[i]} - {edades[i]} años")
    
nombres = []
edades = []
print("Ingresa los datos")
while True:
    nombre = input("Ingrese un nombre:")
    if not nombre:
        break
    nombres.append(nombre)
    while True:
        try:
            edad = int(input(f"Ingrese la edad de {nombre}: "))
            if edad < 0 or edad > 100:
                continue
            else:
                edades.append(edad)
                break
        except:
            print("Error, ingrese una edad entre 1 - 100")


while True:
    try:
        print("""MENÚ DE OPCIONES----------------
        1- Cantidad de personas mayores de edad (18 años o más).
        2- Edad promedio.
        3- Listado de nombre y edad de las personas menores de edad.
        0- Salir.
        """)
        opcion = int(input("Ingrese la opción: "))

        if opcion == 1:
            print(f"La cantidad de personas mayores de edad (18 años o más) son: {cantidadMayores(edades)}")

        elif opcion == 2:
            print(f"El promedio de edades es: {promedioEdad(edades)}")

        elif opcion == 3:
            listadoMenores(nombres,edades)

        elif opcion == 0:
            print("Hasta luego.")
            break
        else:
            print("Opción incorrecta. Ingrese ( 1 - 2 - 3 - 0 )")

    except:
        print("Opción invalida.") 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
Ejercicio 2:
Desarrolle un programa que permita cargar los nombres y sueldos de n empleados (dejando de ingresar datos cuando se ingrese un nombre en blanco). Los nombres se deben cargar en una lista y los sueldos en otra. Los sueldos solo deben permitir números enteros mayores o iguales a 0.

Una vez cargados los datos, debe mostrar el siguiente menú:
MENÚ DE OPCIONES----------------
1- Porcentaje de empleados con sueldo superior a $50,000.
2- Promedio de sueldos.
3- Listado de nombre y sueldo de los empleados con sueldo inferior a $30,000.
0- Salir.
Ingrese la opción: 
Realice una función para cada opción que deben realizar lo siguiente:

Porcentaje de empleados con sueldo superior a $50,000. Muestra el porcentaje de empleados cuyo sueldo supera $50,000.
Promedio de sueldos. Calcula y muestra el promedio de los sueldos ingresados.
Listado de nombre y sueldo de los empleados con sueldo inferior a $30,000."""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""Ejercicio 3:
Desarrolle un programa que permita cargar los nombres y tiempos (en segundos) de n corredores en una carrera (dejando de ingresar datos cuando se ingrese un nombre en blanco). Los nombres se deben cargar en una lista y los tiempos en otra. Los tiempos solo deben permitir números enteros mayores que 0.

Una vez cargados los datos, debe mostrar el siguiente menú:
MENÚ DE OPCIONES----------------
1- Cantidad de corredores con tiempo menor a 10 segundos.
2- Tiempo promedio de la carrera.
3- Listado de nombre y tiempo de los corredores con tiempo mayor a 15 segundos.
0- Salir.
Ingrese la opción: 
Realice una función para cada opción que deben realizar lo siguiente:

Cantidad de corredores con tiempo menor a 10 segundos. Muestra la cantidad de corredores con un tiempo inferior a 10 segundos.
Tiempo promedio de la carrera. Calcula y muestra el tiempo promedio de todos los corredores.
Listado de nombre y tiempo de los corredores con tiempo mayor a 15 segundos."""
