## Código: Memorice para 2 Jugadores (Debug de la lista)
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

    print("numCards = " + str(numCards)) #SHADOWEYE
    print("lst = " + str(lst)) #SHADOWEYE

    # Mientras que el largo de la lista sea menor que la cantidad de 
    # pares de cartas solicitadas
    while(len(lst) < numCards * 2):

        print("len(lst) = " + str(len(lst)) + " aun es menor que numCards * 2 = " + str(numCards * 2)) #SHADOWEYE

        # Se crea una variable llamada doble, que detectará si
        # hay dos numeros iguales en la lista
        doble = 0

        # Escoje un numero al azar entre uno hasta el numero seleccionado
        randomNum = rd.randint(1, numCards)

        print("randomNum = " + str(randomNum)) #SHADOWEYE

        # Se crea una variable para iterar en la lista de las cartas
        iteracion = 0

        # Se crea la longitud original de la lista, ya que más adelante,
        # al agregar un elemento a la lista, la longitud cambia, por lo que 
        # al iterar la lista queremos conservar la longitud inicial
        originalLenght = len(lst)

        print("originalLenght = " + str(originalLenght)) #SHADOWEYE

        # Si la lista está vacía
        if(originalLenght == 0):

                # Se agrega el primer número
                lst.append(randomNum)

                print("Felicidades, el primer numero agregado " + str(randomNum) + " a la lista lst = " + str(lst)) #SHADOWEYE

        # Si la lista no está vacía
        else:
            # Mientras que la psoción de iteracion sea menor que la longitud inicial de la lista
            while(iteracion < originalLenght):

                print("iteracion = " + str(iteracion)) #SHADOWEYE

                # Si hay una similitud entre el numero random y el numero en la
                # posición iterada de la lista
                if(lst[iteracion] == randomNum):

                    # Aumentamos la cantidad de dobles o copias
                    doble += 1

                    print("doble = " + str(doble)) #SHADOWEYE
                
                # Se itera al siguiente elemento de la lista
                iteracion += 1

            # Si no hay un doble o si hay solo un doble
            if(doble == 0 or doble == 1):

                # Se agrega el número a la lista
                lst.append(randomNum)
                print("Felicidades, se agrego " + str(randomNum) + " a la lista lst = " + str(lst)) #SHADOWEYE

        # El proceso se repetirá hasta que la longitud de
        # la lista sea igual a la solicitada
        print("\n¡¡¡VUELTA!!!\n")  #SHADOWEYE
    
    #Retorna la lista generada
    return lst


## Código Principal

# Presentación
print("\n\n   \'¡MEMORICE!\'   \n\n")

# Cantidad de pares de tarjetas
numPares = int(input("Escoje la cantidad de pares de cartas: "))
# print("numPares = " + str(numPares)) # SHADOWEYE

# Lista de Cartas
cards = []

# Genera la lista
cards = genList(cards, numPares)

# Test de salida de la lista de cartas
print("\n" + str(cards) + "\n")