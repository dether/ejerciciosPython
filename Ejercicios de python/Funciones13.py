"""Ejercicio 13
Realizar la función NumLetras,  que recibe un número entero y devuelve el número en letras.
Ejemplo: 
print(NumLetras(15723))
# quince mil setecientos veintitres"""
""" print(91 % 10) """
def numLetras(numero):
    primerosNumeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "séis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciséis","diecisiete","dieciocho","diecinueve"]
    decenas = ["veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
    centenas = ["cien", "doscientos", "trescientos", "cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
    if numero < 20:
        return primerosNumeros[numero]
    
    elif numero < 100:
        if numero % 10 == 0:
            calculoDecena = numero // 10
            return decenas[calculoDecena - 2]
        else:
            calculoDecena = numero // 10
            calculoPrimeros = numero % 10
            if calculoDecena == 2:
                return f"venti{primerosNumeros[calculoPrimeros]} "
            return f"{decenas[calculoDecena - 2]} y {primerosNumeros[calculoPrimeros]}"
        
    elif numero < 1000:
        if numero % 100 == 0:
            calculoCentena = numero // 100
            return centenas[calculoCentena - 1]
        else:
            calculoCentena = numero // 100 #9
            resto = (numero - (calculoCentena * 100)) # 85
            if resto < 20:
                    calculoPrimeros = resto
                    return f"{centenas[calculoCentena - 1]} {primerosNumeros[calculoPrimeros]}"
            elif resto % 10 == 0:
                calculoDecena = resto // 10 #2
                return f"{centenas[calculoCentena - 1]} {decenas[calculoDecena - 2]}"
            else:
                calculoDecena = resto // 10 #8
                
                calculoPrimeros = resto - (calculoDecena * 10) # 85 - 80
                return f"{centenas[calculoCentena - 1]} {decenas[calculoDecena - 2]} y {primerosNumeros[calculoPrimeros]}"
    elif numero < 1000000:
        if numero % 1000 == 0:
            calculoMil = numero // 1000
            if calculoMil == 1:
                return "mil"
            else:
                return f"{numLetras(calculoMil)} mil"
        #900000
        else:
            # Caso en el que no es múltiplo de mil exacto
            calculoMil = numero // 1000
            resto = numero % 1000
            if calculoMil == 1:
                return f"mil {numLetras(resto)}"
            else:
                return f"{numLetras(calculoMil)} mil {numLetras(resto)}"
    else:
        return "Fuera de rango."
            
asd = numLetras(31)
print(asd)