import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (120, 0, 120)
LIGHTBLUE = (146, 209, 255)
PINK = (255, 144, 252)
# colors = (WHITE, GREEN, PINK, PURPLE, LIGHTBLUE)

colors = ("z", "za", "zac", "zach", "zach!")


def changeColor():
    DISPLAYSURF2 = pygame.display.set_mode((400, 300))
    fontObj2 = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj2 = fontObj2.render('cool stuff', True, GREEN, BLUE)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (200, 150)
    DISPLAYSURF2.fill((255, 255, 255))
    DISPLAYSURF2.blit(textSurfaceObj2, textRectObj2)
    for color in colors:
        textSurfaceObj2 = fontObj2.render(color, True, GREEN, BLUE)
        textSurfaceObj2 = fontObj2.render(color, True, GREEN, BLUE)

        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj2.center = (200, 150)
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
        pygame.display.update()
        time.sleep(1)


while True:
    changeColor()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()