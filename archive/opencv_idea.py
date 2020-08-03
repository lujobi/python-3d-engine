import cv2
import numpy as np
import time

import threading

WIDTH, HEIGHT = 200, 200
WIDTH, HEIGHT = 1000, 1000

class App:

  def __init__(self, width, height, requested_tps):
    self.height = height
    self.width = width
    self.requested_tps = requested_tps

    self.current_tps = 0
    self.base = np.array([[[0,0,0]]*self.width]*self.height, dtype='uint8')

    self.running = False
    self.s = 0

  def _tick(self):
    self.s += 20
    if self.s >= WIDTH * HEIGHT :
      self.s = 0

  def _render(self):
    image = np.copy(self.base)
    cv2.circle(image, (self.s % WIDTH, int(self.s / WIDTH)), 3, (255, 0, 0))
    return image

  def _render_thread(self):
    render_count = 0
    fps = None
    title = 'testing'
    t_last = time.time_ns()

    while self.running:

      if time.time_ns() - t_last > 1E9:
        t_last = time.time_ns()
        fps = render_count
        print(f'{title} - at {fps} FPS, {self.current_tps} TPS')
        render_count = 0

      cv2.imshow('test', self._render())
      render_count += 1

      key = cv2.waitKey(1) & 0xFF

      if key == ord('q'):
        self.running = False

  def _tick_thread(self):
    tick_count = 0
    t_l = time.time_ns()
    t_l2 = time.time_ns()

    while self.running:
      if time.time_ns() - t_l > 1E9:
        t_l = time.time_ns()
        self.current_tps = tick_count
        tick_count = 0

      if (time.time_ns() - t_l2 > 1E9/self.requested_tps):
        t_l2 = time.time_ns()
        self._tick()
        tick_count += 1

      else:
        time.sleep(0.0001)


  def run(self):
    self.running = True
    render_thread = threading.Thread(target=self._render_thread)
    tick_thread = threading.Thread(target=self._tick_thread)

    # Start treads and wait for them to stop
    render_thread.start()
    tick_thread.start()
    render_thread.join()
    tick_thread.join()

    print('done')
    cv2.destroyAllWindows()


if __name__ == "__main__":
  app = App(WIDTH, HEIGHT, 30)
  app.run()