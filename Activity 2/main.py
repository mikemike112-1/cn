#import statements 
import pygame 
import sys
from pygame.locals import *

# this will initialize your pygame functions and code 
# pieces and assets you will use in your program 
pygame.init()

# creating your window 
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

# here we can modify DISPLAYSURF to have a different background
# color
# You can try colors like:
# RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE
DISPLAYSURF.fill(WHITE)

# now you are going to draw different shapes on the screen
# the first one we will draw is a "polygon"
# to do so, follow thses steps 
# step 1:
# pygame.draw
# this tells pygame that we want access to the draw library 
# step 2: 
# pygame.draw.polygon()
# this tells pygame that we want to draw a polygon
# "polygon" simply refers to a shape with many sides 
# step 3: 
# pygame.draw.polygon(DISPLAYSURF)
# DISPLAYSURF is here because it is telling the program where we 
# want the shape to be drawn on top of 
# step 4: 
# add in the color as the next parameter  
# pygame.draw.polygon(DISPLAYSURF, GREEN)
# step 5: 
# add in your first point here. you need at least 3 points in 
# order to form the most basic shape, a triangle 
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14, 0), (291, 106), (236, 277)))

#now we can create a polygon with 4 points 
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14, 0), (291, 106), (236, 277), (56, 277)))

# and then 5 points
pygame.draw.polygon(DISPLAYSURF, GREEN, ((14, 0), (291, 106), (236, 277), (56, 277), (0, 806)))

# practice by drawing this one as well, with a different color
pygame.draw.polygon(DISPLAYSURF, BLUE, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# now you will draw a line 
# it is very similar to the polygon with just a few differences
# instead of using ".polygon", you will use ".line"
# instead of having unlimited points, like a polygon
# this one can only have 2 points because lines only have 2 points
# the start and the end 
# the last number "4" is the width of the line and you can change to whatever you want 
pygame.draw.line(DISPLAYSURF, RED, (60, 60), (120, 60), 4)

# practice by drawing another line 
# this time this one does not have a number at the end, it will default to having a width of 1 
pygame.draw.line(DISPLAYSURF, RED, (120, 60), (60, 120))

# now we are going to make a circle
# this one has one coordinate which is showing where the circle will go
# the number "20" is showing what the size of the circle should be
# the number 0 is a placeholder that will allow you make a hole in your circle later
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)

# let's make another circle, this one with a hole in the middle 
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 150), 20, 10)

# now let's draw an ellipse
# an ellipse is basically like an oval 
# notice how it takes 4 numbers instead of 2 for the coordinates
# the first 2 numbers tell the ellipse where to go
# the third number tells the ellipse how wide it should be (left-to-right)
# the forth number tells the ellipse how tall to make the ellipse up to down
# the last number, outside the parantheses, defines how wide to make the ellipse line 
pygame.draw.ellipse(DISPLAYSURF, RED, (400, 50, 10, 80), 2)

# now we will draw a rectangle 
# the first 2 numbers tell where the rectangle should be placed
# the third number tells how wide it should be (left-to-right)
# the fourth number tells how high it should be (up-to-down) 
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

# ------------------------------------------
### I DONT THINK I EVEN NEED THESE LINES HERE... REMOVING THEM DIDN'T CHANGE ANYTHING
# pixObj = pygame.PixelArray(DISPLAYSURF)
# pixObj[480][380] = BLACK
# pixObj[482][382] = BLACK
# pixObj[484][384] = BLACK
# pixObj[486][386] = BLACK
# pixObj[488][388] = BLACK
# del pixObj
# ------------------------------------------

# running the game here 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()