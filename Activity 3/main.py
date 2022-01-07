# activity 3
# learning objectives:
#   - import
#   - pygame
#   - sys
#   - pygame.locals
#   - import *
#   - whileTrue 
#   - indentation
#   - if
#   - loading in images
#   - animation
#   - fps
#   - updating the display

import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
# text that shows up at the top when the game begins
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)
# loading in the image that we imported in
### MAKE SURE YOU CHANGE THE FILE NAME TO THE NAME OF YOUR IMAGE!!
catImg = pygame.image.load('cat.png')
# setting up variables that will be used to set the coordinates of the image
catx = 10
caty = 10
# the "direction" variable will be used to change the direction our image moves in
direction = 'right'

while True: # the main game loop
    # makes the background color to white
    DISPLAYSURF.fill(WHITE)
    # conditional statements that check what the current direction is
    # the goal of the game is to make our image float around in a square like pattern
    # so, once our image "hits" a certain corner, we change the direction to the next movement
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
    # the blit functon allows our image to show up on our gui(graphical user interface)
    # we first pass in the image & then the x and y coordinates
    DISPLAYSURF.blit(catImg, (catx, caty))
    # this for loop is used to check what the current event is
    # once the user quits out of the gui, it allows the gui to exit and close nicely
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # the update() function is used to update the gui
    pygame.display.update()
    # FPS: frames per second
    # fps can be used to set up how many frames the user will see
    # the higher amount of frames => the screen will be updated more frequently
    # the lower amount of frames => can lead to the user missing out on certain frames / actions
    # for example when playing games, you want a higher fps, that way the user is able to see the actions 
    # faster and more frequently
    fpsClock.tick(FPS)