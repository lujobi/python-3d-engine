import numpy as np
from abc import ABC, abstractmethod

class BaseObject(ABC):

  def __init__(self, position):
    self.position = np.array(position)
    super().__init__()
  
  @abstractmethod
  def intersect(self, ray, hit):
    pass