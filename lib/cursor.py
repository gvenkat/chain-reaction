
from pygame import sprite
import pygame

class Cursor( sprite.Sprite ):

  def __init__(self, color, radius):

    sprite.Sprite.__init__(self)

    # use transparent image
    image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA, 32)
    self.image = image.convert_alpha()

    pygame.draw.circle(self.image, (0, 0, 255), (0,0), radius, 0)
    self.rect = self.image.get_rect()
    self.pos = None


  def set_position( self, pos ):
    self.pos = pos

  def update( self ):
    print "I get called"
    self.rect.midtop = self.pos



