"""Desarrolle un programa que calcule el dígito verificador de un código.
Para calcular el dígito verificador, se deben realizar los siguiente pasos:
1. Obtener el código sin guion ni dígito verificador. 
2. Invertir el número. (ej: de 201012341 a 143210102). 
3. Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe comenzar de nuevo, por ejemplo, con 143210102: 
    num= 201012341
    1*2 + 4*3 + 3*4 + 2*5 + 1*6 + 0*7 + 1*2 + 0*3 + 2*4 = 52
4. Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
    52 % 11 = 8
5. Con el resultado obtenido en el paso anterior, debemos restarlo de 11:
    11 − 8 = 3
6. Finalmente, el dígito verificador será el obtenido en la resta de punto anterior, por lo cual el código con dígito verificador será: 201012341-3."""

#1
codigo = (input("Ingrese el codigo sin guion, ni digito verificador: "))
#2
reverse = ""
digitos = [2, 3, 4, 5, 6, 7]
total = 0
verificador = 0
for i in range(-len(codigo),0):
    #invertimos
    reverse = codigo[i] + reverse
#3
# num= 123, reverse= 321, i=0(posición), digito=3(toma el primer digito) 
for i in range(len(reverse)):
    digito = int(reverse[i])
    print(f"i: {i}, digito:{digito}")
    # factor = array[i%6] siempre va a dar valores de 0-5 incrementandose
    factor = digitos[i % len(digitos)]
    print(f"digitos:{digitos} [i:{i} % {len(digitos)} = {i%len(digitos)}], factor: {factor}")
    total = total + (digito * factor)
#4
total = total % 11
#5
verificador = 11 - total
print(f"El código con dígito verificador será: {codigo}-{verificador}")

    


