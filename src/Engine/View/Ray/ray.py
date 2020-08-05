from numba import double   # import the types
from numba.experimental import jitclass

spec = [
  ('origin', double[:]),
  ('direction', double[:]),
]

@jitclass(spec)
class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = direction

  def __str__(self):
    return f'Ray:\n - Origin: {self.origin}\n - Direction: {self.direction}'