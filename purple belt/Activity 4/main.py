# activity 4
# learning objectives:
#   - import
#   - pygame
#   - sys
#   - pygame.locals
#   - import *
#   - whileTrue 
#   - indentation
#   - if
#   - adding in text
#   - fonts
#   - for loops

import pygame, sys
from pygame.locals import *
# "pygame.init()" initializes all the parts of pygame
pygame.init()
# DISPLAYSURF STANDS FOR DISPLAY SURFACE
# the display surface is the size of your game screen that you will be
# building on and playing on.
# in this case, it is 400 by 300. (X and Y coordinates)
# 300 is the x axis and 400 is the y axis
DISPLAYSURF = pygame.display.set_mode((400, 300))
# sets the text that will be displayed
pygame.display.set_caption('Hello World!')
# sets up the 3 colors that will be used with the RGB code
# RGB: red, green, blue
# our computers use those 3 colors to show color on our screens
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
# we use a variable to store the font and font size we will be using
fontObj = pygame.font.Font('freesansbold.ttf', 32)
# textSurfaceObj is used to show the text, the text will be green, with a blue highlight
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
# the get_rect() function will create a rectangle for the text that we added in
textRectObj = textSurfaceObj.get_rect()
# the .center method will center our text object created
textRectObj.center = (200, 150)

while True: # main game loop
    DISPLAYSURF.fill(WHITE) # makes the background white
    # the blit functon allows our image to show up on our gui(graphical user interface)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()