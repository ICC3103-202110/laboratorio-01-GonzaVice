## Código: Memorice para 2 Jugadores
## Autor: Gonzalo Ignacio Vicente Tenorio
## Fecha: 22-03-2021
## Versión: 1.0


## Exportación de Módulos

# Importar librería random
import random as rd


## Definición de Funciones


## Código Principal

# Presentación
print("\n\n   \'¡MEMORICE!\'   \n\n")

# Cantidad de pares de tarjetas
numPares = int(input("Escoje la cantidad de pares de cartas: "))
# print("numPares = " + str(numPares)) # SHADOWEYE

# Lista de Cartas
cards = []

# Introduce numeros en la lista con la cantidad de pares de tarjetas
for num in range(numPares*2):
    # Si no está en la lista
    if(not num in cards):
        # El numero se agrega en la lista
        cards.append(num)
        # print(num) # SHADOWEYE
        # print(num in cards) # SHADOWEYE

# Test de salida de la lista de cartas
print("\n" + str(cards) + "\n")