from parchis import menu_parchis
from juego_palillos import partida
import time

def menu():
    salir=False
    while salir==False:
        print("=========================")
        print("=    MENÚ MINIJUEGOS    =")
        print("=========================")
        print(" 1) La oca")
        print(" 2) Juego de los palillos")
        print(" 3) Parchís")
        print(" 4) Salir")
        print(" 5) Creditos")
        opcion=int(input("¿Qué juego deseas jugar? "))
        if (opcion==1):
            print("1")
        elif (opcion==2):
            partida()
        elif (opcion==3):
            menu_parchis()
        elif (opcion==4):
            salir=True
        elif (opcion==5):
            print("*************************************")
            print("*            James Cañarte          *")
            print("*          Tamara Fernandez         *")
            print("*            Alex Baskota           *")
            print("*************************************")
            time.sleep(3)
        else:
            print("")

menu()