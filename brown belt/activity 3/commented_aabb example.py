# Import pygame
import pygame as pg

"""
The following line was in the code uncommented originally but it is never called anywhere 
"""
# vec = pg.math.Vector2

# Create the variables for the screen
WIDTH = 800
HEIGHT = 600
FPS = 60

# Create the variables for the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0, 128)
GREEN = (0, 255, 0, 128)
CYAN = (0, 255, 255, 128)
YELLOW = (255, 255, 0)
LIGHTGRAY = (150, 150, 150)
DARKGRAY = (40, 40, 40)

# Initialize pygame
pg.init()

# Create the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("AABB Collisions")

# This variable will be used to help control the screen later on
clock = pg.time.Clock()

# This function will create the text onto the screen
# You can change the location of the text in the game by changing the
# 'align' parameter to match any one of the if statements
def draw_text(text, size, color, x, y, align="nw"):

    # This is setting up the font  and font size that we will be using
    font_name = pg.font.match_font('hack')
    font = pg.font.Font(font_name, size)

    # Here we are setting up and placing the text onto the screen
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    """
    Could you please look at this and see if you can decipher what is happening and what its purpose is?
    I think I have a vague idea based on the stuff I mentioned about the parameter up there but it is not
    making any sense even with that. If you can't figure it our as well, let me know and I will modify the code to 
    remove most of this function. Thanks.
    """
    if align == "nw":
        text_rect.topleft = (x, y)
    if align == "ne":
        text_rect.topright = (x, y)
    if align == "sw":
        text_rect.bottomleft = (x, y)
    if align == "se":
        text_rect.bottomright = (x, y)
    if align == "n":
        text_rect.midtop = (x, y)
    if align == "s":
        text_rect.midbottom = (x, y)
    if align == "e":
        text_rect.midright = (x, y)
    if align == "w":
        text_rect.midleft = (x, y)
    if align == "center":
        text_rect.center = (x, y)

    # Display the text on to the surface
    screen.blit(text_surface, text_rect)

# Here we are creating the variables which will be used to create the rectangles
p = pg.Rect(0, 0, 150, 150)
p.center = (WIDTH / 3, HEIGHT / 3)
m_r = pg.Rect(0, 0, 100, 100)
m = pg.Surface((100, 100)).convert_alpha()
col = GREEN
# msg stands for message
msg = ""

# We now have the game screen being created and run here
# This time, the loop is a little lengthier but it is because there are more things we need to be constantly updating
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # With this line, you are able to quit the game not just by clicking on the 'x' button,
        # but by also pressing 'esc' on your keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # The following variable is used in order to get the position of the mouse on the screen
    m_r.center = (pg.mouse.get_pos())

    # Here we have some comparisons happening to see whether
    # the mouse is currently inside of particular specified bounds
    in_x = m_r.left < p.right and m_r.right > p.left
    in_y = m_r.top < p.bottom and m_r.bottom > p.top

    # Now we see those boundary checking variables in live action
    # When you finish the code, run the game and come back and see if you can explain what is
    # happening between the code and the screen
    if in_x and in_y:
        # col = RED
        m.fill(RED)
        msg = "Colliding!"
    elif in_x or in_y:
        # col = CYAN
        m.fill(CYAN)
        msg = "Not colliding"
    else:
        # col = GREEN
        m.fill(GREEN)
        msg = "Not colliding"

    # All of the following lines of code are used for creating the screen that we are using
    screen.fill(DARKGRAY)
    pg.draw.line(screen, LIGHTGRAY, (p.left, p.bottom + 5), (p.left, HEIGHT), 2)
    pg.draw.line(screen, LIGHTGRAY, (p.right, p.bottom + 5), (p.right, HEIGHT), 2)
    pg.draw.line(screen, LIGHTGRAY, (p.right + 5, p.top), (WIDTH, p.top), 2)
    pg.draw.line(screen, LIGHTGRAY, (p.right + 5, p.bottom), (WIDTH, p.bottom), 2)
    pg.draw.rect(screen, YELLOW, p)

    "The following line was created by the original author but I don't think we need it so you can erase it or test it"
    # pg.draw.rect(screen, col, m)

    "These lines have to do with thing I mentioned about the function. Maybe I do need them but could you please check?"
    screen.blit(m, m_r)
    draw_text(msg, 22, WHITE, 15, 15)
    draw_text("left", 18, WHITE, p.left - 5, HEIGHT - 5, align="se")
    draw_text("right", 18, WHITE, p.right + 5, HEIGHT - 5, align="sw")
    draw_text("top", 18, WHITE, WIDTH - 5, p.top - 5, align="se")
    draw_text("bottom", 18, WHITE, WIDTH - 5, p.bottom + 5, align="ne")
    draw_text(str(m_r), 20, col, WIDTH / 2, 15, align="nw")
    pg.display.flip()
