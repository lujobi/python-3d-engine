import numpy as np
from numba import jit

@jit
def shade(ray, hit):
  if (hit.distance < np.Inf):
    return hit.normal * 128 + 128
  else:
    #theta = np.acos(ray.direction.y) / - np.pi
    #phi = atan2(ray.direction.x, -ray.direction.z) / - np.pi * 0.5
    #return _SkyboxTexture.SampleLevel(sampler_SkyboxTexture, float2(phi, theta), 0).xyz
    return [0,0,255]
  