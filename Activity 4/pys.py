import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

def cycle():
    textSurfaceObj1 = fontObj.render('Hello world!', True, GREEN, WHITE)
    textSurfaceObj2 = fontObj.render('Hello world!', True, GREEN, BLUE)
    DISPLAYSURF.blit(textSurfaceObj1, textRectObj)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj)



while True:
    DISPLAYSURF.fill(WHITE)
    cycle()

    #DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()