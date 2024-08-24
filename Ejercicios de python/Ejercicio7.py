print("""Una temperatura Celsius (centígrados) C puede ser convertida a una temperatura equivalente a F (Fahrenheit)  de acuerdo a la siguiente formula: f = (9/5)c+32
Escribir un programa que lea una temperatura de Celsius como número decimal y obtenga la temperatura Fahrenheit equivalente.""")

temperatura = int(input("Ingrese una temperatura: "))

equivalencia = (9/5)*temperatura+32

print(f"La temperatura Fahrenheit equivalente es: {equivalencia} F°")
