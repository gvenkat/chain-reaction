import gamelevel
import ball
import pygame
import grid

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

    sprites = [
      ball.GameBall( i, level[ 'ball_size' ], level[ 'ball_speed' ] , level[ 'expanded_ball_size' ], xmax, ymax )
        for i in range( level[ 'number_of_balls' ] )
    ]

    group  = Group( sprites )

    group.draw( self.surface )

    self.sprites, self.group = sprites, group

    self.blank = pygame.Surface(( level[ 'ball_size'] * 2 , level[ 'ball_size' ] * 2) )
    self.blank = self.blank.convert_alpha()

  def update( self ):
    self.group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )
    self.surface.fill( pygame.Color( 233, 233, 233 ) )

    grid.Grid( self.surface ).draw()
    self.group.update()
    self.group.draw( self.surface )


  def handle_event( self, event ):
    print "About to handle game event"



