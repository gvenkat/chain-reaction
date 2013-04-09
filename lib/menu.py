
from pygame import event, font, Color, Rect, draw, display
import sys

# If its not already initialized
font.init()

class Menu( object ):

  def __init__( self, surface, items=[ ], callback=None, start_x=None, end_x=None, start_y=None, end_y=None, background=Color( 85, 85, 85, 30 ), font_name=None, font_size=12, color=Color( 255, 255, 255, 30 )  ):
    self.surface = surface
    self.items = items
    self.callback = callback
    self.start_x = start_x
    self.end_x = end_x
    self.start_y = start_y
    self.end_y = end_y
    self.background = background
    self.color = color

    if font is None:
      self.font = font.Font( None, font_size ) 
    else:
      self.font = font.SysFont( font_name, font_size )


    if self.callback is None:
      sys.stderr.write( "No callback given ... wouldn't know what to do" )

    if len( items ) == 0:
      sys.stderr.write( "No items given, what do you need the menu for?" )
      raise SystemExit

    if start_x is None or end_x is None or start_y is None or end_y is None: 

      sys.stderr.write( 
        """
          The dimensions not given properly, i'll just make it up myself, don't worry too much, 
          i'll make it look as good as i can
        """ 
      )

      width, height = surface.get_size()
      menu_width, menu_height   = ( int( width * 0.7 ), int( height * 0.7 ) )

      self.start_x  = ( width - menu_width ) / 2
      self.end_x    = self.start_x + menu_width 
      self.start_y  = ( height - menu_height ) / 2 
      self.end_y    = self.start_y + menu_height 


  def container_height( self ):
    return self.end_y - self.start_y

  def container_width( self ):
    return self.end_x - self.start_x

  def height_per_menu_item( self ):

    if len( self.items ) > 5:
      number_of_items = 5
    else:
      number_of_items = len( self.items )

    vertical_padding = 10

    return ( self.container_height() - ( 2 * vertical_padding ) ) / number_of_items


  def yposition_for_item( self, item ):
    return item * self.height_per_menu_item()


  def draw_container( self ):
    draw.rect( self.surface, self.background, Rect( ( self.start_x, self.start_y ), ( self.container_width(), self.container_height() ) ) )


  def draw_items( self ):
    # FIXME: Shows only 5 items

    horizontal_padding = 10
    for index, item in ennumerate( self.items.slice( 0, 5 ) ):
      text = self.font.render( str( index ) + '. ' + str( item ), True, self.color )
      rect = text.get_rect().move( self.start_x + horizontal_padding, self.yposition_for_item( index ) )
      surface.blit( text, rect )
      pygame.display.update( rect )


  def draw( self ):
    self.draw_container()
    self.draw_items()









    





    


