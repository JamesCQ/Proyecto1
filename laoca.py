import random
import os

def menu_laoca():
    salir=False
    while salir==False:
        os.system("cls")
        print("===========================================")
        print("=           BIENVENIDO A LA OCA!          =")
        print("===========================================")
        print(" 1) Empezar partida")
        print(" 2) Instrucciones")
        print(" 3) Volver al menú de juegos")
        print(" 4) Creditos")
        print("===========================================")
        opcion=int(input("Escoge una opción: "))
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


