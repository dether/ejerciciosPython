print(" Escriba un programa que lea las calificaciones de los alumnos de una clase. Las calificaciones se leen desde teclado y son número enteros del 1 al 10. Se deja de ingresar calificaciones cuando el usuario ingresa el valor 0 (cero). Una vez ingresadas las calificaciones debe mostrar el promedio y la cantidad de calificaciones en la siguiente escala cualitativa:Insuficiente (calificaciones menores a 6), Bueno (5-6-7), Muy Bueno (8-9), Excelente (10) ")
cantidad = 0
total = 0
insuficiente = 0
bueno = 0
muyBueno = 0
excelente = 0
nota = 1
while nota != 0:
  nota = int(input("Ingrese una calificación: "))
  if nota > 0 & nota < 11:
    cantidad = cantidad + 1
    total = total + nota
    if nota < 6:
      insuficiente = insuficiente + 1
    elif nota < 8:
      bueno = bueno + 1
    elif nota < 10:
      muyBueno = muyBueno + 1
    else:
      excelente = excelente + 1
  elif nota > 10:
    print("La nota ingresada debe respetar los rangos entre los valores 1 - 10.")

print("El promedio es:", (total/cantidad))
print("Insuficiente:", insuficiente)
print("Bueno:", bueno)
print("Muy Bueno:",muyBueno)
print("Excelente:", excelente)
