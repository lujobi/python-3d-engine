from abc import ABC, abstractmethod

class BaseObject(ABC):

  def __init__(self, pos):
    self.pos = pos
    super().__init__()
  
  @abstractmethod
  def intersect(self, ray):
    pass