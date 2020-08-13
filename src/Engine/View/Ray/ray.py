import numpy as np


class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = direction
    self.energy = np.array([1.0,1.0,1.0])

  def __str__(self):
    return f'Ray:\n - Origin: {self.origin}\n - Direction: {self.direction}'