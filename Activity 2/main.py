#activity 2
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

#import is used for adding in functions that can be used inside your code
#pygame has functions that can be used for creating our games and programs
#it also has images that we will use later
import pygame

#sys is used for bringing in certain functions from inside the python
#environment(world)
import sys

#this picks a specific group of code that can be used from the pygame
#library which can be used
from pygame.locals import *

#this initializes all the part of pygame
#initialize means to prepare and setup
pygame.init()

#VARIABLES
#displaysurf is just a variable name
#in python, the variables do not need to be labeled as var such as in
#javascript
#you simply give it a name and then set it equal to what it is meant to be

#DISPLAYSURF STANDS FOR DISPLAY SURFACE
#the display surface is the size of your game screen that you will be
#building on and playing on.
#in this case, it is 400 by 300. think of x and y
#300 is the x axis and 400 is the y axis
DISPLAYSURF = pygame.display.set_mode((400, 300))

#as you can tell now, pygame.display deals with everything that is your game
#window.
#pygame.display.set_caption sets the name for your game window
#at the end, change and run the words in the quotes a few times
pygame.display.set_caption('Hello World!')

#just like in javascript, we also have a while-true loop in python,
#it looks like this...
while True: # main game loop

    #this, is a for loop that will automatically loop through all the
    #elements inside of the given list or array of stuff
    for event in pygame.event.get():

        #if statements are written similar to the following to the following
        #example
        #the "event.type" is referring to the type of event that is happening
        #the "QUIT" event happens when you clik on the x to leave the game
        if event.type == QUIT:

            #this will end all the pygame uses in the code
            pygame.quit()

            #this will exit the python window cleanly and safely
            sys.exit()

    #another pygame.display section of code
    #this will apply all the changes you made to the screen and actually
    #display them
    #since we did not make any changes to our screen, we will continue to
    #see a blank screen
    pygame.display.update()
