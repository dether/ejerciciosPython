"""
1. Cálculo de ganancias y margen de ganancia ¿Cuál es el producto con mayor margen de ganancia?
2. Filtro por distribuidor y cantidad para reponer ¿Cuántos productos cumplen con esta condición?
3. Promedio de precios de venta y compra por marca ¿Qué marca tiene el mayor promedio de venta?
4. Productos vendidos en un año específico ¿Cuántos productos diferentes fueron vendidos en el año 2020?
5. Promedio de cantidad de productos por distribuidor ¿Qué distribuidor tiene el mayor promedio de cantidad de productos?
6. Productos con precio de compra inferior a $400
7. Productos con mayor diferencia entre precios de compra y venta
8. Productos vendidos por un distribuidor específico
"""
#05062023   Impresora    SmartLine     729.13    402.36   75   Distribuidor B  
#fecha      0-8 
#producto  8-22
#marca     22-36
#venta     36-47
#compra    47-58
#canti    58-63
#distri   63-80

while True:
    try:
        #archivo para leer
        txt = "comercio.txt"

        #leemos el archivo y guardamos en la variable archivo
        archivo = open(txt)
        archivoNuevo = []

        for linea in archivo:
            #si el primer str esta comprendido entre "0" y "9" en el codigo ASCII
            if '0' <= linea[0] <= '9':
                #guardo en el nuevo array las lineas y quito los \n
                archivoNuevo.append(linea.strip())

        archivo.close()
        break

    #manejo de errores para archivos.
    except FileNotFoundError:
        print("No existe el archivo.")
        break

# funciones generales
def filtrarDistribuidores(lista):
    distribuidores = []
    for linea in lista:
        if linea[62:] not in distribuidores:
            distribuidores.append(linea[62:])
    return distribuidores

def filtrarMarcas(lista):
    marcas = []
    for linea in lista:
        if linea[24:35] not in marcas:
            marcas.append(linea[24:35])
    return marcas

# funciones para el menu
def gananciaProducto(lista):
    print("Consulta sobre ganancias y márgenes de ganancia de los productos vendidos...")
    for linea in lista:
        ganancia = float(linea[36:47]) - float(linea[47:56])
        porcentaje = ganancia / float(linea[47:56]) * 100
        print(f"producto: {linea[11:22]}, marca: {linea[24:35]}, ganancia: {ganancia:.2f}, margen de ganancia: {porcentaje:.2f}%")

def filtrarProductosPorDistribuidor(distribuidor, lista):
    print(f"Mostrando productos del {distribuidor.title()}...")
    for linea in lista:
        if linea[62:76] == distribuidor.title():
            print(f"Producto: {linea[11:22]} Marca: {linea[24:35]} Precio: {linea[36:47]}")

def productoMayorPrecioMarca(lista):
    marcas = filtrarMarcas(lista)
    for marca in marcas:
        print(f"Marca: {marca}")
        for linea in lista:
            if linea[24:35] == marca:
                print(f"                Producto: {linea[11:22]}")
    


def promedioVentasPorMarca():
    pass

def productosVendidosPorAño():
    pass

def listaDePedidoPorDistribuidor():
    pass

def promedioCantidadVentasDistribuidor():
    pass

def productoOferta():
    pass

def porcentajeCompraVenta():
    pass

def diezMarcaMasVendida():
    pass

while True:
    try:
        print("""
MENU DE OPCIONES
----------------------------------------------------------------------------
1. Consultar ganancias y márgenes de ganancia de productos.
2. Filtrar productos por Distribuidor.
3. Productos con mayor precio de cada marca.
4. Calcular promedio de precios de venta y compra por marca.
5. Listar productos vendidos por anio.
6. Mostrar productos que se necesita comprar para reponer.
7. Calcular promedio de cantidad de productos vendidos por distribuidor.
8. Filtrar productos en oferta.
9. Consultar porcentaje de productos por los precios de compra y venta.
10. 10 marcas más vendidas.
0. Salir.
""")
        opcion = int(input("Ingrese una opción: "))
        
        if opcion == 0:
            print("Saliendo del programa...")
            break

        elif opcion == 1:
            gananciaProducto(archivoNuevo)

        elif opcion == 2:
            while True:
                    distribuidores = filtrarDistribuidores(archivoNuevo)
                    distribuidor = input("Ingrese el nombre de un distribuidor: ").title()
                    if distribuidor == "":
                        print("Debe ingresar un nombre de distribuidor para continuar.")

                    valor = False
                    for nombre in distribuidores:
                        if nombre == distribuidor:
                            valor = True

                    if valor:
                        if distribuidor:
                            filtrarProductosPorDistribuidor(distribuidor, archivoNuevo)
                            break      
                    else:
                        print("El nombre ingresado no esta registrado como distribuidor.")   
                        
        elif opcion == 3:
            productoMayorPrecioMarca(archivoNuevo)
        else:
            print("Opción incorrecta, ingrese valores entre 0-1-2-3-4-5-6-7-8-9-10.")
    except:
        print("Opción invalida, ingrese un número entero.")