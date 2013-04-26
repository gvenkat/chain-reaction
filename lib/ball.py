
import math
import random
import pygame
from pygame import sprite, Color


class GameBall( sprite.Sprite ):

  def __init__( self, number, ball_size, ball_speed, expanded_size, xmax, ymax ):

    sprite.Sprite.__init__(self)
    self.color = self.get_random_color()
    self.number = number
    self.ball_size = ball_size
    self.expanded_size = expanded_size
    self.ball_speed = ball_speed
    self.xmax = xmax
    self.ymax = ymax

    self.direction = 20 + ( random.random() * 340 )

    self.downspeed = math.cos( self.direction ) * self.ball_speed
    self.rightspeed = math.sin( self.direction ) * self.ball_speed

    self.x = ( self.xmax - 2 * self.ball_size ) * random.random() + self.ball_size
    self.y = ( self.ymax - 2 * self.ball_size ) * random.random() + self.ball_size

    image = pygame.Surface((ball_size*2, ball_size*2), pygame.SRCALPHA, 32)
    self.image = image.convert_alpha()

    pygame.draw.circle(self.image, self.color, (ball_size,ball_size), ball_size, 0)

    self.rect = self.image.get_rect()
    self.rect.midtop = ( self.x, self.y )



  def get_random_color( self ):
    return Color( random.randrange( 0, 256 ), random.randrange( 0, 256 ), random.randrange( 0, 256 ), 100 )

  def update( self ):
    self.x += self.rightspeed
    self.y += self.downspeed

    if  ( self.x + self.ball_size ) > self.xmax or ( self.x - self.ball_size ) < 0:
      self.rightspeed = -1 * self.rightspeed

    if ( self.y + self.ball_size * 2 ) > self.ymax or self.y  < 0:
      self.downspeed = -1 * self.downspeed



    self.rect.midtop = ( self.x, self.y )

