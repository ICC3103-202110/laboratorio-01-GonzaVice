## Código: Memorice para 2 Jugadores
## Autor: Gonzalo Ignacio Vicente Tenorio
## Fecha: 23-03-2021
## Versión: 1.2


## Exportación de Módulos

# Importar librería random
import random as rd


## Definición de Funciones

# Función: Generar lista
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

        # Si la lista está vacía
        if(originalLenght == 0):

                # Se agrega el primer número
                lst.append(randomNum)

        # Si la lista no está vacía
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


## Código Principal

# Presentación
print("\n\n   \'¡MEMORICE!\'   \n\n")

# Cantidad de pares de tarjetas
numPares = int(input("Escoje la cantidad de pares de cartas: "))

# Lista de Cartas
cards = []

# Genera la lista
cards = genList(cards, numPares)

# Test de salida de la lista de cartas
print("\n" + str(cards) + "\n")

for iteracion in cards:
    print("*", end = " ")