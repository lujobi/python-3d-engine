from .base_object import BaseObject

class Sphere(BaseObject):

  def __init__(self, pos, radius):
    self.radius = radius
    super().__init__(pos)

  def intersect(self, ray, hit):
    pass