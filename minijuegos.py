import juego1
import juego3
import Tres_en_raya

menu = ("=========================\n=      M E N Ú          =\n=========================\n 1) Juego 1\n 2) Juego 2\n 3) Juego 3\n 4) salir\n=========================")
print(menu)          #Imprimo el menu que he hecho a mano con string
opcion=int(input("¿Qué juego deseas jugar? "))       #pregunto la opcion con un int

while (opcion!=4):         #mientras que cuando te pida la opcion y no sea un 4 (salir), no se termina el bucle while
    if (opcion==1):

        print(menu)
        opcion=int(input("¿Qué juego deseas jugar? "))
    elif (opcion==2):

        print(menu)
        opcion=int(input("¿Qué juego deseas jugar? "))
    elif (opcion==3):
        print(menu)
        opcion=int(input("¿Qué juego deseas jugar? "))