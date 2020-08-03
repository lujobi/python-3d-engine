import threading

class LockableData:
  def __init__(self, **kwargs):
    self._data = kwargs
    self.lock = threading.Lock()

  def get(self, key):
    value = None
    self.lock.acquire()
    try:
      value = self._data.get(key)
    finally:
      self.lock.release()
      return value

  def set(self, key, value):
    self.lock.acquire()
    try:
      self._data[key] = value
    finally:
      self.lock.release()
  
  def incr(self, key):
    self.lock.acquire()
    try:
      self._data[key] += 1
    finally:
      self.lock.release()