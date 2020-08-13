import numpy as np
from src.utils.Algebra import reflect

def shade(ray, hit):
  if (hit.distance < np.Inf):

    specular = np.array([0.6, 0.6, 0.6])

    ray.origin = hit.position + hit.normal * 0.001
    ray.direction = reflect(ray.direction, hit.normal)
    ray.energy *= specular

    return ray, hit.normal * 128 + 128 # np.array([0,0,0]) #hit.normal * 128 + 128
  else:
    ray.energy = np.array([0,0,0])
    #theta = np.acos(ray.direction.y) / - np.pi
    #phi = atan2(ray.direction.x, -ray.direction.z) / - np.pi * 0.5
    #return _SkyboxTexture.SampleLevel(sampler_SkyboxTexture, float2(phi, theta), 0).xyz
    return ray, np.array([200,0,200])
  