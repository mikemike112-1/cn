# Activity 8
# learning objectives:
#   - import
#   - pygame
#   - sys
#   - pygame.locals
#   - import *
#   - whileTrue
#   - indentation
#   - if
#   - self

#Import pygame
import pygame

#Setting up our Variables
WIDTH = 480
HEIGHT = 600
FPS = 60

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("move a box!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    # self in python is referring to the object you are in, it is just like $this from JavaScript
    def __init__(self):
        #Initializing the sprite
        pygame.sprite.Sprite.__init__(self)
        #Setting up the size, color, and shape of the sprite
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    #Creating a function to update itself (the rectangle)
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        #Checks which arrow key was pressed and moves the sprite accordingly
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()