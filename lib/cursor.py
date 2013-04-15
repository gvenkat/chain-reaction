
from pygame import sprite
import pygame

class Cursor( sprite.Sprite ):

  def __init__(self):

    sprite.Sprite.__init__(self)

    self.image = pygame.Surface((50, 50))
    self.image.fill((255, 255, 255))
    pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
    self.rect = self.image.get_rect()
    self.pos = None


  def set_position( self, pos ):
    self.pos = pos

  def update( self ):
    print "I get called"
    self.rect.midtop = self.pos



