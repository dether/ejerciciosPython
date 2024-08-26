"""Cuatro enteros entre 0 y 100 representan las notas de un estudiante de un curso de informática. 
Escribir un programa para pida estas cuatro notas y, calculando el promedio de ellas, muestre la calificación que le corresponde según la siguiente tabla:
  Promedio  |  Calificación 
   90-100   |       A
   80-89    |       B
   70-79    |       C
   60-69    |       D
   0-59     |       E
"""
nroNotas = 4
totalNotas = 0
i = 1

while i != 5:
  nota = int(input(f"Ingrese la {i}° nota (entre 0 y 100): "))
  if nota < 0 or nota > 100:
    print("Ingrese una nota entre 0 y 100.")
  else:
    totalNotas = totalNotas + nota
    i = i + 1

promedio = totalNotas/nroNotas

if promedio == 100:
  print(f"   Promedio    |  Calificación \n      {promedio}    |       A       ")
elif promedio > 89:
  print(f"   Promedio    |  Calificación \n      {promedio}     |       A       ")
elif promedio > 79 and promedio < 90:
  print(f"   Promedio    |  Calificación \n      {promedio}     |       B       ")
elif promedio > 69 and promedio < 80:
  print(f"   Promedio    |  Calificación \n      {promedio}     |       C       ")
elif promedio > 59 and promedio < 70:
  print(f"   Promedio    |  Calificación \n      {promedio}     |       D       ")
else:
  print(f"   Promedio    |  Calificación \n      {promedio}     |       E       ")

