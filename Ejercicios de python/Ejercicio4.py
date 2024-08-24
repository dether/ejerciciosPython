print("Escribir un programa que solicite al usuario la longitud y anchura de un rectángulo y a continuación visualice su superficie con cuatro decimales")

longitud = float(input("Ingrese la longitud del rectángulo: "))
anchura = float(input("Ingrese la anchura del rectángulo: "))

superficie = float(longitud * anchura)

print(f"El área del rectángulo con longitud {longitud} y anchura {anchura} es {superficie:.4f}.")