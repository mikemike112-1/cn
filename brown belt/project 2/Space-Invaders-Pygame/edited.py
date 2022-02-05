# these are our imports for this projects
# this one introduces a couple of new imports: math and random
# both of these are libraries with different functions that we will use
# the 'import random' will help us in making things a bit random
# the 'import math' will help us to do some math related stuff later
import math
import random

import pygame

# remember how in the past we wrote an * at the end?
# well, in this form we are specifying exactly what it is that we want to import from pygame
# mixer is useful when dealing with sounds
from pygame import mixer

# Initialize the pygame functions
pygame.init()

# create the screen like we typically do
screen = pygame.display.set_mode((800, 600))

# here, we are defining a variable with the background image we will be using
background = pygame.image.load('background.png')

# here is our first time ever using sound in our games
# this first line loads and prepares a specific sound file into our program
mixer.music.load("background.wav")

#COME BACK LATER: WHAT DOES THIS DO?
mixer.music.play(-1)

# this sets the name of our window like we have done previously
pygame.display.set_caption("Space Invader")

# this line loads and prepares the image we will use for our icon on the window
# we have not been using the icon much in the past if at all
icon = pygame.image.load('ufo.png')
#this line will set the image to be our icon
pygame.display.set_icon(icon)

# These are our variables that we will use later for the player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
# This variable will later be used to define what the change in x for the player is when the player moves left and right
# think of it as being similar to the speed of the player
playerX_change = 0

# These are the enemy variables
# This game has many empty arrays that will be filled and used later
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
# this is the number of enemies and as you have guessed can be changed later to choose how many enemies you can put
# on the screen
# WARNING: do not change this number until after your code works and runs perfectly
# come back at the end in order to change it
num_of_enemies = 6

# here we have a for loop
# this for loop will go through and make enemies depending on how many enemies you have set in the variable earlier
# notice how the variable num_of_enemies is being passed into the for loop as the range
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# The bullet variables are below
# 'ready' is going to be used for the bullet_state when the bullet is not currently fired
# 'fire' is going to be used when the bullet is currently visible on the screen
# most of these should be familiar
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
# this variable is used to define the speed of the bullet in the x coordinate or the left-right direction
# it is 0 because the bullet does not go sideways
bulletX_change = 0
# the speed here for the y coordinate is 10
bulletY_change = 10
bullet_state = "ready"

# the score variables are below
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# the x and y positions are defined here for some of the text we will be making later
textX = 10
testY = 10

# the Game Over font is defined and created here
over_font = pygame.font.Font('freesansbold.ttf', 64)

# this function is being used to define and show the score
# the x and y coordinates are being passed in as far as where the score will be placed
def show_score(x, y):
    # this line is making the line of text for the score
    # str() is telling the program to turn what is in the parentheses into a string
    # you can think of a string as text and letters
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))

    # this like will place the text onto the screen
    screen.blit(score, (x, y))

# this is just like show_score, the only difference is the text which says GAME OVER now
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# this function is used to tell the player where to appear on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# this function is used to tell a specific enemy where it should appear on the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# this funciton is used to fire a bullet
def fire_bullet(x, y):
    # the word 'global' means that the variable is now accessible anywhere on the screen
    global bullet_state
    # if you recall from the top of the code, the state of the bullet can be changed and here it is being set again
    bullet_state = "fire"
    # from the other lines we have done so far, what do you think this line does?
    screen.blit(bulletImg, (x + 16, y + 10))

# this function checks whether the bullet has hit an enemy
# the simplest way of checking this is by checking if the two objects are at the same place
# that is why you see x and y values being passed in
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    # a result of true means it there has been a collission, false means there has not been a collision
    if distance < 27:
        return True
    else:
        return False


# This is the loop that runs the game
running = True
while running:

    # this line should be quite familiar to you now, it fills the background of the screen to be white
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # these if statements check which key has been pressed on the keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # here we see how sound is played and when it is played
                    # under what condition do we get to hear the sound played?
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # if the enemy reaches the player then the game is over
        # see if you can figure out how this code works
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # this code will update the position of the specific enemny on the screen
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # this code checks if a collision has happened by checking if the function we made earlier
        # returns as true or false
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        # if the function returns as true then this code will run
        # go through this code line by line and see if you can determine what each line does
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # hint: random.randint() will give you a random integer (whole number) between a certain minimum and maximum
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # These next couple if statements help to control the bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # this function calls the player function from above while telling it where to go using the two
    # parameters passed inside
    player(playerX, playerY)

    # this function will call the function that shows the score
    show_score(textX, testY)

    # lastly, this line should be familiar because it updates the display your game will be running on
    pygame.display.update()
