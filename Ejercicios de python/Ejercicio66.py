"""Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.- 
Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.- Informar qué nombres de nivel primario no se repiten en los de nivel secundario."""
nombrePrimaria = []
sinRepeticionesPrimaria = []
repeticiones = []
nombreSecundaria = []
sinRepeticionesSecundaria = []
noRepiten = []
nombre = ""
while nombre != "x":
    nombre = input("Ingrese nombre del alumno de primaria: ").lower()
    if nombre != "x":
        nombrePrimaria.append(nombre)
nombre = ""

while nombre != "x":
    nombre = input("Ingrese nombre del alumno de secundaria: ").lower()
    if nombre != "x":
        nombreSecundaria.append(nombre)

for pila in nombrePrimaria:
    esUnico = True
    for nom in sinRepeticionesPrimaria:
        if pila == nom:
            esUnico = False
    if esUnico:
        sinRepeticionesPrimaria.append(pila)

for pila in nombreSecundaria:
    esUnico = True
    for nom in sinRepeticionesSecundaria:
        if pila == nom:
            esUnico = False
    if esUnico:
        sinRepeticionesSecundaria.append(pila)

#se repiten entre primario y secundario
for pila in sinRepeticionesPrimaria:
    esUnico = False
    for nom in sinRepeticionesSecundaria:
        if pila == nom:
            esUnico = True
    if esUnico:
        repeticiones.append(pila)

#no se repiten entre primario y secundario
for pila in sinRepeticionesPrimaria:
    if pila not in sinRepeticionesSecundaria:
        noRepiten.append(pila)

print(f"Nombres de alumnos de nivel primario sin repeticiones: {sinRepeticionesPrimaria}")
print(f"Nombres de alumnos de nivel secundario sin repeticiones: {sinRepeticionesSecundaria}")
print(f"Nombres que se repiten entre nivel primario y secundario: {repeticiones}")
print(f"Nombres de nivel primario que no se repiten en nivel secundario: {noRepiten}")

