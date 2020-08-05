import numpy as np
from numba import double    # import the types
from numba.experimental import jitclass

spec = [
  ('position', double[:]),
  ('distance', double),
  ('normal', double[:]),
]

dt = np.double

@jitclass(spec)
class RayHit:
  def __init__(self, position=np.array([0,0,0], dt), distance=np.Inf, normal=np.array([0,0,0], dt)):
    self.position = position
    self.distance = distance
    self.normal = normal

  def __str__(self):
    return f'Ray hit:\n - Position: {self.position}\n - Distance: {self.distance}\n - Normal: {self.normal}'