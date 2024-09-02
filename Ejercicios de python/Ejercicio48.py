"""Un tablero de ajedrez es una grilla de 8 * 8 casillas. Cada celda puede ser representada mediante las coordenadas de su fila y su columna, numeradas desde 1 hasta 8.
El caballo es una pieza que se desplaza en forma de L: su movimiento consiste en avanzar dos casillas en una dirección y luego una casilla en una dirección perpendicular a la primera:
Escriba un programa que reciba como entrada las coordenadas en que se encuentra un caballo, y entregue como salida todas las casillas hacia las cuales el caballo puede desplazarse.
Todas las coordenadas mostradas deben estar dentro del tablero.
Si la coordenada ingresada por el usuario es inválida, el programa debe indicarlo.

    Ingrese coordenadas del caballo.
    Fila: 2
    Columna: 8
    El caballo puede saltar de 2 8 a:
    1 6
    3 6
    4 7
    
    Ingrese coordenadas del caballo.
    Fila: 3
    Columna: 4
    El caballo puede saltar de 3 4 a:
    1 3
    1 5
    2 2
    2 6
    4 2
    4 6
    5 3
    5 5

    Ingrese coordenadas del caballo.
    Fila: 1
    Columna: 9
    Posición invalida."""
print("Ingrese coordenadas del caballo.")
fila = int(input("Fila: "))
columna = int(input("Columna: "))
# anoto todos los posibles movimientos. 
movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)]
movimientos = [(-1, -2), (-1, 2), (1, -2),(1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

if ((fila > 8) or (fila < 1)) or ((columna < 1) or columna > 8):
    print("Posición invalida.")
else:
    print(f"El caballo puede saltar de {fila} {columna} a: ")
    # Cada i=[()...()] i representa los parentesis
    # el 0 y 1 representa la posición dentro de cada parentesis. 
    for i in movimientos:
        filaNueva = fila + i[0]
        columnaNueva = columna + i[1]
        if 0 < filaNueva < 9 and 0 < columnaNueva < 9:
            print(filaNueva, columnaNueva)

""" if ((fila > 8) or (fila < 1)) or ((columna < 1) or columna > 8):
    print("Posición invalida.")
else:
    print(f"El caballo puede saltar de {fila} {columna} a: ")
    if (((fila - 2) > 0) and ((columna + 1) < 9)):
        print(fila-2, columna+1)

    if (((fila - 2) > 0) and ((columna - 1 > 0))):
        print(fila-2, columna-1)

    if (((columna - 2) > 0) and ((fila + 1) < 9)):
        print(fila+1, columna-2)

    if (((columna - 2) > 0) and ((fila - 1 > 0))):
        print(fila-1, columna-2)

    if (((fila + 2) < 9) and ((columna + 1) < 9)):
        print(fila+2, columna+1)

    if (((fila + 2) < 9) and ((columna - 1) > 0)):
        print(fila+2, columna-1)

    if (((columna + 2) < 9) and ((fila + 1) < 9)):
        print(fila+1, columna+2)

    if (((columna + 2) < 9) and ((fila - 1) > 0)):
        print(fila-1, columna+2) """