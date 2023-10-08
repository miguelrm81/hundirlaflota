import numpy as np
import random
from functionsmias import *
from variables import *

print("Bienvenidos a mi demo del Hundir la flota!!!")

jugador_1 = input("Introduce tu nombre: " )

print(f"Gracias por jugar {jugador_1}, empieza tu turno")

tablero_1 = crear_tablero()
tablero_2 = crear_tablero()
tablero_3 = crear_tablero()
tablero_4 = crear_tablero()

print(tablero_1)
print(f"Este sera tu tablero {jugador_1}")
print(tablero_2)
print("Este sera el tablero de tu contrincante")

barco_11 = crear_barco_random(2)
barco_21 = crear_barco_random(2)
tablero_1 = colocar_barco(barco_11, tablero_1)
tablero_1 = colocar_barco(barco_21, tablero_1)

barco_12 = crear_barco_random(2)
barco_22 = crear_barco_random(2)
tablero_2 = colocar_barco(barco_12, tablero_2)
tablero_2 = colocar_barco(barco_22, tablero_2)

print(" EMPIEZA EL JUEGO!!! ")



turno_jugador(jugador_1, tablero_1)

turno_cpu (jugador_2, tablero_1)

turno_jugador(jugador_1, tablero_2)

turno_cpu (jugador_2, tablero_1)

turno_jugador(jugador_1, tablero_2)

turno_cpu (jugador_2, tablero_1)






