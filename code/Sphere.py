from Primitive import *
from Point import *
from Ray import *
from Vector import *
from Intersection import *

class Sphere(Primitive):
    def __init__(self):
        self.radius = 1
        super().__init__()

    def __str__(self):
        return "Sphere: {0}".format(super().__str__())
    
    def intersect(self, ray):
        sphere_to_ray = ray.origin - self.origin
        a = Vector.dot(ray.direction, ray.direction)
        b = 2 * Vector.dot(ray.direction, sphere_to_ray)
        c = Vector.dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = (b * b) - 4 * a * c
        if discriminant < 0:
            return None
        t1 = (-b - math.sqrt(discriminant)) / 2 * a
        t2 = (-b + math.sqrt(discriminant)) / 2 * a
        return Intersection([t1, t2], self)

