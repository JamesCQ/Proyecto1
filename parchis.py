import random
import os

def tirada():
    dado = random.randint(1,6)

    return dado

def puntos(listapuntos,dado):

    

def partida():
    turnoazul=True
    jugando=True
    while jugando:
        os.system("clear")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~")
        print("Tu turno equipo azul")
        print("~~~~~~~~~~~~~~~~~~~~")
        input(" Pulsa Enter para tirar de dado ...")

def instrucciones()
    print("")
    print("===========================================")
    print("=El primero que llegue a los 72 puntos sin=")
    print("=         pasarse, gana. Suerte :)        =")

def menu_parchis():
    salir=False
    while salir==False:
        print("===========================================")
        print("= BIENVENIDO AL PARCHIS DE DOS JUGADORES! =")
        print("= Habrán dos equipos, primero comienza el =")
        print("=        equipo azul, luego el rojo       =")
        print("===========================================")
        print(" 1) Empezar partida")
        print(" 2) Instrucciones")
        print(" 2) Volver al menú de juegos")
        print(" 3) Creditos")
        print("===========================================")
        opcion=int(input("Escoge una opción: "))
        if opcion==1:
            partida()
        elif opcion==2:
            salir=True
        elif opcion==3:
            print("===========================================")
            print("")
            print("James Adrian Cañarte Quintana")
            print("")
            print("===========================================")
        else:
            print("Introduce de nuevo, la opcion fue incorrecta: ")

listapuntos=[]
