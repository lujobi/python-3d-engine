import numpy as np

class RayHit:
  def __init__(self, position=[0,0,0], distance=np.Inf, normal=[0,0,0]):
    self.position = position
    self.distance = distance
    self.normal = normal

  def __str__(self):
    return f'Ray hit:\n - Position: {self.position}\n - Distance: {self.distance}\n - Normal: {self.normal}'