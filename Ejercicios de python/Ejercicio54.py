"""La siguiente espiral de 5 * 5 se forma comenzando del número 1, y moviéndose a la derecha en el sentido de las agujas del reloj:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
La suma de las diagonales de esta espiral es 101.
Escriba un programa que entregue la suma de las diagonales en una espiral de m * m creada de la misma manera, habiendo ingresado m."""
#https://www.youtube.com/watch?v=SJifcarYTno tutorial del ejercicio
m = int(input("Ingrese m: "))
# creamos m matrices = [   [fila],      [fila],        [fila]]
#   [[f1],[f2],[f3]] = [[c0, c1, c2],[c0, c1, c2],[c0, c1, c2]]
matriz = [[0] * m for _ in range(m)]
# tengo que iniciar en f2[c1] con valor =1
valor = 1
""" ejemplo m =3
INDICE
    0     1   2
0   [c1, c2, c3]
1   [c1, c2, c3]
2   [c1, c2, c3]
"""
fila, columna = m//2, m//2      #ejemplo m =3
matriz[fila][columna] = valor
valor += 1
#               
movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]       
direccion = 0  # Comienza moviéndonos a la derecha 
pasos = 1# Cantidad de pasos a mover en una dirección antes de cambiar                                               

while valor <= m * m:
    for _ in range(2):  # Cada paso se repite dos veces (excepto la primera dirección)
        for _ in range(pasos):
            if valor > m * m:
                break
            fila += movimientos[direccion][0]
            columna += movimientos[direccion][1]
            matriz[fila][columna] = valor
            valor += 1
        direccion = (direccion + 1) % 4  # Cambia de dirección (circular)
    pasos += 1  # Aumenta el número de pasos en cada dirección

#imprimir matriz
ancho = 2  # Ancho de cada campo en la matriz
for fila in matriz:
    # Imprime cada fila con los elementos alineados
    print(''.join(f' {elem:>{ancho}}' for elem in fila))

# Calcula la suma de las diagonales
suma_diagonales = 0
for i in range(m):
    suma_diagonales += matriz[i][i]  # Diagonal principal
    suma_diagonales += matriz[i][m - 1 - i]  # Diagonal secundaria
    
# Si m es impar, la intersección de las diagonales se cuenta dos veces
if m % 2 == 1:
    fila_medio = m // 2
    suma_diagonales -= matriz[fila_medio][fila_medio]

print(f"La suma de las diagonales de esta espiral es {suma_diagonales}.")
"""
!2*2
1  2 
4  3
!3*3
7  8  9 
6  1  2 
5  4  3 
!4*4
7  8  9  10
6  1  2  11
5  4  3  12
16 15 14 13
!5*5
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
!6*6
21 22 23 24 25 26
20  7  8  9 10 27
19  6  1  2 11 28
18  5  4  3 12 29
17 16 15 14 13 30
36 35 34 33 32 31
"""