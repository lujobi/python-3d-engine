import pygame
from .View.Color.colors import StaticColor

class Engine:
  def __init__(self):
    self.pos = (0,0)

  def render(self, screen):
    screen.fill(StaticColor.WHITE)
    width, height  = screen.get_size()

    pygame.draw.circle(screen, StaticColor.BLACK, self.pos, 3)
    pygame.display.flip()


  def tick(self, stop, events, tick):
    self.pos = (tick*200%1000, int(tick*200/1000))

    for event in events:
      if event.type == pygame.QUIT:
        stop()
        return
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_q]:
        stop()
        return

    return True
  
