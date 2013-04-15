
from pygame import event, font, Color, Rect, draw, display, constants, Surface, sprite
import pygame
import cursor

import sys

# If its not already initialized
font.init()

def eraseSprite(screen, rect):
   screen.blit(blank, rect)


class Menu( object ):

  def __init__( self,
                surface,
                items=[ ],
                callback=None,
                start_x=None,
                end_x=None,
                start_y=None,
                end_y=None,
                background=Color( 85, 85, 85, 30 ),
                font_name=None,
                font_size=12,
                color=Color( 255, 255, 255, 30 ),
                cursor_color=Color( 224, 27, 106, 30 ),
                cursor_radius=10
              ):

    self.surface = surface
    self.items = items
    self.callback = callback
    self.start_x = start_x
    self.end_x = end_x
    self.start_y = start_y
    self.end_y = end_y
    self.background = background
    self.color = color
    self.font_size = font_size
    self.menu_items = [ ]
    self.cursor_color = cursor_color
    self.cursor_radius = cursor_radius
    self.cursor_position = 0

    self.blank = pygame.Surface((cursor_radius, cursor_radius))
    self.blank.fill((255, 255, 255))

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

    padding_top = 20

    return ( padding_top + self.start_y +
      ( item * self.height_per_menu_item() ) +
      ( ( self.height_per_menu_item() - self.font_size ) / 2 ) )


  def draw_container( self ):
    draw.rect( self.surface, self.background, Rect( ( self.start_x, self.start_y ), ( self.container_width(), self.container_height() ) ) )


  def get_horizontal_padding( self ):
    return 250


  def draw_items( self ):
    horizontal_padding = 500
    for index, item in enumerate( self.items[0:5] ):
      text = self.font.render( str( index + 1 ) + '. ' + str( item ), True, self.color )
      rect = text.get_rect().move( self.start_x + self.get_horizontal_padding(), self.yposition_for_item( index ) )

      # keep a copy
      self.menu_items.append( ( text, rect ) )

      self.surface.blit( text, rect )
      display.update( rect )


  def cursor_x_position( self ):
    return self.start_x + 200

  def cursor_y_position( self ):
    return self.yposition_for_item( self.cursor_position ) + 5

  def draw_cursor( self ):
    # Create and draw
    self.cursor = cursor.Cursor()
    self.cursor_group = sprite.Group( ( self.cursor ) )
    # self.cursor_group.draw( self.surface )

    self.update_cursor_position()


  def setup_highlighted_text( self ):
    pass

  def goto( self, to_index ):

    if to_index > len( self.items ) - 1:
      self.cursor_position = 0
    elif to_index < 0:
      self.cursor_position = len( items ) - 1
    else:
      self.cursor_position = to_index

    self.update_cursor_position()

  def update_cursor_position( self ):
    self.cursor.set_position( ( self.cursor_x_position(), self.cursor_y_position() ) )
    self.cursor_group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )

    self.cursor_group.update()
    self.cursor_group.draw( self.surface )



  def handle_event( self, event ):
    if event.type == constants.KEYDOWN:
      if event.key in [ getattr( constants, 'K_' + str( i + 1 ) ) for i,j in enumerate( self.items ) ]:
        print "right key"
      elif event.key == constants.K_DOWN:
        self.goto( self.cursor_position + 1 )
      elif event.key == constants.K_UP:
        self.goto( self.cursor_position - 1 )
      else:
        print "whatever else"


  def draw( self ):
    self.draw_container()
    self.draw_items()
    self.draw_cursor()
    self.setup_highlighted_text()


















