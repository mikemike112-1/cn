import pygame
import sys
from pygame.locals import *
pygame.init()
FPS = 32.5
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

Celebratory_1 = pygame.image.load('cat.png')
Celebratory_3 = pygame.image.load('cat.png')
Celebratory_4 = pygame.image.load('cat.png')




celebratex = 10
celebratey = 10

direction = 'right'

while True:  # the main game loop

    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        celebratex += 1
        if celebratex == 280:
            direction = 'down'
    elif direction == 'down':
        celebratey += 0.5
        if celebratey == 220:
            direction = 'left'
    elif direction == 'left':
        celebratex -= 1
        if celebratex == 10:
            direction = 'up'
    elif direction == 'up':
        celebratey -= 0.5
        if celebratey == 10:
            direction = 'right'

    DISPLAYSURF.blit(Celebratory_1, (celebratex, celebratey))
    DISPLAYSURF.blit(Celebratory_3, (celebratex + 80, celebratey))
    DISPLAYSURF.blit(Celebratory_4, (celebratex + 160, celebratey))

    pygame.draw.line(DISPLAYSURF, RED, (10, 10), (20, 10), 5)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)