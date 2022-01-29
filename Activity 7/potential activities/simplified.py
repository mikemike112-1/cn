#!/usr/bin/env python

# import statements
import pygame
import sys
import time
import random

from pygame.locals import *

# frames per second
FPS = 5

# initializes pygame here
pygame.init()

# frames per second
fpsClock = pygame.time.Clock()

# defines the variables for the screen size
# You will use these variables later to create the pixel size of the game window you will be
# playing your game in later
#this is the width (left to right)
SCREEN_WIDTH = 640

#this is the height (up to down)
SCREEN_HEIGHT = 480

# previously you were using DISPLAYSURF to make the screen and its dimension
# in this game, we will use the variable name, 'screen'
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# pygame.surface is used for various display related and screen related functions that you will be using throughout
# the code
# the DISPLAYSURF.get_size() will automatically retrieve the size of the screen to make sure that the objects we
# will place on the screen are able to be used in the same width and height
surface = pygame.Surface(DISPLAYSURF.get_size())

# this is used solely for pixel formatting. it is not neccessarily visible to us therefore we are not going to spend
# very much time on it
surface = surface.convert()

# this will fill in the background of the display with a specific color
# it is using the rgb formatting here, (255, 255, 255), which is also the color white
surface.fill((255, 255, 255))

# the clock is used to control and keep track of how often the games display/screen refreeshes itself
clock = pygame.time.Clock()

# this will control how many often your computer will read-in a specific key on your keyboard when it is held down
pygame.key.set_repeat(1, 40)

# this defines the gridsize
# the gridsize is used for several calculations with the screen later on
GRIDSIZE = 10

# MAYBE PUT IN AN EXAMPLE OF A GRID HERE FOR THE STUDENTS TO BETTER UNDERSTAND A GRID AND WHAT IT DOES OR LOOKS LIKE

# this is a calculation used to define how the screen is split up
# in this particular case, by dividing the screen into 10 parts we can reference the screen in more reasonable spots
# do you remember the value of SCREENWIDTH? Look above if you do not
# that is a very large number, imagine if that number was what we used to place our snake and snake food, then it would
# all be way too small for us to actually see and play. Therefore by dividing the screen by 10 we are able to make the
# screen much easier to play with
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE

# we are doing the same thing we did with the width here on the height as well
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

# these coordinates are used to tell the snake which direction to go
# we will use them later to change directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# here is some more screen formatting which we will not discuss too much at this time
DISPLAYSURF.blit(surface, (0, 0))

# this is our first function, it should look familiar to the activity which you did in the past with functions
# it is used to draw a box
# a box is the same as the small squares that will be appearing on the screen
# this function has 3 parammeters that will be passed in from the calling of the function later in the code
# surf is used for the surface size in pixels
# color is the color of the box which will be passed in
# pos is used to tell the current position or location that the box is going to be placed
def draw_box(surf, color, pos):

    # this variable will be using the parameter pos to get the x and y coordinates that the rectangle will be made on
    # gridsize simply is telling the rectangle what size it will be in pixels
    # look above if you do not remember how large GRIDSIZE is
    # remember that the function follows the
    r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))

    pygame.draw.rect(surf, color, r)


class Snake(object):
    def __init__(self):
        self.lose()
        self.color = (0, 0, 0)

    def get_head_position(self):
        return self.positions[0]

    def lose(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def point(self, pt):
        if self.length > 1 and (pt[0] * -1, pt[1] * -1) == self.direction:
            return
        else:
            self.direction = pt

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y * GRIDSIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.lose()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surf):
        for p in self.positions:
            draw_box(surf, self.color, p)


class Apple(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize()

    def randomize(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    def draw(self, surf):
        draw_box(surf, self.color, self.position)


def check_eat(snake, apple):
    if snake.get_head_position() == apple.position:
        snake.length += 1
        apple.randomize()


if __name__ == '__main__':
    snake = Snake()
    apple = Apple()
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.point(UP)
                elif event.key == K_DOWN:
                    snake.point(DOWN)
                elif event.key == K_LEFT:
                    snake.point(LEFT)
                elif event.key == K_RIGHT:
                    snake.point(RIGHT)

        surface.fill((255, 255, 255))
        snake.move()
        check_eat(snake, apple)
        snake.draw(surface)
        apple.draw(surface)
        font = pygame.font.Font(None, 36)
        text = font.render(str(snake.length), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = 20
        surface.blit(text, textpos)
        DISPLAYSURF.blit(surface, (0, 0))

        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS + snake.length / 3)
