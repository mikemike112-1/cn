# Import pygame here
import pygame as pg

# Let's define some familiar variables
WIDTH = 600
HEIGHT = 600
FPS = 60

# Let's define some color variables using RGB values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and the display window we will be using
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Non-integer movement Example")
clock = pg.time.Clock()

# This is going to be our class for the Player object
# pg.sprite.Sprite is simply a way for us to refer to the main Player object and have the object be updated
# and controlled by using the code and functions inside of our class here
class Player(pg.sprite.Sprite):

    # __init__ is going to be used to create some initial properties and variables for our class
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # vx is short for velocity-x, or in other words the velocity on the x-axis
        # you can think of velocity as direction and speed
        self.vx = 120

        # px is short for pixel and is a placeholder for now, it will be used more in the later code
        self.px = 0

        self.rect.left = 0
        self.rect.centery = HEIGHT / 2

    # This function updates the position of the square on the screen
    def update(self, dt):
        self.px += self.vx * dt
        if self.px > WIDTH:
            self.px = 0
        self.rect.x = self.px

# these variables create a new player and adds the player to the game
all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True

while running:
    # keep loop running at the right speed
    dt = clock.tick(FPS) / 1000
    # This for loop checks to see what you have clicked or typed
    for event in pg.event.get():
        # checks to see if the window is being closed yet
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    # Updates where the player is on the screen
    player.update(dt)
    # Draw the sprites onto the screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
