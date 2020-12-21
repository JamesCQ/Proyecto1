import random
import os
import time

def presentacion():
    print("===========================================")
    print("=           BIENVENIDO A LA OCA!          =")
    print("===========================================")
    print(" 1) Empezar partida")
    print(" 2) Instrucciones")
    print(" 3) Volver al menú de juegos")
    print(" 4) Creditos")
    print("===========================================")


def instrucciones():
    os.system("cls")
    print("===================================")
    print(" Habrá sólo un dado.               ")
    print(" Las casillas están representadas  ")
    print(" en números, así que cada casilla  ")
    print(" tiene un efecto diferente.        ")
    print("===================================")
    input("Pulsa Enter para volver al menú...")

def partida():
    jugando=True
    nombre1 = input("Nombre de jugador1: ")
    nombre2 = input("Nombre de jugador2: ")
    jugador1 = 0
    jugador2 = 0
    turno = 1
    print("***********************************")
    print("   Ten en cuenta que las casillas  ")
    print("   múltiplos de 5 tiras de nuevo   ")
    print(" ¡Y gana el que llegue a 63 puntos!")
    print("***********************************")
    input("Pulsa Enter para jugar!")

    while jugando:
        os.system("cls")
        if turno==1:
            dado = random.randint(1,6)
            print("Tu turno", nombre1,"!")
            print("Pulsa Enter para tirar dado...")
            os.system("cls")
            print("Tirando dado...")
            time.sleep(1)
            print("Ha tocado el número", dado)
            jugador1+=dado
            print("Ahora estás en la casilla", jugador1, nombre1,"!")
            if jugador1%5==0:
                turno = 1
                print("Te vuelve a tocar", nombre1, "!")
            else:
                turno = 2
            if jugador2==63:
                print("Ganas la partida!")
                time.sleep(2)
                jugando=False
            elif jugador2>63:
                jugador2-=dado
                print("Te has pasado, así que se resta el dado a tu número de posicion actual")
                print("Tu casilla actual es:", jugador2)
            input("Pulsa Enter para el siguiente turno!")

        elif turno==2:
            dado = random.randint(1,6)
            print("Tu turno", nombre2,"!")
            print("Pulsa Enter para tirar dado...")
            os.system("cls")
            print("Tirando dado...")
            time.sleep(1)
            print("Ha tocado el número", dado)
            jugador2+=dado
            print("Ahora estás en la casilla", jugador2, nombre2,"!")
            if jugador2%5==0:
                turno = 2
                print("Te vuelve a tocar", nombre2,"!")
            else:
                turno = 1
            if jugador2==63:
                print("Ganas la partida!")
                time.sleep(2)
                jugando=False
            elif jugador2>63:
                jugador2-=dado
                print("Te has pasado, así que se resta el dado a tu número de posicion actual")
                print("Tu casilla actual es:", jugador2)
            input("Pulsa Enter para el siguiente turno!")




def menu_laoca():
    os.system("cls")
    salir=False
    while salir==False:
        os.system("cls")
        presentacion()
        opcion=int(input("Escoge una opción: "))
        if (opcion==1):
            partida()
        elif (opcion==2):
            instrucciones()
        elif (opcion==3):
            salir=True
        elif (opcion==4):
            print("====================")
            print("= Tamara Fernandez =")
            print("====================")
        else:
            print("")
