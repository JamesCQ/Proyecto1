import random
import os
import time

equipoazul = 0
equiporojo = 0

def partida():
    jugando=True
    global equipoazul
    global equiporojo
    turno = 1
    while jugando:
        os.system("cls")
        if turno==1:
            dado = random.randint(1,6)
            print("")
            print("~~~~~~~~~~~~~~~~~~~~")
            print("Tu turno equipo azul")
            print("~~~~~~~~~~~~~~~~~~~~")
            input("Pulsa Enter para tirar de dado ...")
            os.system("cls")
            print("Tirando dado...")
            time.sleep(2)
            print("Ha tocado el número", dado)
            print("Tu puntuación anterior es de: ", equipoazul)
            equipoazul+=dado
            print("Así que ahora es de: ", equipoazul)
            if equipoazul==21:
                jugando=False
                print("Equipo azul gana!")
                equipoazul=0
                time.sleep(5)
                menu_parchis()
            elif (equipoazul>21):
                equipoazul-=dado
                print("Te has pasado, así que se resta el dado a tu número de posicion actual")
                print("Tu puntuación actual es de: ", equipoazul)
            input("Pulsa Enter para pasar al siguiente turno...")
            turno = 2

        elif turno==2:
            dado = random.randint(1,6)
            print("")
            print("~~~~~~~~~~~~~~~~~~~~")
            print("Tu turno equipo rojo")
            print("~~~~~~~~~~~~~~~~~~~~")
            input("Pulsa Enter para tirar de dado ...")
            os.system("cls")
            print("Tirando dado...")
            time.sleep(2)
            print("Ha tocado el número", dado)
            print("Tu puntuación anterior es de: ", equiporojo)
            equiporojo+=dado
            print("Así que ahora es de: ", equiporojo)
            if equiporojo==21:
                jugando=False
                print("Equipo rojo gana!")
                equiporojo=0
                time.sleep(5)
                menu_parchis()
            elif (equiporojo>21):
                equiporojo-=dado
                print("Te has pasado, así que se resta el dado a tu número de posicion actual")
                print("Tu puntuación actual es de: ", equiporojo)
            input("Pulsa Enter para pasar al siguiente turno...")
            turno = 1

def instrucciones():
    os.system("cls")
    print("")
    print("===========================================")
    print("=El primero que llegue a los 21 puntos sin=")
    print("=         pasarse, gana. Suerte :)        =")
    print("===========================================")
    print("")
    input("Pulsa Enter para volver al menú...")

def menu_parchis():
    salir=False
    while salir==False:
        os.system("cls")
        print("===========================================")
        print("= BIENVENIDO AL PARCHIS DE DOS JUGADORES! =")
        print("= Habrán dos equipos, primero comienza el =")
        print("=        equipo azul, luego el rojo       =")
        print("===========================================")
        print(" 1) Empezar partida")
        print(" 2) Instrucciones")
        print(" 3) Volver al menú de juegos")
        print(" 4) Creditos")
        print("===========================================")
        opcion=int(input("Escoge una opción: "))
        if opcion==1:
            partida()
        elif opcion==2:
            instrucciones()
        elif opcion==3:
            salir=True
        elif opcion==4:
            print("===========================================")
            print("")
            print("James Adrian Cañarte Quintana")
            print("")
            print("===========================================")
        else:
            print("Introduce de nuevo, la opcion fue incorrecta: ")