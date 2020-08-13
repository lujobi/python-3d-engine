import pygame
from .View.Color.colors import StaticColor
from .View.Camera.camera import Camera
from .Objects.ground_plane import GroundPlane
from .Objects.sphere import Sphere

import numpy as np
from src.utils.timer import timeit

class Engine:
  def __init__(self, width, height):
    self.pos = (0,0)
    h = 1
    r = 2
    self.camera = Camera((width, height), [0,-6,0.2], [0, 0, 0], 1)
    self.objects = [GroundPlane()] #[Sphere([-r*1.01, 0, h], r), Sphere([r, 0, h], r), GroundPlane()]

  @timeit
  def render(self, screen):
    #screen.fill(StaticColor.WHITE)
    width, height  = screen.get_size()

    pixels = self.camera.dispatch_rays(self.objects)
    #for i in range(2, 4):
    #  pixels = self.camera.dispatch_rays(self.objects)
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
  
