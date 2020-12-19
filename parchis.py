import random

<<<<<<< HEAD
def partida(listapuntos):
    while
=======
def tirada(listapuntos):
    if fic1==76:
        puntos+=1
    elif fic2==76:
        puntos+=1
    elif fic3==76:
        puntos+=1
    elif fic4==76:
        puntos+=1

    dado1 = random.randrange(1,6)
    dado2 = random.randrange(1,6)        
    
def partida():
    while puntos!=4:
        print("")
        print("~~~~~~~~~~~~~~~~~~~~")
        print("Tu turno equipo azul")
        print("~~~~~~~~~~~~~~~~~~~~")
        tirada()
        if dado1


>>>>>>> a138ea47d3f005a50be2ae0645fbc971fdc238c6

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
            
puntos = 0
fic1 = 0
fic2 = 0
fic3 = 0
fic4 = 0

listapuntos=[]
