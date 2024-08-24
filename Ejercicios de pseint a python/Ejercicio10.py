print("Diseñar un algoritmo que convierta y muestre una temperatura ingresada en ºCelsius a ºFahrenheit. ")

#T °F = (1.8 * °C) + 32

temperatura = float(input("Ingrese una temperatura en °Celsius: "))
conversion = float((1.8 * temperatura) + 32)
print("La temperatura ingresada es:", temperatura, "°C")
print("La temperatura en °Fahrenheit es:", conversion,"°F")