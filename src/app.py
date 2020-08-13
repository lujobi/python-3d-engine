import pygame
import numpy as np
import time
import threading

from .utils.LockableData import LockableData
from .Engine import Engine

WIDTH, HEIGHT = 1000, 1000

class App:

  def __init__(self, width, height, title, requested_tps, engine):

    self.settings = LockableData(running=False, tick=0, frame_since_update=0)

    self._requested_tps = requested_tps
    self._title = title
    self.engine = engine

    pygame.init()

    self.screen = pygame.display.set_mode((width, height))
    
  def _stop(self):
    self.settings.set('running', False)

  def run(self):
    self.settings.set('running', True)
    tick = 0
    while self.settings.get('running'):
      self.engine.render(self.screen)
      self.engine.tick(self._stop, pygame.event.get(), tick)
      tick += 1
      print(tick)

    print('done')
    pygame.quit()

if __name__ == "__main__":
  e = Engine()
  app = App(WIDTH, HEIGHT, 'Test Engine', 30, e)
  app.run()