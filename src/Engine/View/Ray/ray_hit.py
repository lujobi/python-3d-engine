import numpy as np

class RayHit:
  def __init__(self, position=[0,0,0], distance=np.Inf, normal=[0,0,0]):
    self.position = position
    self.distance = distance
    self.normal = normal