
import sys
import pygame
import time

sys.path.insert( 0, 'lib' )


# constants
WIDTH = 500
HEIGHT = 500
DRAW_GRIDS = True
BACKGROUND_COLOR = None
FOREGROUND_COLOR = None
GRID_COLOR = None

# initialize
pygame.init()

# start display
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )

# deal with the game
while True:
  time.sleep( 1 )
