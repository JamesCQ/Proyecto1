""" Triki """
import pygame
import numpy as np
# Constantes
#pygame.init()
ANCHO = 640
ALTO = 480
# Posiciones lineas
L=ANCHO/3
A=ALTO/3
# Posiciones jugadores
L1=L/2
A1=A/2
#Inidices 
I1=[L1,A1]
I2=[3*L1,A1]
I3=[5*L1,A1]
I4=[L1,3*A1]
I5=[3*L1,3*A1]
I6=[5*L1,3*A1]
I7=[L1,5*A1]
I8=[3*L1,5*A1]
I9=[5*L1,5*A1]
I=np.array([I1,I2,I3,I4,I5,I6,I7,I8,I9])
## Poniendo color  y hacer las lineas
def lineas(screen):
    screen.fill([255,255,255])
    for i in range(1,3):
         pygame.draw.line(screen,(0,0,0),(L*i,0),(L*i,ALTO))
         pygame.draw.line(screen,(0,0,0),(0,A*i),(ANCHO,A*i))     
## Jugadores
def jugadores(screen,I):
    indices=np.array(range(1,10))
    l=np.random.randint(1,3)
    indices1=np.array(['1','2','3','4','5','6','7','8','9'])
    for i in range(1,10):
        if l==1:
            A=np.random.choice(indices)
            B=np.array(np.where(indices==A))
            indices1[A-1]='O'
            pygame.draw.circle(screen,(0,255,0),(int(I[B[0][0]][0]),int(I[B[0][0]][1])),60)
            indices=np.delete(indices,B)
            I=np.delete(I,B,0)
            l=2 
            if indices1[0]==indices1[4] and indices1[4]==indices1[8]:
               break
            elif indices1[2]==indices1[4] and indices1[4]==indices1[6]:
               break
            elif indices1[0]==indices1[1] and indices1[1]==indices1[2]:
                break
            elif indices1[3]==indices1[4] and indices1[4]==indices1[5]:
                break
            elif indices1[6]==indices1[7] and indices1[7]==indices1[8]:
                break
            elif indices1[0]==indices1[3] and indices1[3]==indices1[6]:
                break
            elif indices1[1]==indices1[4] and indices1[4]==indices1[7]:
                break
            elif indices1[2]==indices1[5] and indices1[5]==indices1[8]:
                break
        elif l==2:
            A=np.random.choice(indices)
            B=np.array(np.where(indices==A))
            indices1[A-1]='X'
            pygame.draw.circle(screen,(255,0,0),(int(I[B[0][0]][0]),int(I[B[0][0]][1])),60)
            indices=np.delete(indices,B)
            I=np.delete(I,B,0)
            l=1
            if indices1[0]==indices1[4] and indices1[4]==indices1[8]:
               break     
            elif indices1[2]==indices1[4] and indices1[4]==indices1[6]:
               break
            elif indices1[0]==indices1[1] and indices1[1]==indices1[2]:
                break
            elif indices1[3]==indices1[4] and indices1[4]==indices1[5]:
                break
            elif indices1[6]==indices1[7] and indices1[7]==indices1[8]:
                break
            elif indices1[0]==indices1[3] and indices1[3]==indices1[6]:
                break
            elif indices1[1]==indices1[4] and indices1[4]==indices1[7]:
                break
            elif indices1[2]==indices1[5] and indices1[5]==indices1[8]:
                break
        print('Progreso: \n',np.array([[indices1[0:3]],[indices1[3:6]],[indices1[6:9]]]))
def main():
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TIC TAC TOE")
    icono=pygame.image.load('C:/Users/bella/Desktop/Epython/tOBY.png')
    pygame.display.set_icon(icono)
    lineas(screen)
    jugadores(screen,I)
    corriendo=True
    while corriendo:
        for eventos in pygame.event.get():
          if eventos.type == pygame.QUIT:
              corriendo=False
        pygame.display.update()
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()