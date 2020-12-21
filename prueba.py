import random
import os
import time

equipo1 = 0
equipo2 = 0
jugando = True

while jugando:

    dado = random.randint(1,6)
    opcion = int(input("opcion: "))
    if (opcion==1):
        print("te ha tocado el numero: ", dado, "en el dado")
        equipo1+=dado
        print("ahora tus puntos equipo1 ahora son: ", equipo1)
    elif (opcion==2):
        print("te ha tocado el numero: ", dado, "en el dado")
        equipo2+=dado
        print("ahors tus puntos equipo2 ahora son: ", equipo2)
    else:
        print("intentalo de nuevo: ")

    if (equipo1>=20):
        jugando=False
        print("Ganas equipo1")
    elif (equipo2>=20):
        jugando=False
        print("Ganas equipo2")