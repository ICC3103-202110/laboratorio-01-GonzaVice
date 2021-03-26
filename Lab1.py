### Código: Memorice para 2 Jugadores
### Autor: Gonzalo Ignacio Vicente Tenorio
### Fecha: 26-03-2021
### Versión: 1.5



### Exportación de Módulos

## Importar librería random
import random as rd



### Definición de Funciones


## Función: Generar lista
# Entrada: lista, entero
# Salida: lista
def genList(lst, numCards):

    # Mientras que el largo de la lista sea menor que la cantidad de pares de cartas solicitadas
    while(len(lst) < numCards * 2):

        # Se crea una variable llamada doble, que detectará si hay dos numeros iguales en la lista
        doble = 0

        # Escoje un numero al azar entre uno hasta el numero seleccionado
        randomNum = rd.randint(1, numCards)

        # Se crea una variable para iterar en la lista de las cartas
        iteracion = 0

        # Se crea la longitud original de la lista, ya que más adelante, al agregar un elemento a la lista,
        # la longitud cambia, por lo que al iterar la lista queremos conservar la longitud inicial
        originalLenght = len(lst)

        # Si la lista está vacía (si la longitud es 0)
        if(originalLenght == 0):

                # Se agrega el primer número
                lst.append(randomNum)

        # Si la lista no está vacía (si la longitud no es 0)
        else:
            # Mientras que la posición de iteracion sea menor que la longitud inicial de la lista
            while(iteracion < originalLenght):

                # Si hay una similitud entre el numero random y el numero en la posición iterada de la lista
                if(lst[iteracion] == randomNum):

                    # Aumentamos la cantidad de dobles o copias
                    doble += 1
                
                # Se itera al siguiente elemento de la lista
                iteracion += 1

            # Si no hay un doble o si hay solo un doble
            if(doble == 0 or doble == 1):

                # Se agrega el número a la lista
                lst.append(randomNum)

        # El proceso se repetirá hasta que la longitud de la lista sea igual a la solicitada
    
    #Retorna la lista generada
    return lst


## Función: División de numero para que sea el puntaje máximo
# Entrada: entero
# Salida: entero
def puntajeMax(num):

    # Si el numero es entero
    if(num % 2 == 0):

        # Retorna la división del numero
        return num // 2

    # Si el numero no es entero
    else:

        # Retorna la división del numero más uno
        return (num // 2) + 1



### Código Principal


## Creación de variables y elementos:

# Lista de cartas
cards = []

# Turnos (P1 = 1, P2 = 2)
turno = 1

# Puntaje
p1Points = 0
p2Points = 0

# Si quiere seguir jugando, presiona Y, si no, presiona N
seguirJuego = 'y'


## Comienzo del juego

# Presentación
print("\n\n   \'MEMORICE\'   \n")

# Opción de jugar o no jugar
seguirJuego = input("PRESIONA \'Y\' PARA JUGAR (PRESIONA CUALQUIER OTRA TECLA PARA SALIR): ")

# Si se decide jugar
if(seguirJuego == 'y' or seguirJuego == 'Y'):

    # Pide cantidad de pares de tarjetas
    numPares = int(input("\nESCOJE LA CANTIDAD DE PARES DE CARTAS PARA JUGAR: "))

    # Si cantidad de pares de tarjetas es menor que dos pares
    while(numPares < 2):

        # Es un numero erroneo
        print("\nNUMERO ERRONEO, ESCOJE UN NÚMERO MAYOR QUE 2")

        # Vuelve a pedir hasta que introduzca un numero valido para jugar
        numPares = int(input("\nESCOJE LA CANTIDAD DE PARES DE CARTAS PARA JUGAR: "))

    # Genera la lista
    cards = genList(cards, numPares)

    # Se crea el puntaje máximo para ganar el juego
    puntoMax = puntajeMax(numPares)

    # Indica cuantos puntos necesita cada uno para ganar
    print("\nSE NECESITAN CONSEGUIR " + str(puntoMax) + " PUNTOS ANTES QUE EL OTRO JUGADOR PARA GANAR\n¡BUENA SUERTE!")


# Test de salida de la lista de cartas
# print("\n" + str(cards) + "\n") #SHADOWEYE

# Comienza el juego si se decidió
while(seguirJuego == 'y' or seguirJuego == 'Y'):

    # Mientras que ambos puntajes sean menor que el puntaje máximo
    while(p1Points < puntoMax and p2Points < puntoMax):

        # Se decide quien comienza
        if(turno == 1):
            print("\n  LISTO JUGADOR 1 \n")
        else:
            print("\n  LISTO JUGADOR 2 \n")

        # Imprime cartas de la lista ocultas
        print("     CARTAS: \n")

        # Por cada carta en la lista
        for card in cards:

            # Se imprime la carta censurada
            print("*", end = " ")
        
        # Espacio
        print("\n")

        # Se escoje la primera elección
        card1Escogido = int(input(" ESCOJE LA PRIMERA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))

        # Evita el error de no escojer bien
        while((not card1Escogido >= 1) or (not card1Escogido <= len(cards))):
            print("\nNUMERO ERRONEO\n")
            card1Escogido = int(input(" ESCOJE LA PRIMERA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))

        # Se guarda el valor de la primera carta
        num1 = cards[card1Escogido - 1]

        # Imprime cartas de la lista ocultas excepto la primera escogida
        print("     CARTAS: \n")

        # Hacemos una iteración a la lista
        iteracion = 0

        # Mientras que la iteración esta en una posicion dentro de la lista
        while(iteracion < len(cards)):

            # Si la posicion es de la primera carta que se escogió
            if(iteracion == card1Escogido - 1):

                # Se imprime su valor junto con las otras cartas
                print(cards[iteracion], end = " ")

            # Si no es la posicion de la carta
            else:

                # Se imprime la carta censurada
                print("*", end = " ")

            # La iteración se suma uno para seguir recorriendo la lista hasta el último
            iteracion += 1

        # Espacio
        print("\n\n")

        # Se escoje la segunta elección
        card2Escogido = int(input(" ESCOJE LA SEGUNDA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))

        # Evita el error de no escojer bieny
        while((not card2Escogido >= 1) or (not card2Escogido <= len(cards))):
                print("\nNUMERO ERRONEO\n")
                card2Escogido = int(input(" ESCOJE LA SEGUNDA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))

        # Se guarda el valor de la segunda carta
        num2 = cards[card2Escogido - 1]

        # Imprime cartas de la lista ocultas excepto la primera y segunda escogida
        print("     CARTAS: \n")

        # Devolvemos el valor de la iteración a cero para volver a pasar por la lista
        iteracion = 0

        # Mientras que la iteración esta en una posicion dentro de la lista
        while(iteracion < len(cards)):

            # Si la posicion es de la primera o segunda carta que se escogió
            if(iteracion == card1Escogido - 1 or iteracion == card2Escogido - 1):

                # Se imprime el valor junto con las otras cartas
                print(cards[iteracion], end = " ")

            # Si no es la posicion de la carta
            else:

                # Se imprime la carta censurada
                print("*", end = " ")

            # La iteración se suma uno para seguir recorriendo la lista hasta el último
            iteracion += 1

        # Espacio
        print("\n")

        # Imprime el valor de la primera carta
        print("CARTA 1 = " + str(num1) + "\n")

        # Imprime el valor de la segunda carta
        print("CARTA 2 = " + str(num2) + "\n")

        # Si el valor de las cartas elegidas coinciden
        if(num1 == num2):
            
            # Felicitaciones al usuario
            print("¡FELICIDADES! AMBAS CARTAS SON IGUALES\n")

            # Remueve ambas cartas
            cards.remove(num1)
            cards.remove(num2)

            # Si el turno fue del jugador 1
            if(turno == 1):

                # Se le suma un punto
                p1Points += 1

            # Si el turno fue del jugador 2
            else:
                
                # Se le suma un punto
                p2Points += 1

        # Si el valor de las cartas elegidas no coinciden
        else:

            # Explicación al usuario de que no tienen el mismo valor
            # y que es turno del otro jugador
            print("AMBAS CARTAS NO SON IGUALES\n")

            # Si el turno fue del jugador 1
            if(turno == 1):

                # Es turno del jugador 2
                turno = 2

            # Si el turno fue del jugador 2
            else:

                # Es turno del jugador 1
                turno = 1
            
        # Imprimir la puntuación de ambos jugadores
        print("JUGADOR 1 = " + str(p1Points) + " PTS\n")
        print("JUGADOR 2 = " + str(p2Points) + " PTS\n")
        
        # Si el jugador 1 consigue el puntaje máximo antes que el jugador 2
        if(p1Points >= puntoMax):

            # El jugador 1 gana
            print("¡GANA JUGADOR 1!\n")

            # El juego termina
            seguirJuego = 'n'

        # Si el jugador 2 consigue el puntaje máximo antes que el jugador 1
        elif(p2Points >= puntoMax):

            # El jugador 2 gana
            print("¡GANA JUGADOR 2!\n")

            # El juego termina
            seguirJuego = 'n'
        
        # Si ninguno de los dos jugadores consiguió el puntaje máximo
        else:

            # El juego continua

            # Si el jugador coincidió las cartas
            if(num1 == num2):

                # Vuelve a jugar
                print("VUELVE A JUGAR\n")

            # Si el jugador coincidió las cartas
            else:

                # Juega el otro jugador
                print("TURNO DEL OTRO JUGADOR\n")



print("\n¡¡¡GRACIAS POR JUGAR!!!\n")
    
