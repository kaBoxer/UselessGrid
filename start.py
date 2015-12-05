"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import mapping
from globals import *
from myObjects import *

# Initialize pygame
pygame.init()
pygame.key.set_repeat(100, 100)

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)

#hide mouse cursor
pygame.mouse.set_visible(True)

#have to do this down here because it has some code that requires a pygame screen to be created.
import drawing
import maps

# Set title of screen
pygame.display.set_caption("pyTactics")
 
# Loop until the user clicks the close button.
Running = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Handle Events
def Events_UpdateGrid():  # Note, this is big_Grid
    #GLOBALS
    global Running
    global TOP_LEFT
    #GLOBALS
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            Running = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            # Key Events which are system related, like exit will happen here, others specific to the game
            # will happen as part of the object?
            if event.key == pygame.K_ESCAPE:
                Running = False

        elif event.type == pygame.MOUSEMOTION:
            CursorTiles.empty()
            Cursor()


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse.
            #keys they press
            keys = pygame.key.get_pressed()

            # Get the position of the mouse
            pos = pygame.mouse.get_pos()

            #1234567890 - Emma 12/2/15
            #collision for cursor and a sprite:

            for cur in CursorTiles:
                for spr in AllSprites:
                    if cur.rect.colliderect(spr.rect):
                        spr.select()
                    else:
                        spr.selected = False

#Todo: How to get grid cords for an arbitrary x/y?
#-?


# -------- Main Program Loop -----------
while Running:
    # Handle Events
    Events_UpdateGrid()

    # Draw Everything
    screen.fill((20, 30, 40)) # color of non-tiles. ie background.
    AllTiles.update(screen)
    AllSprites.update(screen)
    CursorTiles.update(screen)
    print "Tiles: %s \t Sprites: %s \t Cursors: %s" % (len(AllTiles), len(AllSprites), len(CursorTiles))
    screen.blit(write(str(pygame.mouse.get_pos())), (200, 475)) #Mouse Cords

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

#print
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
