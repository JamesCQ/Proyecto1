'''
Juego de los Palillos
'''

import random
import time
import os


def presentacion():

    '''Mostramos una pantalla de inicio y devuelve el nivel
    que elija el usuario'''
    

    print()
    print("  * * * * * * * * *  JUEGO DE LOS PALILLOS  * * * * * * * * * *  ")
    print()
    print()
    print("               Gana quien coge el último palillo   ")
    print()
    print()
    print()
    print("             1- Fácil        /      2- Difícil")
    print()
    print()
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   ")
    print()
    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("  Elige nivel (1/2): ")
    return nivel



def instrucciones(palillos, quitas):

    print()
    print("  * * * * * * * * *  JUEGO DE LOS PALILLOS   * * * * * * * * *  ")
    print()
    print()
    print("                  Habrá {} palillos en total.".format(palillos))
    print()
    print("              Se pueden quitar entre 1 y {} palillos.".format(quitas))
    print()
    print()
    print("                      Empiezas a mover tú!")
    print()
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   ")
    print()
    input(" Pulsa Enter para empezar ...")


def sorteo_opciones():

    '''Devuelve dos valores aleatorios: Número de palillos totsles
    (entre 16 y 23) y número de palillos a quitar (entre 3 y 5) '''

    palillos = random.randint(16, 23)
    quitas = random.randint(3,5)

    return palillos, quitas



def area(palillos, quitas):

    "Muestra los palillos que hay en cada jugada"
    
    print()
    print("  * * * * * * * * *  JUEGO DE LOS PALILLOS   * * * * * * * * *  ")
    print()
    print()

    for fila in range(4):
        print(end="   ")
        for p in range(1, palillos+1):
            print("|",end="  ")
            if p % quitas == 0:
                print(end="  ")
        print()
    
    print()
    print()
    print()



def movimientoJugador(palillos, quitas):

    #Devuelve el número de palillos que el usuario quita en cada jugada
    
    if quitas == 3:
        quitas = ("1","2","3")
    elif quitas == 4:
        quitas = ("1","2","3","4")
    elif quitas == 5:
        quitas = ("1","2","3","4","5")

    q = input("   Palillos a quitar: ")
    while q not in quitas or int(q) > palillos:
        if q not in quitas:
            q = input("   Elige entre 1 y {}: ".format(len(quitas)))
        elif int(q) > palillos:
            q = input("   Sólo quedan {} palillos: ".format(palillos))

    else:
        palillos_quitar = int(q)

    return palillos_quitar


def movimiento_Ordenador_aleatorio(palillos, quitas):

    "Devuelve un número aleatorio de palillos a quitar para el ordenador"

    palillos_quitar = random.randint(1,quitas)

    while palillos_quitar > palillos:
        palillos_quitar = random.randint(1,quitas)

    return palillos_quitar

def movimiento_Ordenador_ia(palillos, quitas):

    '''Devuelve el número de palillos a quitas como jugada del 
    ordenador caculados para que el ordenador gane siempre que pueda:
    Se trata de dejar siempre un palillo más de lo que se pueden quitar.'''

    palillos_quitar = None

    while palillos_quitar is None or palillos_quitar > palillos:
        if palillos <= quitas:
            palillos_quitar = palillos
        elif palillos % (quitas+1) == 5:
            palillos_quitar = 5
        elif palillos % (quitas+1) == 4:
            palillos_quitar = 4
        elif palillos % (quitas+1) == 3:
            palillos_quitar = 3
        elif palillos % (quitas+1) == 2:
            palillos_quitar = 2
        elif palillos % (quitas+1) == 1:
            palillos_quitar = 1
        elif palillos % (quitas+1) == 0:
            palillos_quitar = random.randint(1,2)

    return palillos_quitar


def mostrar_ganador(turno):

    "Muestra una pantalla final con el ganador de la partida"

    if turno == 2:
        mensaje1 = "                  Has cogido el último palillo"
        mensaje2 = "          *  *  *  *  *  HAS GANADO   *  *  *  *  *"
    elif turno == 1:
        mensaje1 = "               El ordenador coge el último palillo"
        mensaje2 = "       *  *  *  *  *  GANA EL ORDENADOR   *  *  *  *  *"


    print()
    print("  * * * * * * * * *  JUEGO DE LOS PALILLOS   * * * * * * * * *  ")
    print()
    print()
    print()
    print("{}".format(mensaje1))
    print()
    print()
    print("{}".format(mensaje2))
    print()
    print()
    print()



def partida():
    turno = 1 

    palillos, quitas = sorteo_opciones()

    os.system("clear")
    nivel = presentacion()

    os.system("clear")
    instrucciones(palillos, quitas)

    jugando = True

    while jugando:

        os.system("clear")
        area(palillos, quitas)

        if turno == 1:
            jugada = movimientoJugador(palillos, quitas)
            turno = 2
        elif turno == 2:
            print("   El ordenador está pensando ...")
            time.sleep(2)
            if nivel == "1":
                jugada = movimiento_Ordenador_aleatorio(palillos, quitas)
            elif nivel == "2":
                jugada = movimiento_Ordenador_aleatorio(palillos, quitas)
            turno = 1

        palillos -= jugada

        if palillos == 0:
            os.system("clear")
            mostrar_ganador(turno)
            print("Quieres volver al menú minijuegos o volver a comenzar nueva partida?: ")
            print(" 1) Volver al menú")
            print(" 2) Nueva partida")
            opcion = int(input(": "))
            if opcion==1:
                jugando = False
            elif opcion==2:
                partida()
            else:
                print("")
