
from pygame import sprite

class Cursor( sprite.Sprite ):

  def __init__(self):

    sprite.Sprite.__init__(self)

    self.image = pygame.Surface((50, 50))
    self.image.fill((255, 255, 255))
    pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
    self.rect = self.image.get_rect()


  def update(self):
    self.rect.center = pygame.mouse.get_pos()
