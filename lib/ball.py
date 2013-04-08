
import math
import random

class Ball( object ):

  def __initialize__( self, x=0, y=0, color=None ):
    self.x = x
    self.y = y
    self.color = color or self.get_random_color()
    self.radius = 0
    self.disabled = False


  def get_random_color( self ):
    pass


  def draw( self ):
    pass





class GameBall( Ball ):

  def __initialize__( self, x, y ):
    super( self ).__initalize( x, y )
    self.downspeed = 0
    self.rightspeed = 0

  def move( self ):
    pass

  def start_expansion( self ):
    pass

  def expand( self ):
    pass

  def shrink( self ):
    pass

  def maintain( self ):
    pass

  def draw( self ):
    pass



class StarterBall( Ball ):

  def __initialize__( self, x, y ):
    super( self ).__initialize__( x, y )


  def check_bounds( self ):
    pass

  def move( self ):
    pass

  def place( self ):
    pass

