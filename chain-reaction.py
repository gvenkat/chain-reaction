
import sys
import pygame
import time

sys.path.insert( 0, 'lib' )

from pygame.locals import *

from gameconfig import *
import grid
import menu
import game


# initialize
pygame.init()

# start display
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ), HWSURFACE | DOUBLEBUF )

# background
screen.fill( BACKGROUND_COLOR )

# Draw the grid
grid.Grid( screen ).draw()

# Initial menu
_menu = menu.Menu( screen, [ 'Start', 'Quit' ], font_size=30 )
_menu.draw()

# game
_game = game.Game( screen )

# set ticks
clock = pygame.time.Clock()

pygame.display.flip()



# deal with the game
while True:

  clock.tick( FPS )

  for event in pygame.event.get( [ QUIT, KEYDOWN, MOUSEMOTION, MOUSEBUTTONDOWN ] ):
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


    elif game.Game.started:
      _game.handle_event( event )


  if game.Game.started:
    _game.update()


  pygame.display.flip()
