"""Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen respectivamente $270, $340 y $590. La máquina acepta y da de vuelto monedas de $5 y $10, y billetes de $20, $50, $100, $200, $500 y $1000.
Escriba un programa que pida al usuario elegir el producto y la cantidad que lleva, y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio del producto, el programa debe entregar las monedas de vuelto, una por una.
    
    Elija producto: A
    Cantidad: 1
    Total: $270
    Ingrese pago:
    100
    100
    100
    Su vuelto:
    10
    10
    10

    Elija producto: B
    Cantidad: 2
    Total: $680
    Ingrese pago:
    200
    200
    200
    100
    Su vuelto:
    20

    Elija producto: C
    Cantidad: 2
    Total: $1180
    Ingrese pago:
    1000
    500
    Su vuelto:
    200
    100
    20"""

valor = False
changuito = 0
total = 0
valores = [1000, 500, 200, 100, 50, 20, 10, 5]
continuar =""

while not valor:
    producto = input("Elija un producto: ").lower()
    if producto == "a":
        cantidad = int(input("Cantidad: "))
        changuito= changuito + (270*cantidad)
        print(f"Total: ${changuito}")
        
    elif producto == "b":
        cantidad = int(input("Cantidad: "))
        changuito = changuito + (340*cantidad)
        print(f"Total: ${changuito}")

    elif producto == "c":
        cantidad = int(input("Cantidad: "))
        changuito = changuito + (590*cantidad)
        print(f"Total: ${changuito}")
    else:
        continuar = input("La opción elegida es invalida. Desea seguir agregando productos? Y/N: ").lower()
        if continuar == "n":
            valor = True
i = 0
print(f"Total: ${changuito}")
while changuito > total:
    pago = int(input("Ingrese pago: "))

    if pago in valores:
        total += pago
    else:
        print("Solo se aceptan monedas de $5 o $10 y billetes de $20, $50, $100, $200, $500 y $1000.")

vuelto = total - changuito

if vuelto > 0:
    print("Su vuelto: ")
else:
    print("Gracias por su compra.")

while vuelto > 0:
    for d in valores:
        while vuelto >= d:
            vuelto -= d
            print(d)
""" while vuelto != 0:
    if (vuelto - 500 >= 0):
        vuelto = vuelto - 500
        print("500")
    elif (vuelto - 200 >= 0):
        vuelto = vuelto - 200
        print("200")
    elif (vuelto - 100 >= 0 ):
        vuelto = vuelto -100
        print("100")
    elif (vuelto - 50 >= 0):
        vuelto = vuelto - 50
        print("50")
    elif(vuelto - 20 >= 0):
        vuelto = vuelto - 20
        print("20")
    elif (vuelto -10 >= 0):
        vuelto = vuelto - 10
        print("10")
    elif (vuelto - 5 == 0):
        vuelto = vuelto -5
        print("5") """
