"""Un profesor necesita que escribamos un programa que lea las calificaciones de un parcial de los alumnos de una clase (la cantidad de alumnos no es fija), luego de ingresar la nota del último alumno se finaliza ingresando 0.
Las calificaciones se leen desde teclado y solo permiten números enteros entre 1 y 10. Utilizar lista.
Al ejecutar el programa debe solicitar el ingreso de las notas, y una vez finalizado el ingreso de las notas, el programa deberá mostrar:

    a. Promedio de notas con dos decimales.
    b. Cantidad de alumnos aprobados (que sacaron nota mayor o igual a 6)
    c. Un histograma como el ejemplo, donde la cantidad de * indica la cantidad de veces que apareció cada nota. Un histograma es un gráfico que muestra la frecuencia con que aparecen valores en un conjunto dado.

Por ejemplo, si las notas fueron los siguientes valores:
6 4 1 9 7 5 4 1 9 6 4 5 9 6 7 10 la salida sería:

    El promedio es 5.81
    Aprobaron 9 alumnos de 16 evaluados.
    El histograma es:
    1   **
    2 
    3 
    4   ***
    5   **
    6   ***
    7   **
    8 
    9   ***
    10  *
    Esto indica que dos personas sacaron 1, nadie sacó 2 ni 3, tres personas sacaron 4, …. Cada * indica la cantidad de alumnos que sacaron cada nota. 
"""
contador = 0
acumulador = 0
calificacion = 1
aprobados = 0
histograma = {i: 0 for i in range(1, 11)} #creamos un diccionario con 10 valores, cada valor vale 0.
while calificacion != 0:
    calificacion = int(input("Ingrese una nota: "))
    if 0 < calificacion < 11:
        contador = contador + 1
        acumulador = acumulador + calificacion
        histograma[calificacion] += 1
        if calificacion >= 6:
            aprobados += 1

    elif calificacion == 0:
        break
    else:
        print("La calificación ingresada es invalida, ingrese valores de 1 a 10, o 0 para salir.")

promedio = acumulador / contador
print(f"El promedio es {promedio:.2f} ")
print(f"Aprobaron {aprobados} alumnos de {contador} evaluados.")
print(f"El histograma es:")
#6 4 1 9 7 5 4 1 9 6 4 5 9 6 7 10
for nota in range(1, 11):
    print(f"{nota:<3} {'*' * histograma[nota]}")
