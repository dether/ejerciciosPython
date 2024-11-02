"""Hacer un programa que leyendo los datos del archivo .txt proporcionado, nos permita realizar lo siguiente:

1. Listado de registros en una fecha ingresada por el usuario. Mostrando también los promedios de temperaturas mínimas y máximas de ese día.

2. Registro en el que se da la mayor amplitud térmica.

3. Registros de una base determinada. Mostrando también la fecha en que hizo más calor. Para seleccionar una base, permitir ingresar parte del nombre y mostrar las que contengan ese texto."""

while True:
    try:
        #archivo para leer
        txt = "registro_temperatura365d_smn.txt"

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

#Funciones
def calcularPromedioTemperaturas(fecha: str, lista: list[str]):
    cantidadTempMax = 0
    cantidadTempMin = 0
    sumaTempMax = 0
    sumaTempMin = 0
    # recorremos las lineas guardadas por indice en lista
    for linea in lista:
        if fecha == linea[:8]:
            #si no faltan los valores en la temperatura maxima
            if "      " != linea[8:14]:
                cantidadTempMax += 1
                sumaTempMax = sumaTempMax + float(linea[8:14])
            #si no faltan los valores en la temperatura minima
            if "       " != linea[14:21]:
                cantidadTempMin += 1
                sumaTempMin = sumaTempMin + float(linea[14:21])

    print(f"En la fecha {fecha}:")

    if cantidadTempMax == 0 and cantidadTempMin == 0:
        print(f"No se encontraron registros para la fecha ingresada: {fecha}")

    else:
        if cantidadTempMax != 0:
            print(f" - El promedio de la temperatura maxima es: {(sumaTempMax/cantidadTempMax):.2f}")

        if cantidadTempMin != 0:
            print(f" - El promedio de la temperatura minima es: {(sumaTempMin/cantidadTempMin):.2f}")


def mayorAmplitudTermica(archivo: list[str]):
    mayorAmplitud = 0
    registro = ""

    for linea in archivo:
        #si las temperaturas máximas y mínimas no están vacias con espacios
        if linea[8:14] != "      " and linea[14:21] != "       ":
            amplitud = float(linea[8:14]) - float(linea[14:21])
            if amplitud > mayorAmplitud:
                mayorAmplitud = amplitud
                #guardamos la linea entera, para imprimir datos
                registro = linea 
    # Si mayorAmplitud == 0 entonces es falso!
    if mayorAmplitud: 
        print(f"La mayor amplitud registrada se da en la fecha: {registro[:8]}")
        print(f"En donde la temperatura máxima fue de:{registro[8:14]} y la temperatura mínima fue de:{registro[14:21]}")
        print(f"Por lo cual, la mayor amplitud térmica registrada fue de: {mayorAmplitud:.2f}")
    else:
        print("No se encontraron registros válidos para calcular la amplitud térmica.")

def fechaTemperaturaAlta (nombre: str, archivo: list[str]):
    registros = []
    tempMax = -9999
    registro = ""
    for linea in archivo:
        # si el nombre esta anexado en la linea True
        if nombre.upper() in linea:
            #agregamos a una lista las coincidencias para mostrar
            registros.append(linea)
            # si hay temperatura maxima
            if linea[8:14] != "      ":
                #se compara y de ser necesario se pisa el valor.
                if float(linea[8:14]) > tempMax:
                    tempMax = float(linea[8:14])
                    #Guardamos la linea en donde encontramos la temperatura maxima para mostrar datos de la misma.
                    registro = linea
    
    if registros:
        print(f"Los registros que coinciden con ´{nombre}´ son:")
        print(" FECHA  |T.MAX|T.MIN|     BASES")
        print("--------------------------------------")
        for elemento in registros:
            print(elemento)
        if tempMax != -9999:
            print(f"La temperatura máxima registrada en las bases dadas es: {tempMax} en la fecha: {registro[:8]}.")
        else:
            print("No se encontraron temperaturas máximas válidas en los registros.")
    else:
        print(f"No se encontraron registros que coincidan con '{nombre}'.")

#Menu de opciones para el usuario
while True:
    try:
        print(""" 
MENU DE OPCIONES
--------------------
1 - Promedio de temperaturas minimas y maximas.
2 - Registro de la mayor amplitud termica.
3 - Fecha en la que hizo mas calor.
0 - Salir. 
""")
        opc = int(input("Ingresa una opción: "))
        
        if opc == 0:
            print("Cerrando programa, hasta luego...")
            break
    
        elif opc == 1:
            while True:
                try:
                    fecha = input("Ingrese una fecha en formato ddmmaaaa: ")
                    if fecha == "":
                        print("Debe ingresar una fecha, para continuar.")
                    else:
                        if len(fecha) != 8:
                            print("La fecha debe tener 8 numeros, ingresando día, mes, anio.")
                        else:
                            #verificamos si se puede transformar en entero.
                            if int(fecha):
                                calcularPromedioTemperaturas(fecha, archivoNuevo)
                                break
                except ValueError:
                        print("Fecha invalida. Asegúrese de ingresar una fecha válida.")

        elif opc == 2:
            mayorAmplitudTermica(archivoNuevo)
        elif opc == 3:
            while True:
                nombre = input("Ingrese un nombre para buscar en los regristros: ")
                if nombre != "":
                    fechaTemperaturaAlta(nombre, archivoNuevo)
                    break
                else:
                    print("Ingrese un nombre para continuar.")
        else:
            print("Opción incorrecta, ingrese uno de los siguientes valores 1 - 2 - 3 - 0.")

    except ValueError:
        print("Opción invalida. Ingrese un número.")