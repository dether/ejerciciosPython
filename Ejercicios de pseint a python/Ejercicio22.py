print("Escribir un programa que muestre los primeros n números primos, comenzando en 1.")

maximo = int(input("Ingrese un número: "))
primos = []
i = 2

while len(primos) < maximo:
    primo = True
    for divisor in range(2, int(i**0.5) + 1):
        if i % divisor == 0:
            primo = False
    
    if primo:
        primos.append(i)
    i += 1

print(primos)
