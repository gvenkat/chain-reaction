import gamelevel
import ball
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


  def handle_event( self, event ):
    print "About to handle game event"



