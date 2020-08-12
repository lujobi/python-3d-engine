import numpy as np
from numba import guvectorize, double, jit

@guvectorize([(double[:], double[:]), (double[:], double[:])], '(n)->(n)')# fastmath=True)
def normalize(vec, res):
  norm = np.linalg.norm(vec)
  if norm == 0: res = vec
  else: res = vec / norm


# @jit(nopython=True, parallel = True, fastmath = True)
# def normalize(vec):
#   norm = np.linalg.norm(vec)
#   if norm == 0: return vec
#   return vec / norm

