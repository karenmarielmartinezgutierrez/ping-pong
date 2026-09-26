import pygame
from pygame.locals import *

run = True

pygame.init()

ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ping Pong - Fondo Rosa")
clock = pygame.time.Clock()

# Color rosa
ROSA = (255, 182, 193)

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    # Pintar el fondo de rosa
    ventana.fill(ROSA)

    # Actualizar la pantalla
    pygame.display.update()

    clock.tick(60)

pygame.quit()

#class Player(player.player):
    #def __init__(self,x,y):
        #super().__init__()
        #self.image = pygame.
        #self.image
        #self.rect = self.image
        #self.rect






