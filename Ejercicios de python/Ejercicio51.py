import random
"""En cada ronda del juego piedra, papel o tijera, los dos competidores deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que juegue con el usuario al que le tiene que pedir el nombre, y en cada ronda solicitar la jugada al usuario y mostrar la jugada de la computadora, luego muestre cuál es el marcador después de cada ronda, y termine cuando uno haya ganado tres rondas. El jugador debe indicar su jugada escribiendo piedra, papel o tijera. La computadora determina su jugada de formas aleatoria. Para la jugada de la computadora utilice:
    import random
    jugada_computadora = random.choice(["piedra","papel","tijera"])

    Ejemplo de ejecución:

    Ingrese su nombre: Juan
    Jugada de Juan: tijera
    Computadora: papel
    1 - 0

    Jugada de Juan: tijera
    Computadora: tijera
    1 - 0

    Jugada de Juan: piedra
    Computadora: papel
    1 - 1

    Jugada de Juan: piedra
    Computadora: tijera
    2 - 1

    Jugada de Juan: papel
    Computadora: papel
    2 - 1

    Jugada de Juan: papel 
    Computadora: piedra
    3 - 1
    Juan es el ganador"""
#random elige al azar y choice son las opciones
nombre = input("Ingrese su nombre: ")
reglas = True
puntaje = [0,0]

while (reglas):
    if puntaje[0] == 3:
        reglas = False
        print(f"{nombre} es el ganador")
    elif puntaje[1] == 3:
        reglas = False
        print(f"Computadora es la ganadora.")
    else:
        jugada_computadora = random.choice(["piedra","papel","tijera"])
        jugada = input(f"Jugada de {nombre}: ")
        if jugada == "papel":
            
            if jugada_computadora == "tijera":
                print(f"Computadora: {jugada_computadora}")
                puntaje[1] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            elif jugada_computadora == "piedra":
                print(f"Computadora: {jugada_computadora}")
                puntaje[0] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            else:
                print(f"Computadora: {jugada_computadora}")
                print("Empate, de nuevo!")

        elif jugada == "piedra":
            
            if jugada_computadora == "papel":
                print(f"Computadora: {jugada_computadora}")
                puntaje[1] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            elif jugada_computadora == "tijera":
                print(f"Computadora: {jugada_computadora}")
                puntaje[0] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            else:
                print(f"Computadora: {jugada_computadora}")
                print("Empate, de nuevo!")

        elif jugada == "tijera":

            if jugada_computadora == "papel":
                print(f"Computadora: {jugada_computadora}")
                puntaje[0] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            elif jugada_computadora == "piedra":
                print(f"Computadora: {jugada_computadora}")
                puntaje[1] += 1
                print(f"{puntaje[0]} - {puntaje[1]}")
            else:
                print(f"Computadora: {jugada_computadora}")
                print("Empate, de nuevo!")
        else: 
            print("Valor ingresado invalido, ingrese una de las siguientes opciones: tijera, piedra o papel")
    print("")

""" puntaje[0] = puntaje[0] + 2
print(puntaje) """