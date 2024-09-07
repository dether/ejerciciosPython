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
futurosMovimientos = []

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
            futurosMovimientos.append([filaNueva, columnaNueva])

    n = len(futurosMovimientos)

    for i in range(n):
        for j in range(0, n-i-1):
            # Comparamos por fila, y si las filas son iguales, comparamos por columna
            if futurosMovimientos[j][0] > futurosMovimientos[j+1][0] or (futurosMovimientos[j][0] == futurosMovimientos[j+1][0] and futurosMovimientos[j][1] > futurosMovimientos[j+1][1]):
                # Intercambiamos los pares si es necesario
                futurosMovimientos[j], futurosMovimientos[j+1] = futurosMovimientos[j+1], futurosMovimientos[j]

    # Imprimir los pares ordenados
    for par in futurosMovimientos:
        print(par[0], par[1])

        #con sorted
    """ futurosMovimientosOrdenados = sorted(futurosMovimientos)

    for fila, columna in futurosMovimientosOrdenados:
        print(fila, columna) """

