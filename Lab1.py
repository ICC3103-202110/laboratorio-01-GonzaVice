## Código: Memorice para 2 Jugadores
## Autor: Gonzalo Ignacio Vicente Tenorio
## Fecha: 23-03-2021
## Versión: 1.1


## Exportación de Módulos

# Importar librería random
import random as rd


## Definición de Funciones

# Función: Generar lista
# Entrada: lista
# Salida: lista
def genList(lst):

    # Mientras que el largo de la lista sea menos que la cantidad de cartas solicitadas
    while(len(lst) < numPares*2):

        # Escoje un numero al azar entre 1 hasta el numero seleccionado
        randomNum = rd.randint(1, numPares*2)

        # Si está en la lista
        while(randomNum in lst):

            # Cambia de numero hasta que sea un numero diferente
            randomNum = rd.randint(1, numPares*2)

        # Si es un número diferente, entra a la lista
        lst.append(randomNum)
    
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
cards = genList(cards)

# Test de salida de la lista de cartas
print("\n" + str(cards) + "\n")