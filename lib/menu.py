
from pygame import event, font, Color
import sys

# If its not already initialized
font.init()


class Menu( object ):

  def __init__( surface, items=[ ], callback=None, start_x=None, end_x=None, start_y=None, end_y=None, background=Color( 85, 85, 85, 30 )  )
    self.surface = surface
    self.items = items
    self.callback = callback
    self.start_x = start_x
    self.end_x = end_x
    self.start_y = start_y
    self.end_y = end_y

    if self.callback is None:
      sys.stderr.print( "No callback given ... wouldn't know what to do" )

    if len( items ) == 0:
      sys.stderr.print( "No items given, what do you need the menu for?" )
      raise SystemExit

    if any( lambda x: x is None, ( start_x, end_x, start_y, end_y ) ):

      sys.stderr.print( 
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



    def run():
      pass






    





    


