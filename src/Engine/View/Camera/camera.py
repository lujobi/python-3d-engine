from ....utils.Algebra import normalize
from ..Ray.ray import Ray
from ..Ray.ray_hit import RayHit
from scipy.spatial.transform import Rotation as R
from ..Shader.temp import shade

import numpy as np

class Camera:
  def __init__(self, size, position, euler_angles, focal_length):
    self.size = size
    self.position = position
    self.rotation_matrix = R.from_euler('xyz', euler_angles).as_matrix()
    self.direction = np.matmul(self.rotation_matrix, np.array([0, 1, 0]))
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
        rays[x + z * height] = normalize(np.array([x_pix_pos[x], 0, z_pix_pos[z]]) - local_focal_point)

    return rays

  def dispatch_rays(self, objects):
    width, height = self.size
    dirs = np.matmul(self.basis_rays, self.rotation_matrix)

    res = np.zeros((width, height, 3))

    for i, d in enumerate(dirs):
      ray = Ray(self.focal_point, d)
      hit = RayHit()
      for obj in objects:
        hit = obj.intersect(ray, hit)

      res[i % width][int(i / height)] = shade(ray, hit)
    
    return res


