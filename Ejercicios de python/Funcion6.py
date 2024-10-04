"""Crear una función llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo"""

def login(usuario, contraseña, intentos):
    if (usuario == "usuario1") and (contraseña == "asdasd") and (intentos < 4):
        return True
    else:
        return False

def programa():
    intentos = 0
    while True:
        try:
            if not intentos > 3:
                usuario = input("Ingrese su usuario: ")
                contraseña = input("Ingrese su contraseña: ")
                ingreso = login(usuario, contraseña, intentos)
                if ingreso:
                    print(f"Has ingresado a tu cuenta. Bienvenido {usuario}")
                    #print(login(usuario, contraseña, intentos))
                    break
                else:
                    print(f"El usuario o contraseña ingresados no corresponde a una cuenta registrada.")
                    intentos += 1
                    #print(login(usuario, contraseña, intentos))
            else:
                print(f"Su cuenta se ha bloqueado por unos minutos, vuelva a intentarlo más tarde.")
                break
        except:
            print("El valor ingresado es invalido, ingrese un usuario y una contraseña validas.")
        #print(intentos)

programa()