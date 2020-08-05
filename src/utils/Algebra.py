import numpy as np
from numba import guvectorize, float32, float64, jit

@guvectorize([(float32[:], float32[:]), (float64[:], float64[:])], '(n)->(n)')# fastmath=True)
#@jit([float32[:](float32[:])], fastmath=True)
def normalize(vec, res):
  norm = np.linalg.norm(vec)
  if norm == 0: res = vec
  else: res = vec / norm
