"""Un alumno desea saber que nota necesita en el tercer parcial para aprobar. El promedio se calcula con la siguiente formula.
NP=(P1+P2+P3)/3
NF=NP⋅0.7+NL⋅0.3
Donde NP es el promedio de parciales, NL el promedio de prácticos y N F la nota final.
Escriba un programa que pregunte al usuario las notas de los dos primeros parciales y la nota promedio de prácticos, y muestre la nota que necesita el alumno para aprobar la materia con nota final 60.
Ingrese nota parcial 1: 45
Ingrese nota parcial 2: 55
Ingrese nota prácticos: 65
Necesita nota 74 en el parcial 3
"""

p1 = int(input("Ingrese la primer nota del parcial: "))
p2 = int(input("Ingrese la segunda nota del parcial: "))
practicos = int(input("Ingrese la nota promedio de prácticos: "))
print("Vamos a calcular que nota debe sacarse en el parcial 3...")
# Se aprueba con un 60, entonces la formula seria la siguiente:
# (((P1+P2+P3)/3)*0.7) + (practicos*0.3) = 60
# Al tener todos los valores, despejamos P3
# P3 = (((60 -(practicos*0.3))/0.7)*3) - p1 - p2
p3 = (((60 -(practicos*0.3))/0.7)*3) - (p1+p2)

print(f"Necesita nota {round(p3)} en el parcial 3")

