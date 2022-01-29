# potential objectives
# advanced variable uses
#

import pygame
import sys
import time
import random

from pygame.locals import *
pygame.init()

# here
# you can use variables to
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300


# DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
