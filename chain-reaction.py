
import sys
import pygame
import time
from pygame.locals import *

sys.path.insert( 0, 'lib' )


# constants
WIDTH = 800
HEIGHT = 600
DRAW_GRIDS = True
BACKGROUND_COLOR = None
FOREGROUND_COLOR = None
GRID_COLOR = None

# initialize
pygame.init()

# start display
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ), HWSURFACE | DOUBLEBUF )

# deal with the game
while True:
  time.sleep( 10 )
