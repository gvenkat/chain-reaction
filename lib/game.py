import gamelevel
import ball
import pygame
import grid

from pygame.locals import *

from pygame.sprite import Group


class Game( object ):

  started     = False
  game_level  = 0

  def __init__( self, screen ):
    self.surface = screen
    self.reset_game_level( 0 )
    self.stopped_balls = 0


  def reset_game_level( self, level ):
    Game.game_level = level


  def finished_all_levels( self ):
    return Game.game_level >= max( [ int( i ) for i in gamelevel.levels.keys() ] )


  def failed_level( self ):
    return self.stopped_balls < gamelevel.levels[ str( Game.game_level ) ][ 'stopped_balls' ]


  def start( self ):

    Game.started = True

    level       = gamelevel.levels[ str( Game.game_level ) ]
    xmax, ymax  = self.surface.get_size()
    self.stopped_balls = 0

    # Starter ball
    starter = ball.StarterBall( 30, pygame.Color( 255, 0, 0 ) )
    starter_group = Group( starter )
    starter_group.draw( self.surface )

    # All balls
    sprites = [
      ball.GameBall( i, level[ 'ball_size' ], level[ 'ball_speed' ] , level[ 'expanded_ball_size' ], xmax, ymax )
        for i in range( level[ 'number_of_balls' ] )
    ]

    # Group
    group  = Group( sprites )

    # Draw
    group.draw( self.surface )

    # Set instance variables
    self.sprites, self.group, self.starter, self.starter_group = sprites, group, starter, starter_group


    # blank stuff
    self.blank = pygame.Surface(( level[ 'ball_size'] * 2 , level[ 'ball_size' ] * 2) )
    self.blank = self.blank.convert_alpha()


  def update( self ):

    if self.starter.placed:

      for ball in self.sprites:
        # with the starter ball
        if ball.rect.colliderect( self.starter.rect ) and not ball.stopped and not self.starter.remove:
          print "collides with the start ball"
          print "ball:", ball.rect
          print "starter:", self.starter.rect
          ball.stop()
          ball.expand()
          self.stopped_balls += 1

        if ball.stopped:
          for other_ball in self.sprites:
            if ( not other_ball is ball ) and ( not other_ball.stopped ) and not ball.remove and other_ball.rect.colliderect( ball.rect ):
              other_ball.stop()
              other_ball.expand()
              self.stopped_balls += 1


    if self.starter.remove:
      self.starter_group.remove( self.starter )


    for ball in self.sprites:
      if ball.remove:
        self.group.remove( ball )


    self.group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )
    self.starter_group.clear( self.surface, lambda s,r: s.blit( self.blank, r ) )

    self.surface.fill( pygame.Color( 233, 233, 233 ) )

    grid.Grid( self.surface ).draw()

    self.group.update()
    self.starter_group.update()

    self.starter_group.draw( self.surface )
    self.group.draw( self.surface )


  def has_ended( self ):
    return self.starter.remove and all( [ i.remove for i in self.sprites if i.stopped ] )


  def handle_event( self, event ):

    if event.type == MOUSEMOTION:
      x, y = pygame.mouse.get_pos()
      self.starter_group.update( x, y )

    if event.type == MOUSEBUTTONDOWN:
      self.starter.set_placed()




