from .base_object import BaseObject
import numpy as np
from numba import double, typeof
from numba.experimental import jitclass


dt = np.double

spec = [
  ('position', double[:]),
]

@jitclass(spec)
class GroundPlane:

  def __init__(self):
    self.position = np.array([0,0,0], dt)

  def intersect(self, ray, hit):
    t = ray.origin[2] / ray.direction[2]

    if (t>0 and t < hit.distance):
        hit.distance = t
        #print(ray.origin + t * ray.direction)
        #print(typeof(ray.origin + t * ray.direction))
        hit.position = (ray.origin + t * ray.direction)
        hit.normal = np.array([0, 0, 1], dt)
    
    return hit