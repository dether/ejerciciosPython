""" Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
Vamos a crear las siguientes funciones para trabajar con funciones:
• Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. 
Cuando leas una fracción debes simplificarla. 
• Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se 
muestra sólo el numerador. 
• Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor. 
• Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir 
numerador y dominador por el MCD del numerador y denominador. 
• Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de 
las dos fracciones. La suma de dos fracciones es otra fracción cuyo 
numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción 
resultado. 
• Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y 
denominador=d1*d2. Se debe simplificar la fracción resultado. 
• Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para 
ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción 
resultado. 
• Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello 
numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado. 
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
1. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado. 
2. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta. 
3. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto. 
4. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente. 
5. Salir"""

def leerFraccion ():
    while True:
        try:
            numerador = int(input("Ingrese un número entero, para el numerador: "))
            denominador = int(input("Ingrese un número entero, para el denominador: "))
            if denominador == 0:
                print("El denominador no puede ser cero. Inténtalo de nuevo.")
                continue
            if type(numerador) == int and type(denominador) == int:
                break
        except:
            print("Valor incorrecto💥, ingrese un número entero, por favor.")
            continue
    return numerador, denominador
""" print(leerFraccion()) """

def escribirFraccion(a:int, b:int):
    if b == 1:
        print(f"{a}")
        return
    if a == 0:
        print(0)
        return
    if b < 0 and a > 0:
        a = -a
        b = b * (-1)
    elif b < 0 and a <0:
        a = a
        b = b
    
    print(f"{a}/{b}")
""" asd =Escribir_fracción(10)
print(asd) """

def calcularMCD(a:int, b:int):
    mcd = 1
    numerador = []
    denominador = []
    mcds = []
    if a == 0:
        return 0
    if a % b == 0:
        mcd = b
        return mcd
    else:
        for i in range(1, a+1):
            if a % i == 0:
                numerador.append(i)
        for j in range(1, b+1):
            if b % j == 0:
                denominador.append(j)
        for i in numerador:
            for j in denominador:
                if i == j:
                    mcds.append(j)
        if len(mcds) == 0:
            return 1
        for num in mcds:
            if num > mcd:
                mcd = num
    return mcd
""" asz = Calcular_mcd(9417,0)
print(asz) """

def simplificarFraccion(a: int, b: int):
    mcd = calcularMCD(a,b)
    a = a // mcd
    b = b // mcd
    return a, b

def sumarFracciones(a1: int, b1: int, a2: int, b2: int):
    if b1 == b2:
        if (a1 + a2) == b2:
            return 1, 1
        a = a1 + a2
        b = b2
        if a == 0:
            return 0, 0
        mcd = calcularMCD(a, b)
        a = a // mcd
        b = b // mcd
        return a, b
    else:
        a = a1*(b2) + a2*(b1)
        b = b1 * b2
        mcd = calcularMCD(a, b)
        a = a // mcd
        b = b // mcd
        return a, b
""" asq = Sumar_fracciones()
print(asq) """

def restarFracciones(a1: int, b1: int, a2: int, b2: int):
    if b1 == b2:
        if (a1 - a2) == b2:
            return 1, 1
        a = a1 - a2
        b = b2
        if a == 0:
            return 0, 0
        mcd = calcularMCD(a, b)
        a = a // mcd
        b = b // mcd
        return a, b
    else:
        a = a1*(b2) - a2*(b1)
        b = b1 * b2
        mcd = calcularMCD(a, b)
        a = a // mcd
        b = b // mcd
        if a == 0:
            return 0
        return a, b
""" resta = restarFracciones()
print(resta) """

def multiplicarFracciones(a1: int, b1: int, a2: int, b2: int):
    if a2 == 0 or a1 == 0:
        return 0, 1
    a = a1 * a2
    b = b1 * b2
    mcd = calcularMCD(a, b)
    a = a // mcd
    b = b // mcd
    return a, b

def dividirFracciones(a1: int, b1: int, a2: int, b2: int):
    if a2 == 0 or a1 == 0:
        return 0, 1
    a = a1 * b2
    b = b1 * a2
    mcd = calcularMCD(a, b)
    a = a // mcd
    b = b // mcd
    return a, b
asd = "✅❌💥🤓👨🏽‍🏫👋🏽 "
opcion = 0
print("🚩 Bienvenido usuario 🚩")
while True:
    try:
        print("\n🤓 Ingrese una de las siguientes opciones para continuar.")
        print("Opción 1: Sumar dos fracciones")
        print("Opción 2: Restar dos fracciones")
        print("Opción 3: Multiplicar dos fracciones")
        print("Opción 4: Dividir dos fracciones")
        print("Opción 5: Salir")
        
        opcion = int(input("🤓 Ingrese una opción: "))
        
    except:
        print("💥 Opción invalida, intentelo de nuevo.")
        
    if opcion == 1:
        resultado = leerFraccion()
        if resultado:
            a1 = resultado[0]
            b1 = resultado[1]
            
        resultado2 = leerFraccion()
        if resultado2:
            a2 = resultado2[0]
            b2 = resultado2[1]
            
        a,b = sumarFracciones(a1, b1, a2, b2)
        print(f"✅ El resultado de la sumatoria {a1}/{b1} ➕ {a2}/{b2} 🟰", end=("  ") )
        escribirFraccion(a,b)
        continue
        
    elif opcion == 2:
        resultado = leerFraccion()
        if resultado:
            a1 = resultado[0]
            b1 = resultado[1]
            
        resultado2 = leerFraccion()
        if resultado2:
            a2 = resultado2[0]
            b2 = resultado2[1]
            
        a,b = restarFracciones(a1, b1, a2, b2)
        print(f"✅ El resultado de la diferencia {a1}/{b1} ➖ {a2}/{b2} 🟰", end=(" "))
        escribirFraccion(a,b)
        continue

    elif opcion == 3:
        resultado = leerFraccion()
        if resultado:
            a1 = resultado[0]
            b1 = resultado[1]
            
        resultado2 = leerFraccion()
        if resultado2:
            a2 = resultado2[0]
            b2 = resultado2[1]
            
        a,b = multiplicarFracciones(a1, b1, a2, b2)
        print(f"✅ El resultado del producto {a1}/{b1} ✖ {a2}/{b2} 🟰", end=(" "))
        escribirFraccion(a,b)
    
    elif opcion == 4:
        resultado = leerFraccion()
        if resultado:
            a1 = resultado[0]
            b1 = resultado[1]
            
        resultado2 = leerFraccion()
        if resultado2:
            a2 = resultado2[0]
            b2 = resultado2[1]
            
        a,b = dividirFracciones(a1, b1, a2, b2)
        print(f"✅ El resultado de {a1}/{b1} ➗ {a2}/{b2} 🟰", end=(" "))
        escribirFraccion(a,b)
    
    elif opcion == 5:
        print("😎 Que tengas un buen día, gracias por confiar en nosotros.")
        break