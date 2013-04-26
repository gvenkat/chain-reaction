import gamelevel
import ball
import pygame
import grid

from pygame.locals import *

from pygame.sprite import Group


class Game( object ):

  started     = False
  game_level  = 0

  def __init__( self, screen ):
    self.surface = screen
    self.reset_game_level( 0 )

  def reset_game_level( self, level ):
    Game.game_level = level

  def start( self ):

    Game.started = True

    level       = gamelevel.levels[ str( Game.game_level ) ]
    xmax, ymax  = self.surface.get_size()


    # Starter ball
    starter = ball.StarterBall( 30, pygame.Color( 255, 0, 0 ) )
    starter_group = Group( starter )
    starter_group.draw( self.surface )

    # All balls
    sprites = [
      ball.GameBall( i, level[ 'ball_size' ], level[ 'ball_speed' ] , level[ 'expanded_ball_size' ], xmax, ymax )
        for i in range( level[ 'number_of_balls' ] )
    ]

    # Group
    group  = Group( sprites )

    # Draw
    group.draw( self.surface )

    # Set instance variables
    self.sprites, self.group, self.starter, self.starter_group = sprites, group, starter, starter_group


    # blank stuff
    self.blank = pygame.Surface(( level[ 'ball_size'] * 2 , level[ 'ball_size' ] * 2) )
    self.blank = self.blank.convert_alpha()

  def update( self ):
    self.group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )
    self.starter_group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )

    self.surface.fill( pygame.Color( 233, 233, 233 ) )

    grid.Grid( self.surface ).draw()

    self.group.update()
    self.starter_group.draw( self.surface )
    self.group.draw( self.surface )


  def handle_event( self, event ):
    if event.type == MOUSEMOTION:
      x, y = pygame.mouse.get_pos()
      self.starter_group.update( x, y )

    if event.type == MOUSEBUTTONDOWN:
      self.starter.set_placed()




