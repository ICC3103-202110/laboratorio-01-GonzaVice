### Código: Memorice para 2 Jugadores
### Autor: Gonzalo Ignacio Vicente Tenorio
### Fecha: 26-03-2021
### Versión: 1.4


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


### Código Principal

## Creación de variables y elementos:

# Lista de cartas
cards = []

# Turnos (P1 = 1, P2 = 2)
turno = 1

# Puntaje
p1Points = 0
p2Points = 0

## Comienzo del juego

# Presentación
print("\n\n   \'MEMORICE\'   \n")

# Pide cantidad de pares de tarjetas
numPares = int(input("ESCOJE LA CANTIDAD DE PARES DE CARTAS PARA JUGAR: "))

# Genera la lista
cards = genList(cards, numPares)

# Test de salida de la lista de cartas
print("\n" + str(cards) + "\n")

# Comienza el juego
while(p1Points < 1 and p2Points < 1):

    # Se decide quien comienza
    if(turno == 1):
        print("\n\n  LISTO JUGADOR 1 \n")
    else:
        print("\n  LISTO JUGADOR 2 \n")

    # Imprime cartas de la lista ocultas
    print("     CARTAS: \n")
    for iteracion in cards:
        print("*", end = " ")
    print("\n")

    # Imprime primera elección
    card1Escogido = int(input(" ESCOJE LA PRIMERA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))
    num1 = cards[card1Escogido - 1]


    # Imprime cartas de la lista ocultas excepto la primera escogida
    print("     CARTAS: \n")
    iteracion = 0
    while(iteracion < len(cards)):
        # print("iteracion = " + str(iteracion)) #SHADOWEYE
        # print("cards[iteracion] = " + str(cards[iteracion])) #SHADOWEYE
        if(iteracion == card1Escogido - 1):
            print(cards[iteracion], end = " ")
        else:
            print("*", end = " ")
        iteracion += 1
    print("\n\n")

    # Imprime segunda elección
    card2Escogido = int(input(" ESCOJE LA SEGUNDA CARTA (ENTRE 1 Y " + str(len(cards)) + "): "))
    num2 = cards[card2Escogido - 1]

    # Imprime cartas de la lista ocultas excepto la primera y segunda escogida
    print("     CARTAS: \n")
    iteracion = 0
    while(iteracion < len(cards)):
        # print("iteracion = " + str(iteracion)) #SHADOWEYE
        # print("cards[iteracion] = " + str(cards[iteracion])) #SHADOWEYE
        if(iteracion == card1Escogido - 1 or iteracion == card2Escogido - 1):
            print(cards[iteracion], end = " ")
        else:
            print("*", end = " ")
        iteracion += 1
    print("\n\n")

    print("num1 = " + str(num1))
    print("num2 = " + str(num2))
    if(num1 == num2):
        print("num1 y num2 son iguales, tienes un punto")
        p1Points += 1
        print("p1points = " + str(p1Points))
    
    p1Points = 5


