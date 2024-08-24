print("""
      Crear un algoritmo que permita ingresar una longitud, su unidad de medida y la unidad de medida a la que se quiere convertir (las unidades de medidas posibles son: mm, cm, dm, m, dam, hm, km). Debe mostrar como resultado la longitud ingresada expresada en la nueva unidad de medida. 
  Ejemplo: 
    ◦ Longitud: 248, 
    ◦ Unidad de medida: cm, 
    ◦ Convertir a: hm       
    ◦ Resultado: 0.0248 hm
    """)
longitud = float(input("Ingrese una longitud: "))
unidad = str(input("Ingrese la unidad de medida: "))
convertir = str(input("Ingrese la unidad de medida a convertir: "))

if unidad == "mm":
  if convertir == "cm":
    resultado = longitud/10
  elif convertir == "dm":
    resultado = longitud/100
  elif convertir == "m":
    resultado = longitud/1000
  elif convertir == "dam":
    resultado = longitud/10000
  elif convertir == "hm":
    resultado = longitud/100000
  elif convertir == "km":
    resultado = longitud/1000000

elif unidad == "cm":
  if convertir == "mm":
    resultado = longitud*10
  elif convertir == "dm":
    resultado = longitud/10
  elif convertir == "m":
    resultado = longitud/100
  elif convertir == "dam":
    resultado = longitud/1000
  elif convertir == "hm":
    resultado = longitud/10000
  elif convertir == "km":
    resultado = longitud/100000

elif unidad == "dm":
  if convertir == "mm":
    resultado = longitud*100
  elif convertir == "cm":
    resultado = longitud*10
  elif convertir == "m":
    resultado = longitud/10
  elif convertir == "dam":
    resultado = longitud/100
  elif convertir == "hm":
    resultado = longitud/1000
  elif convertir == "km":
    resultado = longitud/10000

elif unidad == "m":
  if convertir == "mm":
    resultado = longitud*1000
  elif convertir == "cm":
    resultado = longitud*100
  elif convertir == "dm":
    resultado = longitud*10
  elif convertir == "dam":
    resultado = longitud/10
  elif convertir == "hm":
    resultado = longitud/100
  elif convertir == "km":
    resultado = longitud/1000

elif unidad == "dam":
  if convertir == "mm":
    resultado = longitud*10000
  elif convertir == "cm":
    resultado = longitud*1000
  elif convertir == "dm":
    resultado = longitud*100
  elif convertir == "m":
    resultado = longitud*10
  elif convertir == "hm":
    resultado = longitud/10
  elif convertir == "km":
    resultado = longitud/100

elif unidad == "hm":
  if convertir == "mm":
    resultado = longitud*100000
  elif convertir == "cm":
    resultado = longitud*10000
  elif convertir == "dm":
    resultado = longitud*1000
  elif convertir == "m":
    resultado = longitud*100
  elif convertir == "dam":
    resultado = longitud*10
  elif convertir == "km":
    resultado = longitud/10

elif unidad == "km":
  if convertir == "mm":
    resultado = longitud*1000000
  elif convertir == "cm":
    resultado = longitud*100000
  elif convertir == "dm":
    resultado = longitud*10000
  elif convertir == "m":
    resultado = longitud*1000
  elif convertir == "dam":
    resultado = longitud*100
  elif convertir == "hm":
    resultado = longitud*10

print("Longitud:", longitud)
print("Unidad de medida:", unidad)
print("Convertir a:", convertir)
print("Resultado:", resultado, "", convertir)
