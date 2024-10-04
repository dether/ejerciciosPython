""" Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función. Sin utilizar los métodos de string."""

def convertirEspaciado (texto):
    if not type(texto) == str:
        return("El argumento ingresado debe ser un texto.")
    nuevaCadena = ""
    for i in texto:
        if i != " ":
            nuevaCadena += i + " "

    return (nuevaCadena)

cadena ="1dsadsa dsd"
x =convertirEspaciado(cadena)
print(x)