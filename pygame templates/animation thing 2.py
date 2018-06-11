''' Basic PyGame Starting Template '''
# import your modules here
import pygame
from pygame.locals import *
import random
# enable pygame here
pygame.init()

''' Define Your Default Project Properties and Variables '''
# define game window label / string that is displayed in the window title
gameWindow_label = "Animation"
# define size of the game window surface / width and height in pixels
gameWindow_width = 640
gameWindow_height = 480
''' misc variables objects classes and properties '''
# colors for example
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
dootX = 0
dootY = 16
clock = pygame.time.Clock()

#other surfaces
mysquare = pygame.Surface((1,32))

''' Create The Game Window '''
# define the game window surface
gameWindow_surface = pygame.display.set_mode((gameWindow_width,gameWindow_height))
# set the window title
pygame.display.set_caption(gameWindow_label)

gameWindow_surface.fill(gray)

''' Create Runtime Event Loop / The main program loop '''
# define eventLoop as True
eventLoop = True
# enter the main program event loop. (Run the program while eventLoop is True)
while eventLoop:
    # look at each event as they are returned by pygame
    for event in pygame.event.get():
        # [Optional] print out each event to the command prompt or shell.
        #print(event)
        
        # check if the QUIT event is returned
        if event.type == pygame.QUIT:
            # break out of the main program loop. (procede to the quit commands at the end of the script)
            eventLoop = False
            
        #Check for keyboard input events and other misc events here using elif
        #elif
            
    ''' Inside the main event loop'''
    # Clear Screen
    #gameWindow_surface.fill(gray)
    mysquare = pygame.Surface((1,random.randrange(8,32)))
    mysquare.fill(random.choice([black,white,gray]))
    gameWindow_surface.blit(mysquare,(dootX,dootY))
    # Do your game stuff here
    # Render Frame
    #clock.tick(120)
    pygame.display.update()
    if dootX < gameWindow_width:
        dootX += 1
    else:
        dootX = 0
        dootY += 64
    if dootY > gameWindow_height:
        dootY = random.randrange(-32,0)
        dootX = 0


''' The End Of The Script '''
# terminate pygame process, then terminate python process. A proper clean exit.
pygame.quit()
quit()
