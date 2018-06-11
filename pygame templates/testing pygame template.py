''' Basic PyGame Starting Template '''
# import your modules here
import pygame
from pygame.locals import *
# enable pygame here
pygame.init()

''' Define Your Default Project Properties and Variables '''
# define game window label / string that is displayed in the window title
gameWindow_label = "The Name of My Game Goes Here"
# define size of the game window surface / width and height in pixels
gameWindow_width = 640
gameWindow_height = 480
''' misc variables objects classes and properties '''
# colors for example
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

''' Create The Game Window '''
# define the game window surface
gameWindow_surface = pygame.display.set_mode((gameWindow_width,gameWindow_height))
# set the window title
pygame.display.set_caption(gameWindow_label)

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
    gameWindow_surface.fill(gray)
    # Do your game stuff here
    # Render Frame
    pygame.display.update()

''' The End Of The Script '''
# terminate pygame process, then terminate python process. A proper clean exit.
pygame.quit()
quit()
