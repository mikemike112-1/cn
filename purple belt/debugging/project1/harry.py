import pygame
import sys
import time
from pygame.locals import *
 # good
width = 400
height = 500
XO = 'x'
winner = None
cat = False
white = (255, 255, 255)
black = (0, 0, 0)
TTT = [[None] * 3, [None] * 3, [None] * 3]
pygame.init()
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Potico Potaco Potoeto')
start = pygame.image.load('mainScreen.png')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
start = pygame.transform.scale(start, (width, height))
x = pygame.transform.scale(x, (80, 80))
o = pygame.transform.scale(o, (80, 80))


def opening():
    screen.blit(start, (0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    pygame.draw.line(screen, black, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, black, (2 * width / 3, 0), (2 * width / 3, height), 7)
    pygame.draw.line(screen, black, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, black, (0, 2 * height / 3), (width, 2 * height / 3), 7)
    draw_status()


def draw_status():
    global cat
    if winner is None:
        message = XO.upper() + "'s turn"
    elif cat:
        message = "Cat (tie)!"
    else:
        message = winner.upper() + " won!"
    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, black)
    rect = text.get_rect(center=(width / 2, height - 50))
    screen.fill(white, rect)
    screen.blit(text, rect)
    pygame.display.update()


def checkwin():
    global TTT, winner, cat
    for row in range(0, 2):
        if (TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None):
            winner = TTT[row][0]
            break
    for col in range(0, 2):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            winner = TTT[0][col]
            break
    if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
        winner = TTT[0][0]
    if (TTT[2][0] == TTT[1][1] == TTT[0][2]) and (TTT[2][0] is not None):
        winner = TTT[2][0]
    if all([all(row) for row in TTT]) and winner is None:
        cat = True
    draw_status()


def drawXO(row,col):
    global TTT, XO
    # HARRY MODIFIED HERE
    posy = row * height / 3 + 30
    posx = col * width / 3 + 30
    TTT[row][col] = XO
    if XO == "x":
        screen.blit(x, (posx, posy))
        XO = "o"
    else:
        screen.blit(o, (posx,posy))
        XO = "x"
    pygame.display.update()


def click():
    x, y = pygame.mouse.get_pos()
    if x < width/3:
        col = 0
    elif x < 2 * width/3:
        col = 1
    elif x < width:
        col = 2
    else:
        col = None
    if y < height/3:
        row = 0
    elif y < 2 * height/3:
        row = 1
    elif y < height:
        row = 2
    else:
        row = None
    if row and col and TTT[row][col] is None:
        global XO
        drawXO(row,col)
        checkwin()


def reset():
    global TTT, winner, XO, cat
    time.sleep(3)
    XO = "x"
    cat = False
    opening()
    winner = None
    TTT = [[None] * 3, [None] * 3, [None] * 3]



screen.fill(white)
opening()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit("well EXCUUUUUUUSE me")
        elif event.type == MOUSEBUTTONDOWN:
            click()
            if winner or cat:
                reset()
    pygame.display.update()
    clock.tick(fps)
