"""Un analista financiero lleva un registro del precio del dólar día a día, y desea saber cuál fue la mayor de las alzas en el precio diario a lo largo de ese período.
Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar para cada uno de los n días.
El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.
Si en ningún día el precio subió, la salida debe decir: No hubo alzas.
    Cuantos dias? 10
    Dia 1: 96.96
    Dia 2: 99.03
    Dia 3: 96.03
    Dia 4: 93.27
    Dia 5: 88.82
    Dia 6: 92.16
    Dia 7: 90.32
    Dia 8: 90.67
    Dia 9: 90.89
    Dia 10: 94.10
    La mayor alza fue de 3.34 pesos"""

nDias = int(input("Cuantos dias? "))
dolarDias = []
alzas = 0
maximo = 0

for i in range(1,nDias+1):
    dolar = float(input(f"Día {i}: "))
    dolarDias.append(dolar)

for element in range(nDias - 1):
    alzas = dolarDias[element+1] - dolarDias[element]
    if alzas > maximo:
        maximo = alzas

if maximo > 0:
    print(f"La mayor alza fue de {maximo:.2f} pesos.")
else:
    print("No hubo alzas.")