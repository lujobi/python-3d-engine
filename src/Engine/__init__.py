import pygame
from .View.Color.colors import StaticColor
from .View.Camera.camera import Camera
from .Objects.ground_plane import GroundPlane
from .Objects.sphere import Sphere

import numpy as np

class Engine:
  def __init__(self, width, height):
    self.pos = (0,0)
    self.camera = Camera((width, height), [0,-4,4], [0, 0, 0], 1)
    self.objects = [Sphere([0, 2, 0], 2), GroundPlane()]

  def render(self, screen):
    #screen.fill(StaticColor.WHITE)
    width, height  = screen.get_size()

    pixels = self.camera.dispatch_rays(self.objects)
    # pixels = np.full((width, height, 3), 255)
    surf = pygame.surfarray.make_surface(pixels)
    screen.blit(surf, (0, 0))

    #pygame.draw.circle(screen, StaticColor.BLACK, self.pos, 3)
    pygame.display.flip()

  def tick(self, stop, events, tick):
    pass
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
  
