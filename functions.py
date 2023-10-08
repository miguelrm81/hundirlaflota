import numpy as np
import random 
def intro(instrucciones) :
    """
    Funcion que nos da la vienvenida, nos indica si queremos elegir la ayuda y las instrucciones del juego, si queremos jugar la 
    demo, o probar directamente el juego

    """
    print("                  ¡¡¡HUNDIR LA FLOTA!!!")
    print("Bienvenido a hundir la flota")
    print("Selecciona una de las siguientes opciones: ")
    print("1 - Jugar contra la maquina")
    print("2 - Probar una DEMO")
    print("3 - Ver las instrucciones de juego")
    x = int(input("elija su opcion :"))
    if x == 1 :
        python.py
    elif x == 2 :
        demo.py
    else :
        print(instrucciones)

def orientacion():
    # Lista de letras disponibles
    letras = ["N", "S", "E", "O"]

    # Elegir una letra aleatoria
    letra_aleatoria = random.choice(letras)

    # Imprimir la letra aleatoria
    return letra_aleatoria

def colocar_barco(barco, tablero):
# esta es la funcion que imprime los barcos en el tablero cambiando las casillas por O
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def crear_barco_random(eslora):
    # funcion para crear el barco y decirle si va hacia el N, S, E u Oeste a partir de una casilla que obtenemos 
    while True :
        barco_random=[]
        direccion = orientacion()
        
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        barco_random.append((fila_random, columna_random))
        
        #Aqui tenemos el bucle por el cual coloca los barcos en funcion de su orientacion

        # Norte
        if direccion == "N" :
             while len(barco_random) < eslora:
                columna_random = columna_random +1
                if columna_random > 10 or columna_random < 0 :
                    break
                else :
                    barco_random.append((fila_random, columna_random))


        # Sur
        elif direccion == "S" :
            while len(barco_random) < eslora:
                columna_random = columna_random -1
                if columna_random > 10 or columna_random< 0 :
                    break
                else :
                    barco_random.append((fila_random, columna_random))
        # Este 
        elif direccion == "E" :
            while len(barco_random) < eslora:
                fila_random = fila_random +1
                if fila_random > 10 or fila_random < 0 :
                    break
                else :
                    barco_random.append((fila_random, columna_random))
        # Oeste
        elif direccion == "O" :
            while len(barco_random) < eslora:
                fila_random = fila_random -1
                if fila_random > 10 or fila_random < 0 :
                    break
                else :
                    barco_random.append((fila_random, columna_random))

        
        
        return barco_random

def disparo_usuario():
    #Funcion para obtener mediente un input las coordenadas del disparo
    while True:
        columna = int(input("seleccione la columna : "))
        if columna < 0 or columna > 10:
            print("Numero incorrecto, escribe otro")
        else :
            break

    while True :
        fila = int(input("seleccione la fila : "))
        if fila < 0 or fila > 10:
            print("numero incorrecto, escribe otro")
        else :
            break
        
    coordenadas = (columna,fila)
    print ( f"Tu disparo es {coordenadas}")
    return coordenadas


def disparo_cpu():
    # funcion para obtener la casilla del disparo de la CPU
    
    fila_cpu = random.randint(0,9)
    columna_cpu = random.randint(0,9)
    shoot_cpu = (fila_cpu, columna_cpu)
    return shoot_cpu

def crear_tablero(tamaño=(10,10)):
    #funcion que nos crea el tablero de 10x10
    return np.full(tamaño, " ")

def disparar(casilla, tablero,tablero2):
    #funcion que nos aplica el disparo obtenido y nos dice si es agua o tocado

    print("ESte es tu tablero :")
    print(tablero)
    print("-"*100)
    print("Este es el tablero de tu contrincante : ")
    print(tablero2)
        
          
    while True:
        # si el disparo es agua, pasa el turno. En caso de acertar, volveria a disparar
    
        if tablero[casilla] == " ":
            print("Agua")
            print("Has fallado, cambio de turno")
            tablero[casilla] = "-"
            
            break
        elif tablero[casilla] == "X":
            print("El dispaso se ha repetido, vuelve a disparar")


        else:
            print("Tocado")
            tablero[casilla] = "X"
            
            
            
            
    return tablero, tablero2

def comparar_tablero(lista_barcos,barco) :
    #esta funcion la cree para intentar comparar los tableros e imprimir el tercer tablero en el que no nos salen los barcos
    for tupla1 in lista_barcos:
        for tupla2 in barco:
            if tupla1 == tupla2 :
                return True
            else : 
                return False
def turno_jugador (jugador,tablero):
    #define el turno del jugador, nos indica de quien es el turno, obtiene la coordenada y dispara
    print(f"Es el turno del jugador {jugador}")
    
    x = disparo_usuario()
    disparar(x, tablero)
    print(tablero)
    

def turno_cpu (jugador, tablero):
    #define el turno de la CPU. En este caso se hace todo con el comando random
    print(f"Es el turno del jugador {jugador}")
    x = disparo_cpu()
    disparar(x, tablero)
    print(tablero)
    

def tablero_usuario(tablero1, tablero2) :
    # esta la hice para que imprimiera el tablero del usuario
    print("Este es tu tablero :")
    print(tablero1)
    print("-"*100)
    print("Aqui esta el tablero de tu adversario, con tus disparos :")
    print(tablero2)


"""
def comparador_barco (tablero, barco)
    #esta funcion la usamos para ver si un barco esta dentro del tablero y repetir la operacion de generar barco
    
    for casilla in barco:
        if tablero(casilla) == barco(casilla) :
            break
            
"""
"""
Ideas del juego que estuve probando y fui incapaz de resolver e implementar

Estuve intentando meter en la misma funcion DISPARAR, darle como argumento el segundo tablero, para que en el me dibujara
tambien los aciertos y los fallos para poder imprimir los dos tableros a la vez.

Le di como tableros de un usuario el 1 y el 3, y como tableros de la maquina el 2 y el 4
entonces cada vez que disparara el usuario, se imprimiria a la vez en ambos tableros.

intente crear la variable vidas=20, para que cada vez que un usuario acertara, se le restara una vida. Teniendo en cuenta la cantidad
de barcos en el tablero y la cantidad de sus casillas, iguale vidas a dicha cantidad. Pero cuando intente implementarlo, no me dejo
contabilizar la variable vidas. Me decia que esa variable no existia 
"""
    