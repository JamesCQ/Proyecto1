import random

def tirada(listapuntos):
    fic1 = 0
    fic2 = 0
    fic3 = 0
    fic4 = 0
    fichas = fic1+fic2+fic3+fic4

def partida():
    while fichas!=19:
        print("Tu turno equipo azul")

def menu_parchis():
    salir=False
    while salir==False:
        print("===========================================")
        print("= BIENVENIDO AL PARCHIS DE DOS JUGADORES! =")
        print("= Habrán dos equipos, primero comienza el =")
        print("=        equipo azul, luego el rojo       =")
        print("===========================================")
        print(" 1) Empezar partida")
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
