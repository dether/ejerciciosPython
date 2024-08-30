print("""En una carrera que tiene varios tramos, el ganador es aquel competidor que tarda menos en 
llegar a la meta. Se mide el tiempo que tarda cada corredor en realizar cada tramo, esta medición se toma en minutos. La cantidad de tramos no es fija.
Desarrolle un programa que permita ingresar los tiempos de un corredor de cada tramo y entregue como resultado el tiempo total de carrera en formato horas:minutos.
El programa deja de pedir tiempos de tramos cuando se ingresa un 0.
    Duracion tramo: 15
    Duracion tramo: 30
    Duracion tramo: 87
    Duracion tramo: 0
    Tiempo total de viaje: 2:12 horas
    Duracion tramo: 51
    Duracion tramo: 17
    Duracion tramo: 0
    Tiempo total de viaje: 1:08 horas""")

tramo = 1
minutos = 0
horas = 0

while tramo != 0:
    tramo = int(input("Ingrese la duración por tramo: "))
    minutos = minutos + tramo
  
while minutos > 59:
    if minutos > 59:
        horas = horas + 1
        minutos = minutos - 60

print(f"Tiempo total de viaje: {horas}:{minutos} horas.")