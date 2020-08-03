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

  def _render_thread(self):
    render_count = 0
    fps = None
    t_last = time.time_ns()

    while self.settings.get('running'):

      if time.time_ns() - t_last > 1E9:
        t_last = time.time_ns()
        fps = render_count
        pygame.display.set_caption(f'{self._title} - at {fps} FPS, {self._requested_tps} TPS')
        render_count = 0     

      self.engine.render(self.screen)
      self.settings.incr('frame_since_update')
      render_count += 1

  def _stop(self):
    self.settings.set('running', False)


  def _tick_thread(self):
    tick_count = 0

    clock = pygame.time.Clock()

    while self.settings.get('running'):

      if self.engine.tick(self._stop, pygame.event.get(), tick_count):
        self.settings.set('frame_since_update', 0)
      
      tick_count += 1
      clock.tick(self._requested_tps)


  def run(self):
    self.settings.set('running', True)
    render_thread = threading.Thread(target=self._render_thread)
    tick_thread = threading.Thread(target=self._tick_thread)

    # Start treads and wait for them to stop
    render_thread.start()
    tick_thread.start()
    render_thread.join()
    tick_thread.join()

    print('done')
    pygame.quit()

if __name__ == "__main__":
  e = Engine()
  app = App(WIDTH, HEIGHT, 'Test Engine', 30, e)
  app.run()