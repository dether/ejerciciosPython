""" #05062023   Impresora    SmartLine     729.13    402.36   75   Distribuidor B  
#fecha      0-8 
#producto  11-22
#marca     24-35
#venta     36-47
#compra    47-56
#canti    58-63
#distri   62-80
asd = [
"05062023   Impresora    SmartLine     729.13    402.36   75   Distribuidor B  ",
"22072020   Laptop       TechBrand     903.87    745.62   18   Distribuidor E  ",
"27062020   Impresora    SmartLine     487.45    290.16   34   Distribuidor D  ",
"12102020   Router       ElectroCorp   441.68    273.28    6   Distribuidor A  ",
"07032022   Teclado      DataWare      129.21     99.95   97   Distribuidor E  ",
"01122022   Memoria USB  NextGen       166.99     99.86   97   Distribuidor D  ",
"05072020   Router       NextGen       756.35    408.09   46   Distribuidor C  ",
"05072020   Router2      NextGen       756.35    408.09   46   Distribuidor C  "
]

def filtrarMarcas(lista):
    marcas = []
    for linea in lista:
        if linea[24:35] not in marcas:
            marcas.append(linea[24:35])
    return marcas

def productoMayorPrecioMarca(lista):
    marcas = filtrarMarcas(lista)

    for marca in marcas:
        print(f"Marca: {marca}")
        for linea in lista:
            if linea[24:35] == marca:
                print(f"                Producto: {linea[11:22]}")
    
productoMayorPrecioMarca(asd)

"""

nombres = ["a", "b", "c"]
tiempos = [13, 12, 11, 19]
# aca le pongo cualquier nombre a los argumentos. Solo explicas que vas a hacer con esos datos que te pasen.
def estudiantes_menor_15(variable1,variable2):
    for i in range(len(variable1)):
        if variable2[i] < 15:
            print(f"La persona {variable1[i]} tiene {variable2[i]}.")
#aca le paso las listas existentes como parametros
estudiantes_menor_15(nombres, tiempos)