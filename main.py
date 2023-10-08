import numpy as np
import random
from functions import *
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

barco_11 = crear_barco_random(1)
barco_12 = crear_barco_random(1)
barco_13 = crear_barco_random(1)
barco_14 = crear_barco_random(1)
barco_21 = crear_barco_random(2)
barco_41 = crear_barco_random(4)
barco_22 = crear_barco_random(2)
barco_23 = crear_barco_random(2)
barco_31 = crear_barco_random(3)
barco_32 = crear_barco_random(3)
barco_33 = crear_barco_random(3)
barco_11_cpu= crear_barco_random(1)
barco_12_cpu = crear_barco_random(1)
barco_13_cpu = crear_barco_random(1)
barco_14_cpu = crear_barco_random(1)
barco_21_cpu = crear_barco_random(2)
barco_41_cpu = crear_barco_random(4)
barco_22_cpu = crear_barco_random(2)
barco_23_cpu = crear_barco_random(2)
barco_31_cpu = crear_barco_random(3)
barco_32_cpu = crear_barco_random(3)


tablero_1 = colocar_barco(barco_11, tablero_1)
tablero_1 = colocar_barco(barco_12, tablero_1)
tablero_1 = colocar_barco(barco_13, tablero_1)
tablero_1 = colocar_barco(barco_14, tablero_1)
tablero_1 = colocar_barco(barco_21, tablero_1)
tablero_1 = colocar_barco(barco_22, tablero_1)
tablero_1 = colocar_barco(barco_23, tablero_1)
tablero_1 = colocar_barco(barco_31, tablero_1)
tablero_1 = colocar_barco(barco_32, tablero_1)
tablero_1 = colocar_barco(barco_41, tablero_1)
tablero_2 = colocar_barco(barco_11_cpu, tablero_2)
tablero_2 = colocar_barco(barco_12_cpu, tablero_2)
tablero_2 = colocar_barco(barco_13_cpu, tablero_2)
tablero_2 = colocar_barco(barco_14_cpu, tablero_2)
tablero_2 = colocar_barco(barco_21_cpu, tablero_2)
tablero_2 = colocar_barco(barco_22_cpu, tablero_2)
tablero_2 = colocar_barco(barco_23_cpu, tablero_2)
tablero_2 = colocar_barco(barco_32_cpu, tablero_2)
tablero_2 = colocar_barco(barco_31_cpu, tablero_2)
tablero_2 = colocar_barco(barco_41_cpu, tablero_2)



print(" EMPIEZA EL JUEGO!!! ")

while vidas != 20 :

    turno_jugador(jugador_1, tablero_1)

    turno_cpu (jugador_2, tablero_1)

    vidas = vidas -1




