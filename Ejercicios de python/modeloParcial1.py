""" Desarrolle un programa que permita cargar los nombres y notas de n alumnos (dejando de ingresar datos cuando se ingresa un nombre en blanco). Los nombres se deben cargar en una lista y las notas en otra. Las notas solo deben permitir número enteros entre 1 y 10.
Una vez cargados los datos, debe mostrar el siguiente menú
----------------
1- Porcentaje de alumnos aprobados.
2- Promedio de notas.
3- Listado de nombre y nota de los alumnos desaprobados.
0- Salir.
Ingrese la opción: 

Realizar un función para cada opción que deben realizar lo siguiente (las funciones deben recibir como argumento las listas de nombres y/o notas) :
1- Porcentaje de alumnos aprobados. Muestra el porcentaje de alumnos aprobados. Aprueban 
aquellos alumnos que tienen nota 6 o más.
2- Promedio de notas. Calcula y muestra el promedio de las notas de los alumnos.
3- Listado de nombre y nota de los alumnos desaprobados. 
Luego de ejecutar cada opción (excepto la 0) debe volver al menú. """
def porcentajeAprobados(notas:list[int]) -> float:
    cantidad = 0
    cantidadAprobados = 0
    for nota in notas:
        cantidad += 1
        if nota > 5:
            cantidadAprobados += 1  
    resultado = cantidadAprobados / cantidad * 100
    return resultado

def promedioNotas(notas:list[int]) -> float:
    cantidad = 0
    sumaNotas = 0
    for nota in notas:
        cantidad += 1
        sumaNotas =  sumaNotas + nota
    resultado = sumaNotas / cantidad
    return resultado
#3- Listado de nombre y nota de los alumnos desaprobados. 
def  listado_desaprobados(nombres:list[str], notas:list[int]) -> print:
    cantidad = 0
    for elementos in nombres:
        cantidad += 1
    print(f"Nombre - Notas ")
    for i in range(cantidad):
        if notas[i] < 6:
            print(f" {nombres[i]} - {notas[i]} ")
nombres:list[str] = []
notas: list[int] = []
while True:
    nombre = input("Ingresa un nombre: ").lower().capitalize()
    if not nombre:
        break
    nombres.append(nombre)
    
    while True:
        try:
            nota = int(input(f"Ingresa la nota de {nombre}: "))
            if nota not in range(1,11):
                print("Ingrese una edad valida, entre (1 - 10)")
            else:
                notas.append(nota)
                break
        except:
            print("Error, ingrese un número entero.")
print(nombres)
print(notas)
while True:
    try:
        print("""
        MENU:
        1- Porcentaje de alumnos aprobados.
        2- Promedio de notas.
        3- Listado de nombre y nota de los alumnos desaprobados.
        0- Salir.
        """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print(f"Porcentaje de alumnos aprobados: {porcentajeAprobados(notas)} %")
        elif opcion == 2:
            print(f"Promedio de notas: {promedioNotas(notas)}")
        elif opcion == 3:
            listado_desaprobados(nombres,notas)
        elif opcion == 0:
            print("Hasta luego.")
            break
        else:
            print("Opcion incorrecta, ingrese uno de los siguientes valores (1 - 2 - 3 - 0)")
    except:
        print("Opción invalida. Intentelo de nuevo.")

