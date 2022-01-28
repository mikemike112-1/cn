import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (96,108,56)
BLUE = (0,0,255)
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14,0), (291,106), (236, 277)))
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14,0), (291,106), (236, 277), (56, 277)))
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14,0), (291,106), (236, 277), (56, 277), (0,806)))
pygame.draw.polygon(DISPLAYSURF, BLUE, ((146,0), (291,106), (236, 277), (56, 277), (0,106)))
pygame.draw.line(DISPLAYSURF, RED, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, RED, (120, 60), (60, 120))
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 150), 20, 10)
pygame.draw.ellipse(DISPLAYSURF, RED, (400, 50, 10, 80), 2)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

