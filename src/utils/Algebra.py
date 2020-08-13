import numpy as np


def normalize(vec):
  norm = np.linalg.norm(vec)
  if norm == 0: 
    return vec
  return vec / norm

def reflect(vec, normal):
  return vec - 2 * np.dot(vec, normal) * normal
