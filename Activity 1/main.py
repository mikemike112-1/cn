#activity 1
#learning objectives:
#   -import
#   -pygame
#   -sys
#   -pygame.locals
#   -import *
#   -whileTrue
#   -tabs
#   -if
#   -AND MORE STUFF BUT NEED TO MAKE IT STRATEGIC AS WELL
#   NOT J DO A DUMP OF STUFF 
#
#   before continuing: ask the ninja what each of these are and
#   how they used each of these inside of this activity
#   if there is any lack of clarity: simply move backwards and
#   do a little more practice


import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
