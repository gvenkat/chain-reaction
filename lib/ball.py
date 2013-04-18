
import math
import random
from pygame import sprite


class GameBall( sprite.Sprite ):

  def __init__( self, number, ball_size, expanded_size, xmax, ymax ):

    sprite.Sprite.__init__(self)
    self.color = self.get_random_color()
    self.number = number
    self.ball_size = ball_size
    self.expanded_size = expanded_size


  def get_random_color( self ):
    pass

  def set_start_position( self ):
    pass

  def update( self ):
    pass








