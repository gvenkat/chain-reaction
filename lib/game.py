import gamelevel
import ball


class Game( object ):

  started     = False
  game_level  = 0

  def __init__( self, screen ):
    self.surface = screen

  def reset_game_level( self, level ):
    Game.game_level = level

  def start( self ):
    Game.started = True
    self.reset_game_level( 0 )


  def handle_event( self, event ):
    print "About to handle game event"



