from ....utils.Algebra import normalize
from ..Ray.ray import Ray
from ..Ray.ray_hit import RayHit
from scipy.spatial.transform import Rotation as R
from ..Shader.temp import shade

import numpy as np
from numba import jit, float32, typeof
from numba.experimental import jitclass

spec = [
  ('size', float32[:]),
  ('position', float32[:]),
  ('rotation_matrix', float32[:]),
  ('direction', float32[:]),
  ('focal_length', float32),
  ('focal_point', float32[:]),
  ('basis_rays', float32[:]),
]

dt = np.float32

#@jitclass(spec)
class Camera:
  def __init__(self, size, position, euler_angles, focal_length):
    self.size = size
    self.position = position
    self.rotation_matrix = R.from_euler('xyz', euler_angles).as_matrix()
    self.direction = np.matmul(self.rotation_matrix, np.array([0, 1, 0], dt))
    self.focal_length = focal_length
    self.focal_point = position - focal_length * self.direction
    self.basis_rays = self.precalc_basis_rays()

  def precalc_basis_rays(self):
    width, height = self.size
    aspect_ratio = width/height

    local_focal_point = np.array([0, -self.focal_length, 0])

    x_pix_pos = np.zeros(width)
    x_start = - 1 + 1 / width
    x_step = 2 / width 
    for x in range(width):
      x_pix_pos[x] = x_start + x * x_step

    z_pix_pos = np.zeros(height)
    z_start = - 1/aspect_ratio + 1 / height
    z_step = 2 / height 
    for z in range(height):
      z_pix_pos[z] = z_start + z * z_step

    rays = np.zeros((width*height, 3))
    for x in range(width):
      for z in range(height):
        rays[x + z * height] = normalize(np.array([x_pix_pos[x], 0, z_pix_pos[z]], dt) - local_focal_point)

    return rays

  def dispatch_rays(self, objects):
    return dispatch_rays(self.size, self.basis_rays, self.rotation_matrix, self.focal_point, objects)

#@vectorize([float32[::]((int32,int32), float32[::], float32[::], float32[:], pyobject)], fastmath = True)
@jit(nopython=True, parallel = True, fastmath = True)
def dispatch_rays(size, basis_rays, rotation_matrix, focal_point, objects):
  width, height = size
  dirs = np.dot(basis_rays, rotation_matrix)

  res = np.zeros((width, height, 3))

  for i, d in enumerate(dirs):
    ray = Ray(focal_point, d)
    hit = RayHit()
    for obj in objects:
      hit = obj.intersect(ray, hit)

    res[i % width][int(i / height)] = shade(ray, hit)
  
  return res

