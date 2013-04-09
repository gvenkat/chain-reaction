
from pygame import draw, Color

class Grid( object ):

  def __init__( self, surface, grid_lines=10, color=Color( 254, 254, 254 ) ): 
    self.surface = surface 
    self.color = color
    self.grid_lines = grid_lines


  def draw( self ):
    width, height = self.surface.get_size()
    
    # vertical lines
    vertical_line_spacing = width / self.grid_lines
    for i in range( self.grid_lines ): 
      draw.line( self.surface, self.color, ( i * vertical_line_spacing, 0 ), ( i * vertical_line_spacing, height ), 1 )

    # horizontal lines
    horizontal_line_spacing = int( height / self.grid_lines )
    for j in range( self.grid_lines ): 
      draw.line( self.surface, self.color, ( 0, j * horizontal_line_spacing ), ( width, j * horizontal_line_spacing ), 1 )







