import random

def tiradadados(listapuntos):
    puntos=dict()
    dado1=random.randrange(1,6)
    dado2=random.randrange(1,6)
    puntos[0]=dado1
    puntos[1]=dado2
    listapuntos.append(puntos)

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
            print("1")
        elif opcion==2:
            salir=True
        elif opcion==3:
            print("James Adrian Cañarte Quintana")
        else:
            print("Introduce de nuevo, la opcion fue incorrecta: ")
            
listapuntos=[]
