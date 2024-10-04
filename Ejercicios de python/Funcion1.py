""" Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en 
pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.  Sin utilizar los métodos de string."""

def EscribirCentrado (texto):
    try:
        espacios = " " * int(40 - (len(texto)/2))
    except:
        return "El argumento ingresado no es un texto"
    return (f"{espacios + texto}\n{espacios + "=" * len(texto)}")

x = EscribirCentrado("Centrado")
print(x)