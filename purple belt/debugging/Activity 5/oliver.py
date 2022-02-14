import pygame
import sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Hello!')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((104, 90), (25, 222), (265, 291), (58, 17), (90, 33), (5, 106)))
pygame.draw.polygon(DISPLAYSURF, BLACK, ((264, 230), (251, 236), (66, 97), (88, 167), (55, 126), (30, 106)))
pygame.draw.polygon(DISPLAYSURF, BLUE, ((22, 28), (211, 196), (255, 107), (59, 187), (27, 96), (234, 11)))
pygame.draw.polygon(DISPLAYSURF, RED, ((14, 0), (291, 106), (236, 277), (56, 277), (0, 806), (0, 106)))
FPS = 30
fpsClock = pygame.time.Clock()
catlol = pygame.image.load('catlol')

catx = 10
caty = 10
direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
