import random
import os 

def crea_tablero(fil,col,val):
    tablero = []
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def muestra_tablero(tablero):
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
        print()

def coloca_minas(tablero, minas, fil, col):
    minas_ocultas = []
    numero = 0
    while numero < minas:
        y = random.randint(0fil-1)
        x = random.randint(0fil-1)
        if tablero[y][x] != 12:
            tablero[y][x] = 12
            numero += 1
            minas_ocultas.append((y,x))
    return tablero, minas_ocultas

def coloca_pistas(talero,fil,col):
        for y in range(fil):
            for x in range(col):
                if tablero[y][x] == 9:
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                                if tablero[y+i][x+j]!= 9:
                                    tablero[y+i][x+j] += 1
        return tablero
def rellenado(oculto, visible, x, fil, col, val):
    ceros = [(y,x)]
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                    if visible[y+i][x+j] == val and oculto[y+i][x+j] == 0:
                        visible [y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))
                    else:
                        visible[y+i][x+j] = oculto[y+i][x+j]
    return visible

def tablero_completo(tablero, fil, col, val):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x] == val:
                return False
    return True

def presentacion():
    
    os.system("cls")
    
    print("********************************")
    print("*                              *")   
    print("*         Buscaminas           *")  
    print("*                              *")  
    print("*           w/a/s/d            *")  
    print("*                              *")  
    print("*         m - mostrar          *")  
    print("*                              *")  
    print("*    b/v - marcar/desmarcar    *")  
    print("*                              *")  
    print("*                              *")  
    print("********************************")
    print()
input("'enter' para empezar ...")

def menu ():
    print()
    opcion = input("¿w/s/a/d - m - b/v?")
    return opcion

columnas = 16
Filas = 12

visible = crea_tablero(filas, columnas, "-")

oculto = crea_tablero(filas, columnas, 0)

oculto, minas_ocultas = colocadas_minas(oculto, 15, filas, columnas)

presentacion()

y = random.randint(2, filas-3)
x = random.randint(2 , columnas-3)  

real = visible[y][x]
visibley[y][x] = "x"

os.system("cls")

muestra_tablero(visible)

minas_marcadas = []

jugando = True
while jugando:
    mov = menu()
    if mov == "w":
        if y == 0:
            y = 0
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "s"
        if y == filas-1:
            y == filas-1
        else:
            visible[y][x] = real
            y += 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "a":
        if x == 0:
            x = 0
        else:
            visible[y][x] = real 
            x -= 1
            real = visible[y][x]
            visible[y][x] = "x"
    elif mov == "d":
        if x == columnas-1:
            x = columnas-1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "x"
            
            os.system("cls")
            
            muestra_tablero(visible)
    elif mov == "b":
        if real == "-"
            visible[y][x] = "#"
            real = visible[y][x]
            if (y,x) not in minas_marcadas:
                minas_marcadas.append((y,x))
    elif mov == "v":
        if real == "#"
            visible[y][x] = "-"
            real = visible[y][x]
            if (y,x) not in minas_marcadas:
                minas_marcadas.appen 