"""
PUT THIS IN BEFORE PURPLE BELT RIGHT BEFORE SNAKE
"""

# this activity is going to show you how you can move an object on your screen by using the arrow keys

# this is our typical pygame import that will let us use pygame functions
import pygame as pg

# the variables for our screen are defined here
WIDTH = 800
HEIGHT = 600
# FPS stands for frames per second
FPS = 60

# these are the variables for our colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# this is going to initialize pygame
pg.init()

# COME BACK: I DO NOT KNOW WHY THIS IS HERE
pg.mixer.init()

# create our screen
screen = pg.display.set_mode((WIDTH, HEIGHT))

# the title of the game screen
pg.display.set_caption("4-way vs. 8-way Movement")

# this variable will be used for updating the screen later
clock = pg.time.Clock()

# this is a class for the Player object
class Player(pg.sprite.Sprite):

    # this __init__ function is used to initialize the game itself
    def __init__(self):
        # COME BACK: I DONT KNOW WHAT THIS DOES
        pg.sprite.Sprite.__init__(self)

        # all of the 'self' words that you see are similar to saying $this in JavaScript
        # what was the purpose of $this in JavaScript?
        self.image = pg.Surface((50, 50))

        # this line will fill the screen's background to be colored green
        self.image.fill(GREEN)

        # this line will set the rectangle variable to be a rectangle
        self.rect = self.image.get_rect()

        # vx is an abbreviation for velocity x and
        # vy is an abbreviation for velocity y
        self.vx, self.vy = 0, 0

        # this is making a property for the class which will get the center of the rectangle
        # by diving the width by 2 we are able to get the center of the width and then by
        # dividing the height by 2 we get the center of the height
        # when both of these centers are combined we are left at the center of the rectangle
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    # this function will update the position of the rectangle
    def update(self):
        self.vx, self.vy = 0, 0
        self.move_8way_fixdiag()
        self.rect.x += self.vx
        self.rect.y += self.vy

        # these lines will stop the rectangle from going off the edges of the screen
        # these are similar to lines we have done in JavaScript many times
        # can you figure out how each if statement works?
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    # stopped here, everything below is not my code
    def move_4way(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vy = -5
        elif keystate[pg.K_DOWN]:
            self.vy = 5
        elif keystate[pg.K_LEFT]:
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.vx = 5

    def move_8way(self):
        self.vx, self.vy = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vy += -5
        if keystate[pg.K_DOWN]:
            self.vy += 5
        if keystate[pg.K_LEFT]:
            self.vx += -5
        if keystate[pg.K_RIGHT]:
            self.vx += 5

    def move_8way_fixdiag(self):
        self.move_8way()
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pg.display.flip()

pg.quit()
