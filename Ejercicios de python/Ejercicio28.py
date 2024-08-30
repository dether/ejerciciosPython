"""Años Bisiestos. Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la diferencia es de más o menos un cuarto de día. Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados. Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400. 
Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
Ingrese un anno: 1988
1988 es bisiesto
Ingrese un anno: 2011
2011 no es bisiesto
Ingrese un anno: 1700
1700 no es bisiesto
Ingrese un anno: 1500
1500 es bisiesto
Ingrese un anno: 2400
2400 es bisiesto"""

añoActual = int(input("Ingrese un año: "))
#año juliano < 1582 
# Bisiesto = tiene que ser divisible por 4
#año gregoriano > 1581.
# Bisiesto = (tiene que ser divisible por 400) o ((divisible por 4) y (no divisible por 100))
if añoActual < 1582:
    if añoActual % 4 == 0:
        print(f"El año ingresado:{añoActual}. Pertenece al Calendario Juliano y es bisiesto.")
    else:
        print(f"El año ingresado {añoActual}. Pertenece al Calendario Juliano y  no es bisiesto.")
elif añoActual > 1581:
    if (añoActual % 400 == 0) or ((añoActual % 4 == 0) and not (añoActual % 100 == 0)):
        print(f"El año ingresado:{añoActual}. Pertenece al Calendario Gregoriano y es bisiesto.")
    else:
        print(f"El año ingresado {añoActual}. Pertenece al Calendario Gregoriano y no es bisiesto.")

