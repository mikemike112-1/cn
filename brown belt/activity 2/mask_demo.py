# quick demo to help explain masks and pixel perfect collisions
import pygame as pg

# Define the screen size dimensions that will be used
WIDTH = 480
HEIGHT = 480
FPS = 60

# Define the color variables that will be used during the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# Initialize pygame here and create the game window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# This function will be used for adding text onto the screen
# It takes 4 different parameters: text, size, color, x, y
def draw_text(text, size, color, x, y):

    # This variable is choosing the font style that will be used
    font_name = pg.font.match_font('arial')
    # This variable is setting the font to the style we just chose and the size we passed in as a parameter
    font = pg.font.Font(font_name, size)
    # This line here creates the font onto the screen for us to be able to see
    text_surface = font.render(text, True, color)

    # Here, we are going to be making a rectangle
    text_rect = text_surface.get_rect()
    # Now we are choosing where on the screen the rectangle will be placed
    text_rect.midtop = (x, y)
    # This is a line we have used in the past to display the rectangle on the screen
    screen.blit(text_surface, text_rect)

# These variables will be used for creating variables for the image files that we will soon add into our game
ship_image = pg.image.load('playerShip1_orange.png').convert_alpha()

# This line is resizing the size of the ship_image variable
ship_image = pg.transform.scale(ship_image, (200, 76 * 2))

# Now we continue adding more image variables into the code
bunny_image = pg.image.load('bunny1_ready.png').convert_alpha()
enemy_image = pg.image.load('flyMan_fly.png').convert_alpha()

# This is the start of the class for our Player class
# The parameter being passed in is the player which will have its properties properly updated
class Player(pg.sprite.Sprite):

    # This function will set up the player object and define some important properties we will be using
    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image

        """
        The following line was commented by the original authors
        You are free to disregard it as it does not directly affect anything in the activity 
        It deals with transparency and more info can be found on the pygame website 
        """
        # self.image.set_colorkey(BLACK)

        # Set up a rectangle to be used
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

# Here we are setting up the players in the game and adding them to their respective groups
all_sprites = pg.sprite.Group()
p1 = Player(bunny_image)
all_sprites.add(p1)
p2 = Player(enemy_image)
all_sprites.add(p2)
p2.rect.x -= 125
p2.rect.y -= 125

# This function is used to fill the sprite's mask
def draw_mask(sprite):
    for x in range(sprite.rect.width):
        for y in range(sprite.rect.height):
            if sprite.mask.get_at((x, y)):
                pg.draw.circle(sprite.image, MAGENTA, (x, y), 1)

# This function draws the circle which goes around the sprites outline
def draw_outline(sprite):
    # outline the sprite's mask
    o = sprite.mask.outline()
    for px in o:
        pg.draw.circle(sprite.image, MAGENTA, px, 2)

# This is the setup for the loop which will be running and updating the game once it starts
running = True
outline_on = False
fill_on = False
pg.key.set_repeat(200, 50)

# Here is the while loop for the game running
while running:
    clock.tick(FPS)

    # The following for loop checks what key has been pressed and updates the game screen with the right positions
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                p2.rect.x -= 1
            if event.key == pg.K_RIGHT:
                p2.rect.x += 1
            if event.key == pg.K_UP:
                p2.rect.y -= 1
            if event.key == pg.K_DOWN:
                p2.rect.y += 1
            if event.key == pg.K_m:
                fill_on = not fill_on
                outline_on = False
            if event.key == pg.K_o:
                outline_on = not outline_on
                fill_on = False

    # Update the sprites on the screen
    all_sprites.update()

    # Check if the two sprites have collided
    h = pg.sprite.collide_mask(p1, p2)

    # If there is collision then draw on the screen with the appropriate circles
    if outline_on:
        draw_outline(p2)
        draw_outline(p1)
    elif fill_on:
        draw_mask(p2)
        draw_mask(p1)
    elif not outline_on and not fill_on:
        p1.image = bunny_image.copy()
        p2.image = enemy_image.copy()

    """
    The following commented code was commented out by the original authors
    I'm not sure what it does but I don't think it is needed  
    """
    # h = p1.mask.overlap_area(p2.mask, (p1.rect.x-p2.rect.x, p1.rect.y-p2.rect.y))
    # pg.display.set_caption(str(h))

    # Create and display the remaining objects and shapes needed onto the screen
    # Grab your sensei and see if you can explain to them what each of the next lines do
    screen.fill((40, 40, 40))
    screen.blit(p1.image, p1.rect)
    pg.draw.rect(screen, WHITE, p1.rect, 1)
    pg.draw.rect(screen, WHITE, p2.rect, 1)
    screen.blit(p2.image, p2.rect)

    # Lastly, here is where our text is displayed and updated
    draw_text("Hit: " + str(h), 18, WHITE, WIDTH / 2, 5)
    if h:
        px = (h[0] + p1.rect.x, h[1] + p1.rect.y)
        pg.draw.circle(screen, CYAN, px, 4)
    pg.display.flip()

pg.quit()
