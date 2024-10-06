segundos = 14550 #3hrs
horas = 0
minutos = 0
if segundos:
    minutos = int(segundos / 60)
    segundos = segundos - (minutos * 60)
    horas = int(minutos / 60)
    minutos =  minutos - (horas * 60)
print(horas)
print(minutos)
print(segundos)

mensaje = "a"
if mensaje:
    print("no hay mensaje")
    print(mensaje.upper())


