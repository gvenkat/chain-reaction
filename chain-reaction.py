
import sys
import pygame
import time

sys.path.insert( 0, 'lib' )

from pygame.locals import *

import grid
import menu

# constants
WIDTH = 800
HEIGHT = 600
DRAW_GRIDS = True
BACKGROUND_COLOR = Color( 233, 233, 233 )
FOREGROUND_COLOR = None
GRID_COLOR = None

# initialize
pygame.init()

# start display
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ), HWSURFACE | DOUBLEBUF )

# background
screen.fill( BACKGROUND_COLOR )

# Draw the grid
grid.Grid( screen ).draw()

# Initial menu
_menu = menu.Menu( screen, [ 'Start', 'Help', 'Quit' ], font_size=30 )
_menu.draw()

pygame.display.flip()

# deal with the game
while True:

  for event in pygame.event.get():
    if event.type == QUIT:
      raise SystemExit

  pygame.display.flip()


  time.sleep( 1 )
