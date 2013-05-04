
import sys
import pygame
import time

sys.path.insert( 0, 'lib' )

from pygame.locals import *

from gameconfig import *
import grid
import menu
import game


pygame.init()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ), HWSURFACE | DOUBLEBUF )

screen.fill( BACKGROUND_COLOR )

grid.Grid( screen ).draw()

_menu = menu.Menu( screen, [ 'Start', 'Quit' ], font_size=30 )
_menu.draw()

_game = game.Game( screen )

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

    if _game.has_ended():
      print "The game has ended"





  pygame.display.flip()
