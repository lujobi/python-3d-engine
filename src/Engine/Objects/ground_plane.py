from .base_object import BaseObject
import numpy as np

class GroundPlane(BaseObject):

  def __init__(self):
    super().__init__([0,0,0])

  def intersect(self, ray, hit):
    t = -ray.origin[2] / ray.direction[2]

    if (t>0 and t < hit.distance):
        hit.distance = t
        hit.position = np.array(ray.origin + t * ray.direction)
        hit.normal = np.array([0, 0, 1])
    
    return hit