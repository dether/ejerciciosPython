#Leer todo el contenido de una vez con .read()
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#2. Leer línea por línea con un bucle for
with open("mi_archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # `.strip()` elimina el salto de línea al final de cada línea
#Esto es útil para procesar cada línea de forma individual, ideal para archivos grandes donde no quieres cargar todo el contenido en memoria de una sola vez.

#3. Leer todas las líneas como una lista de líneas con .readlines()
with open("mi_archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)
#Este método carga todas las líneas y las almacena en una lista, donde cada línea es un elemento de la lista. Es útil si necesitas acceder a líneas específicas por su índice.

#4. Leer una cantidad específica de caracteres con .read(n)
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read(10)  # Lee los primeros 10 caracteres
    print(contenido)
#Si quieres leer solo un número específico de caracteres, puedes pasar un número n a .read(). Esto es útil cuando solo necesitas leer una parte del archivo.

"""
                    Resumen
Método	                                    Descripción
.read()	                    Lee todo el archivo como una sola cadena de texto.
for linea in archivo	    Itera sobre el archivo línea por línea.
.readlines()	            Lee todo el archivo y devuelve una lista de líneas.
.read(n)	                Lee los primeros n caracteres del archivo."""