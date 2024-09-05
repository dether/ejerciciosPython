"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el total con 8 
dígitos enteros y 2 decimales."""

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese su precio: "))
unidades = int(input("Ingrese el número de unidades: "))
total = precio * unidades
print(f"Producto: {nombre.capitalize()}, Precio: $ {precio:09.02f}, Unidadades: {unidades:03.0f}, Total: {total:011.2f}")