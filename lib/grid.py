
from pygame import draw, Color

class Grid( object ):

  def __init__( self, surface, grid_lines=10, color=Color( 254, 254, 254 ) ): 
    self.surface = surface 
    self.color = color
    self.grid_lines = grid_lines


  def draw( self ):
    width, height = self.surface.get_size()
    
    # vertical lines
    for i in range( int( width / self.grid_lines ) ):
      draw.line( self.surface, self.color, ( i, 0 ), ( i, height ), 1 )

    # horizontal lines
    for j in range( int( height / self.grid_lines ) ):
      draw.line( self.surface, self.color, ( 0, j ), ( width, j ), 1 )







