from datetime import datetime
print("Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:")

añoNacimiento = int(input("Ingrese el año en el que nacio: "))
mesNacimiento = int(input("Ingrese el mes en el que nacio: "))
diaNacimiento = int(input("Ingrese el día en el que nacio: "))

fechaActual = datetime.now()
añoActual = fechaActual.year
mesActual = fechaActual.month
diaActual = fechaActual.day
edad = añoActual - añoNacimiento

if (mesActual < mesNacimiento) or (mesActual == mesNacimiento and diaActual < diaNacimiento):
    edad = edad - 1

print(f"Tu edad es: {edad}.")
