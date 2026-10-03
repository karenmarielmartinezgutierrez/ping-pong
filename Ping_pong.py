import pygame
from pygame.locals import *

run = True

pygame.init()

ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ping Pong - Fondo Rosa")
clock = pygame.time.Clock()

# Colores
ROSA = (255, 182, 193)
MORADO = (150, 100, 200)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):

        self.rect = pygame.Rect(x, y, width, height)

        self.fill_color = ROSA

        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(
            ventana,
            self.fill_color,
            self.rect
        )

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

#Clase imagen
class Picture(Area):

    def __init__(self, filename, x=0, y=0, width=10, height=10):

        Area.__init__(
            self,
            x=x,
            y=y,
            width=width,
            height=height
        )

        self.image = pygame.image.load(filename).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (width, height)
        )

    def draw(self):

        ventana.blit(
            self.image,
            (self.rect.x, self.rect.y)
        )

# Paletas
jugador1 = Area(
    40,
    230,
    25,
    140,
    MORADO
)

jugador2 = Area(
    735,
    230,
    25,
    140,
    MORADO
)

#Pelota
pelota = Picture(
    "Pelota.png",
    375,
    275,
    50,
    50
)

# Velocidades
velocidad_paleta = 7

velocidad_x = 5
velocidad_y = 5

# Texto
fuente = pygame.font.SysFont(
    "Arial",
    45
)





    # Actualizar la pantalla
    pygame.display.update()

    clock.tick(60)

pygame.quit()




