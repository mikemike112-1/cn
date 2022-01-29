#pasta
import pygame
import sys
from pygame.locals import *
pygame.init()

CYAN = (0, 200, 220)
CYANOFF = (0, 150, 170)
grey = (150, 150, 150)
WHITE1 = (230, 220, 235)
DISPLAYSURF = pygame.display.set_mode((500, 600))
DISPLAYSURF.fill(grey)
pygame.draw.rect(DISPLAYSURF, CYAN, [50, 50, 400, 1150])
pygame.draw.rect(DISPLAYSURF, CYANOFF, (50, 700, 400, 1200))
#                                         top left    top right   bottom right  bottom left
pygame.draw.polygon(DISPLAYSURF, WHITE1, ((0, 1150), (100, 1160), (90, 1250), (0, 1290)))
pygame.draw.polygon(DISPLAYSURF, WHITE1, ((300, 1150), (450, 1150), (470, 1240), (290, 1290)))
pygame.draw.polygon(DISPLAYSURF, WHITE1, ((140, 1150), (200, 1160), (210, 1250), (130, 1290)))

ey = 50;
effect = pygame.draw.rect(DISPLAYSURF, WHITE1, (50, ey, 10, 100))

while True:
    # pygame.draw.rect(DISPLAYSURF, WHITE1, (50, ey, 10, 100))
    effect.move(50, ey + 10)
    pygame.time.delay(1000)
    ey -= 25;
    #DISPLAYSURF.blit(effect, (effectx, ey))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()