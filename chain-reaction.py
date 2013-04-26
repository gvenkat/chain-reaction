
import sys
import pygame
import time

sys.path.insert( 0, 'lib' )

from pygame.locals import *

import grid
import menu
import game

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

# game
_game = game.Game( screen )

# set ticks
clock = pygame.time.Clock()

pygame.display.flip()



# deal with the game
while True:

  clock.tick( 30 )

  for event in pygame.event.get( [ QUIT, KEYDOWN ] ):
    if event.type == QUIT:
      raise SystemExit

    elif not game.Game.started:
      what = _menu.handle_event( event )

      if what == 'Start':
        # redraw the grid
        screen.fill( BACKGROUND_COLOR )
        grid.Grid( screen ).draw()
        _game.start()

      elif what == 'Quit':
        raise SystemExit

      elif what == 'Help':
        pass

    elif game.Game.started:
      _game.handle_event( event )


  if game.Game.started:
    _game.update()


  pygame.display.flip()
