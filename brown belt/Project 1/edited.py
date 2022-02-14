import pygame
 
# Define some colors to use later
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Here we are going to initialize pygame
pygame.init()

# Here, we will use a varibale to set the width and height of the screen [width, height]
size = (700, 500)

# Here we have a variable that will be used later on for creating the game display itself
# Notice that we have passed in the size variable we previously made
# If we needed to change the size of the screen now, we would do so by modifying the size variable
screen = pygame.display.set_mode(size)

# Now we are going to create our first class for this game
# This class Ball will be used for making a ball along with defining the balls behaviors and features
class Ball(object):

    # This __init__ function is used to define what our initial values are
    # Let's take some time to go through each of these and describe the purpose for each one
    def __init__ (self, screen, radius,x,y):

        # Before we dive into the different properties of this class which we are initializing, let's make sure
        # that we know what the word 'self' is being used for
        # 'self' is a term used when defining or referring to a property that is inside of and belongs to a
        # particular class
        # the underscores (_) that you see are used here to simply help you remember that these properties are only
        # able available to be used when you are inside of the correct class
        # you cannot access them outside of the class and change them directly, you have to do some more work to get
        # that completed.

        # __screen will be used to replace the screen variable from above
        self.__screen = screen

        # _radius will be used to replace the screen variable from above
        self._radius = radius

        # _xLoc will be used to replace the screen variable from above
        self._xLoc = x

        # _yLoc will be used to replace the screen variable from above
        self._yLoc = y

        # __xVel and yVel are used to define the velocity of the ball
        # if you do not know what velocity means, in its simples definition it means rate of change and direction
        # for us, we will simplify it even more and call it the speed and direction

        # __xVel will be used for the x velocity
        self.__xVel = 5

        # __yVel will be used for the y directions velocity
        # the minus sign indicates the direction that the ball will be moving
        self.__yVel = -3

        # the following will be used for getting the width and height of the game by using the get_size() function
        w,h = pygame.display.get_surface().get_size()

        # here we are setting the width and height of the class to the already used width and height
        self.__width = w
        self.__height = h

    # this function will draw a ball onto the screen
    # by passing in the 'self' it allows us to pass the entire set of properties into this function and allows
    # us to be able to use them as well
    def draw(self):
        pygame.draw.circle(screen,(255, 0, 0) , (self._xLoc,self._yLoc), self._radius)

    # the purpose of this function is to update the position of the ball on the screen and
    # also checks if the ball has hit a wall and if so, turns the ball around
    def update(self, paddle, brickwall):

        # look through this logic and see if you can determine some parts of it on your own
        # remember, if you need hints look above to see if you can determine what the variables mean and how they work
        # do not worry if you don't understand much or any of it
        self._xLoc += self.__xVel
        self._yLoc += self.__yVel
        if self._xLoc == self._radius:
            self.__xVel *= -1
        elif self._xLoc >= self.__width - self._radius:
            self.__xVel *= -1
        if self._yLoc == self._radius:
            self.__yVel *= -1
        elif self._yLoc >= self.__height - self._radius:
            return True

        # this if statement uses a collide function being called that we have not yet created
        # you will see it soon a little later in the code
        if brickwall.collide(self):
            # basically if this if statement is true, then it will change the velocity to go the opposite which is
            # why the yVel (the up and down velocity) is being flipped to go the opposite direction
            self.__yVel *= -1

        # these variables will be used to replace and simplify some of the more complicated variables from earlier
        # these will be quite helpful in checking whether the ball and paddle have collided with each other
        paddleX = paddle._xLoc
        paddleY = paddle._yLoc
        paddleW = paddle._width
        paddleH = paddle._height
        ballX = self._xLoc
        ballY = self._yLoc

        # this very long if statement check if the ball has managed to hit the paddle
        # the '\' you see at the end of the first line simply says that the if statement is continued
        # on the second line
        # the word 'and' is the same thing as saying && in JavaScript
        if ((ballX + self._radius) >= paddleX and ballX <= (paddleX + paddleW)) \
        and ((ballY + self._radius) >= paddleY and ballY <= (paddleY + paddleH)):
            self.__yVel *= -1

        # WHY IS THIS RETURNING FALSE?
        return False
        
# this class will be used for creating a paddle and defining the properties and behaviors of the paddle
class Paddle (object):

    # this __init__ does the same as the one above by defining all the variables we will be using inside this class
    def __init__ (self, screen, width, height,x,y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w = pygame.display.get_surface().get_size()
        h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h

    # this function draws the paddle onto the screen
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), (self._xLoc,self._yLoc,self._width,self._height),0)

    # this update function is used to update the position of the paddle on the screen
    def update(self):

        # here we are going to start simplifying some of the variables that you make by putting them in the same line
        # by placing x and y next to each other we are saying that the x and y variables are supposed to be equal to
        # the same thing
        x,y = pygame.mouse.get_pos()

        # this if statement is the one asking whether the mouse and paddle are at the same place
        #  if they are not then the paddle moves its x position to the same one for the mouse
        if x >= 0 and x <= (self.__W - self._width):
            self._xLoc = x
 
# this class is used for creating the bricks and defining their behaviors
class Brick (pygame.sprite.Sprite):

    # this __init__ function does the prior __init__'s
    # look above if you need a reminder as to what the job of it is
    def __init__(self, screen, width, height, x,y):
        self.__screen = screen
        self._width = width
        self._height = height
        self._xLoc = x
        self._yLoc = y
        w, h = pygame.display.get_surface().get_size()
        self.__W = w
        self.__H = h
        self.__isInGroup = False

    # this function draws a brick
    # notice how the color is in as an RGB value, (56, 177, 237)
    def draw(self):
        pygame.draw.rect(screen, (56, 177, 237), (self._xLoc,self._yLoc,self._width,self._height),0)

    # the bricks will be inside of a group and that group will be passed in to help keep track of them and
    # their properties
    def add (self, group):
        # this line adds a brick to a group
        group.add(self)
        # this line changes the flag indicating whether the brick is currently in a group or not
        self.__isInGroup = True

    # this will remove the brick from a group
    def remove(self, group):
        group.remove(self)
        self.__isInGroup = False

    # if the brick is in a group then it is still alive and on the screen
    def alive(self):
        # this will return true if it is in a group and false if it is not
        return self.__isInGroup

    # some more collision detection, this time it is for the ball and the bricks
    def collide(self, ball):
        brickX = self._xLoc
        brickY = self._yLoc
        brickW = self._width
        brickH = self._height
        ballX = ball._xLoc
        ballY = ball._yLoc
        radius = ball._radius

        # this if statement checks if the ball and brick have touched each other, if so then it will return true
        if ((ballX + radius) >= brickX and ballX <= (brickX + brickW)) \
        and ((ballY + radius) >= brickY and ballY <= (brickY + brickH)):
            return True

        return False

# this class will create a brick wall
class BrickWall (pygame.sprite.Group):

    # another __init__ this time it is for the brick wall
    def __init__ (self,screen, x, y, width, height):
        self.__screen = screen
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        # this line is one you may not have seen before
        # the [] represent an empty arry
        # arrays in python are mostly the same as arrays in JavaScript
        # since you have multiple bricks, having an array helps to keep track of them
        self._bricks = []

        X = x
        Y = y

        # this is a for loop that is going to make a 3 by 4 wall of bricks
        # it will have 3 rows each with 4 bricks
        # take a minute and see if you can realize how this
        for i in range(3):
            for j in range(4):
                self._bricks.append(Brick(screen,width,height,X,Y))
                X += width + (width/ 7.0)
            Y += height + (height / 7.0)
            X = x

    # this function will add a brick to the BrickWall group
    def add(self,brick):
        # here, append means add
        self._bricks.append(brick)

    # this function will remove a brick from the BrickWall group
    def remove(self,brick):
        self._bricks.remove(brick)

    # this function will draw all the bricks onto the screen
    def draw(self):
        for brick in self._bricks:
            if brick != None:
                brick.draw()

    # this function will update the screen of the bricks which have been made
    def update(self, ball):
        for i in range(len(self._bricks)):
            if ((self._bricks[i] != None) and self._bricks[i].collide(ball)):
                self._bricks[i] = None
        
        # this cleans up the list of bricks of bricks that no longer exist
        for brick in self._bricks:
            if brick == None:
                self._bricks.remove(brick)

    # this checks if you have won simply by checking if all the bricks are gone
    def hasWin(self):
        return len(self._bricks) == 0

    # this function checks if the brick has been hit by the ball
    def collide (self, ball):
        for brick in self._bricks:
            if brick.collide(ball):
                return True
        return False

# The game objects ball, paddle and brick wall
ball = Ball(screen,25,350,250)
paddle = Paddle(screen,100,20,250,450)
brickWall = BrickWall(screen,25,25,150,50)

isGameOver = False # determines whether game is lose
gameStatus = True # game is still running

score = 0 # score for the game.
 
pygame.display.set_caption("Brickout-game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# for displaying text in the game 
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

# message for game over
# EDITED: I CHANGED THE FONT SIZE FROM 60 TO 50
mgGameOver = pygame.font.SysFont('Comic Sans MS', 50)

# message for winning the game.
mgWin = pygame.font.SysFont('Comic Sans MS', 60)

# message for score
mgScore = pygame.font.SysFont('Comic Sans MS', 60)

textsurfaceGameOver = mgGameOver.render('Game Over!', False, (0, 0, 0))
textsurfaceWin = mgWin.render("You win!",False,(0,0,0))
textsurfaceScore = mgScore.render("score: "+str(score),False,(0,0,0))
   
# this is the main loop that makes the game display run and all the parts update properly
while not done:
    # this loop is the ont similar to the other projects you have worked on in the past
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # fills the screen's background with the color white
    screen.fill(WHITE)

    # checks if gameStatus is true or not
    if gameStatus:

        # first draws ball for appropriate displaying the score. 
        brickWall.draw()

         # this if statement is for keeping track of the score
        if brickWall.collide(ball):
            score += 10
        # these statements here actually show the score onto the screen
        textsurfaceScore = mgScore.render("score: "+str(score),False,(0,0,0))
        screen.blit(textsurfaceScore,(300,0))

        # this will update the wall by calling the update function inside of the brickWall class we made above
        brickWall.update(ball)

        # what do these 2 lines do?
        paddle.draw()
        paddle.update()

        # if our update function for the ball returns true then the game will be set to game over
        # the 2 variables inside will be used to determine what action to take
        if ball.update(paddle, brickWall):
            isGameOver = True
            gameStatus = False

        # check if the wall has won
        if brickWall.hasWin():
            gameStatus = False

        # what does this line do?
        ball.draw()

    # when the game is not running anymore then run the code in this else statement
    else:
        # if the player loses then run the if statement code
        if isGameOver:
            screen.blit(textsurfaceGameOver,(0,0))
            textsurfaceScore = mgScore.render("score: "+str(score),False,(0,0,0))
            screen.blit(textsurfaceScore,(300,0))
        # if the player loses then run the elif code
        elif brickWall.hasWin():
            screen.blit(textsurfaceWin,(0,0))
            textsurfaceScore = mgScore.render("score: "+str(score),False,(0,0,0))
            screen.blit(textsurfaceScore,(300,0))
     
    # update the screen
    pygame.display.flip()
 
    # this will limit our frames per second to be 60
    clock.tick(60)
 
# end the game and closes the window
pygame.quit()