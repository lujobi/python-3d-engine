import numpy as np
from .base_object import BaseObject
from ...utils.Algebra import normalize
from numba import float32    # import the types
from numba.experimental import jitclass

spec = [
  ('position', float32[:]),
  ('radius', float32),
]

dt = np.float32

@jitclass(spec)
class Sphere:

  def __init__(self, position, radius):
    self.radius = radius
    self.position = np.array(position, dt)

  def intersect(self, ray, hit):
    d = ray.origin - self.position
    p1 = np.dot(ray.direction, d)
    p2sqr = p1 * p1 - np.dot(d, d) + self.radius * self.radius

    if (p2sqr < 0):
        return hit

    p2 = np.sqrt(p2sqr)
    t = - (p1 - p2  if p1 - p2 > 0  else p1 + p2)

    if (t>0 and t < hit.distance):
        hit.distance = t
        hit.position = ray.origin + t * ray.direction
        hit.normal = normalize(hit.position - self.position)
    
    return hit